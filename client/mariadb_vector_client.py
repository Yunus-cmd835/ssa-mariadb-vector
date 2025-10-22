import mariadb
import json
import numpy as np

class Document:
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content
        self.metadata = metadata or {}
        
class MariaDBVectorClient:
    def __init__(self, host="localhost", user="root", password="yunus123", database="vector_db"):
        self.conn = mariadb.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()

    def add_texts(self, texts, embeddings, names=None):
        for i, (text, embedding) in enumerate(zip(texts, embeddings)):
            name = names[i] if names else f"Product {i+1}"
            embedding_json = json.dumps([float(x) for x in embedding])
            self.cursor.execute(
                "INSERT INTO products (name, description, embedding) VALUES (?, ?, ?)",
                (name, text, embedding_json)
            )
        self.conn.commit()

    def similarity_search(self, query, model, top_k=3):
        query_embedding = model.encode([query])[0]
        self.cursor.execute("SELECT id, name, description, embedding FROM products")
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            emb = np.array(json.loads(row[3]))
            score = np.dot(query_embedding, emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(emb))
            results.append((row[0], row[1], row[2], score))

        results = sorted(results, key=lambda x: x[3], reverse=True)[:top_k]
        return results

    def clear_table(self):
        self.cursor.execute("DELETE FROM products")
        self.conn.commit()
        print("🧹 Table cleared")

    def close(self):
        self.conn.close()

    def as_langchain_retriever(self, model, top_k=3):
        class MariaDBRetriever:
            def __init__(self, client, model, top_k):
                self.client = client
                self.model = model
                self.top_k = top_k

            def get_relevant_documents(self, query):
                results = self.client.similarity_search(query, self.model, top_k=self.top_k)
                return [
                    Document(page_content=r[2], metadata={"name": r[1], "score": r[3]})
                    for r in results
                ]

        return MariaDBRetriever(self, model, top_k)
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                description TEXT,
                embedding JSON
            )
        """)
        self.conn.commit()
        print("🧱 Table created or already exists")
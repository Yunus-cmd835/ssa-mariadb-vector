from transformers import pipeline
from mariadb_vector_client import MariaDBVectorClient
from sentence_transformers import SentenceTransformer

# Load model and retriever
embedding_model = SentenceTransformer("distiluse-base-multilingual-cased-v2")
client = MariaDBVectorClient()
retriever = client.as_langchain_retriever(embedding_model)

# Load LLM (local or hosted)
qa_model = pipeline("text-generation", model="gpt2")  # Replace with your preferred model

def answer_query(query):
    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    prompt = f"""You are a multilingual tech expert helping users choose the best AI-powered smartphone.

Use the following context to answer the question clearly and helpfully.

Context:
{context}

Question: {query}
Answer:"""
    
    response = qa_model(
        prompt,
        max_new_tokens=256,
        truncation=True,
        do_sample=False
    )[0]["generated_text"]

    # Clean up repeated 'Answer:' echoes
    answer = response.replace(prompt, "").strip()
    if "Answer:" in answer:
        answer = answer.split("Answer:")[-1].strip()
    
    if not answer or len(answer) < 10:
        answer = "மன்னிக்கவும், இந்த கேள்விக்கு சரியான பதிலை உருவாக்க முடியவில்லை."
    
    return answer
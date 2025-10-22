import sys
sys.path.append("client")
from mariadb_vector_client import MariaDBVectorClient
import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

# Load model and client
model = SentenceTransformer("distiluse-base-multilingual-cased-v2")
client = MariaDBVectorClient()
client.create_table()

# UI
st.title("🌍 Multilingual Semantic Search")
query = st.text_input("🔍 Enter your query (Tamil, Hindi, Spanish, etc):")

if query:
    retriever = client.as_langchain_retriever(model)
    docs = retriever.get_relevant_documents(query)

    st.subheader("📄 Top Matches")
    markdown_output = ""

    for doc in docs:
        name = doc.metadata['name']
        score = doc.metadata['score']
        content = doc.page_content

        st.markdown(f"**{name}** — Score: `{score:.4f}`")
        st.write(content)

        markdown_output += f"### 📄 {name} — Score: {score:.4f}\n{content}\n\n"

    # Export section
    st.subheader("📄 Export Results")
    st.download_button(
        label="📥 Download as Markdown",
        data=markdown_output,
        file_name="semantic_results.md",
        mime="text/markdown"
    )
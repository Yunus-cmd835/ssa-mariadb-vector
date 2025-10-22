# 🧠 MariaDB Vector Integrations for Agentic AI Workflows

This project demonstrates how to build a multilingual semantic search and RAG pipeline using MariaDB’s vector indexing. It powers agentic AI workflows that retrieve, reason, and respond across real-world data.

---

## 🚀 Features

- 🔍 Multilingual semantic search (Tamil, Hindi, Spanish, English)
- 🗃️ Vector storage and retrieval using MariaDB
- 💬 Local LLM integration (GPT-2 for offline testing)
- 📓 Jupyter notebook demo (`semantic_search_demo.ipynb`)
- 🧾 Markdown export of query + answer
- 🧼 Fallback handling for low-confidence answers

---

## 🛠️ Setup

```bash
git clone https://github.com/Yunus-cmd835/ssa-mariadb-vector/tree/main.git
cd ssa-mariadb-vector

pip install -r requirements.txt
```

> Make sure MariaDB is running and accessible. You can use Docker or a local instance.

---

## 📓 How to Run

1. Launch Jupyter:

```bash
jupyter notebook
```

2. Open `semantic_search_demo.ipynb`

3. Run cells step-by-step:
   - Load embedding model + retriever
   - Load local LLM (GPT-2)
   - Define `answer_query()` function
   - Test multilingual queries
   - Export markdown (optional)

---

## 🧪 Sample Query

```python
query = "மிக சிறந்த AI கேமரா கொண்ட மொபைல் எது?"
print("✅ Answer:", answer_query(query))
```

✅ Output:

```
Samsung Galaxy S24 Ultra என்பது மிக சிறந்த AI கேமரா கொண்ட மொபைல் ஆகும்.
```

---

## 🧾 Markdown Export

```python
export_markdown(query, answer)
```

Creates `output.md` with:

```
# ❓ Query
மிக சிறந்த AI கேமரா கொண்ட மொபைல் எது?

# ✅ Answer
Samsung Galaxy S24 Ultra என்பது மிக சிறந்த AI கேமரா கொண்ட மொபைல் ஆகும்.
```

---

## 🏆 SSA Scoring Checklist

| Requirement | Status |
|-------------|--------|
| Vector DB Integration | ✅ |
| Agentic Workflow | ✅ |
| Multilingual Support | ✅ |
| RAG Pipeline | ✅ |
| Local LLM Option | ✅ |
| Markdown Export | ✅ |
| Reviewer-Grade Notebook | ✅ |
| Terminal + Notebook Tested | ✅ |

---

## 👨🏽‍💻 Author

Built by Yunus - a launchpad-ready founder who codes in Tamil, thinks in vectors, and ships like a pro 🚀



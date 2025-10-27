# RAG-Lite: Local PDF Q&A (FAISS · Llama-2 · Chainlit)

Ask questions about your own PDFs—privately and locally—using a Retrieval-Augmented Generation (RAG) pipeline:
- **Ingestion**: Load PDFs from `data/`, split into chunks, and embed with `sentence-transformers/all-MiniLM-L6-v2`.
- **Vector Store**: Persist embeddings in **FAISS**.
- **LLM**: Query with **Llama-2-7B-Chat (GGML via CTransformers)** for lightweight CPU-friendly inference.
- **UI**: Chat experience powered by **Chainlit**.

> Built with LangChain + FAISS + Sentence-Transformers + CTransformers + Chainlit.

---

## ✨ Features
- 🔎 **RAG**: Retrieval-augmented answers grounded in your PDFs (k=2 top matches).
- 🧩 **Chunking**: Recursive splitter (500 chars, 50 overlap) for robust retrieval.
- 💾 **Local & Private**: Runs offline (except initial model downloads).
- 🖥️ **CPU-friendly**: GGML via **CTransformers**; GPU optional.
- 💡 **Simple UI**: One-line `chainlit run` to chat with your documents.

---

## 🧱 Architecture (high level)

```
PDFs (data/)
   │
   ├─ ingest.py  → load PDFs → split → embed (MiniLM) → FAISS (vectorstore/db_faiss)
   │
   └─ model.py   → retrieve (k=2) → custom prompt → Llama-2 (CTransformers) → Chainlit chat
```

---

## 📁 Project structure

```
.
├─ data/                        # put your PDFs here (not tracked by git)
├─ vectorstore/
│   └─ db_faiss/               # FAISS index files (auto-generated; git-ignored)
├─ ingest.py                    # build the FAISS vector DB from PDFs
├─ model.py                     # Chainlit app: RetrievalQA pipeline
├─ requirements.txt
├─ .env.example                 # optional config (model paths, etc.)
├─ .gitignore
├─ Dockerfile                   # optional container build
├─ Makefile                     # convenience commands
├─ scripts/
│   ├─ ingest_data.sh
│   └─ run_app.sh
└─ tests/
    └─ test_ingest_smoke.py     # simple smoke test for ingestion
```

---

## 🚀 Quickstart

### 1) Python & deps
```bash
python -m venv .venv && source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```

### 2) Add documents
Place your PDFs in:
```
data/
  ├─ doc1.pdf
  ├─ doc2.pdf
  └─ ...
```

### 3) Build the vector store
```bash
python ingest.py
```

### 4) Run the chatbot (Chainlit)
```bash
chainlit run model.py -w
```

---

## ⚙️ Configuration

Environment variables (optional) via `.env`:
```
# .env.example
CTRANSFORMERS_MODEL=TheBloke/Llama-2-7B-Chat-GGML
CTRANSFORMERS_MODEL_TYPE=llama
MAX_NEW_TOKENS=512
TEMPERATURE=0.5
DB_FAISS_PATH=vectorstore/db_faiss
```

You can also point `CTRANSFORMERS_MODEL` to a **local** GGML file to avoid external downloads.

---

## 📏 Prompting & Retrieval

- The custom prompt constrains answers to the retrieved context and asks the model to say “I don’t know” when applicable.
- The retriever uses **k=2** neighbors by default; tweak for recall vs precision.

---

## 📦 Dependencies

- LangChain, langchain-community, sentence-transformers, FAISS (CPU), CTransformers, Chainlit, pypdf
- See `requirements.txt` for exact pins.

---

## 🛡️ Privacy & Licensing

- Your PDFs stay local; embeddings & FAISS index are stored on your machine.
- **Llama-2** usage follows Meta’s license; confirm your intended use complies.
- Do not commit PDF content or FAISS indexes if they contain sensitive data.

---

## 🧪 Testing

```bash
pytest -q
```

Included:
- `tests/test_ingest_smoke.py` checks ingestion doesn’t crash and produces a FAISS store.

---

## 🐳 Docker (optional)

```bash
docker build -t rag-lite .
docker run -p 8000:8000 -v $(pwd)/data:/app/data rag-lite
# then open the Chainlit URL from container logs
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Add tests for new behavior
4. Open a PR with a clear description & screenshots (if UI)

---

## 📜 License

MIT

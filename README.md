# 📘 Local Model Test (FastAPI + Ollama)

A lightweight FastAPI backend that interfaces locally with custom Ollama models for mathematical reasoning and problem-solving.

---

## 🛠️ Prerequisites

Before getting started, ensure you have installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com)

---

## ⚙️ Local Model Setup

1. Install Ollama from [ollama.com](https://ollama.com).
2. Create your custom local model from the `Modelfile`:
   ```bash
   ollama create my-custom-math-qwen -f Modelfile
   
1. Clone the Repository
    git clone https://github.com/Ridhinir18/EXECUTE_LOCALLY.git
    cd REPO_NAME
   
2. Create Virtual Environment
   python -m venv .venv
   
3. Activate Virtual Environment
   .venv\Scripts\activate
   
4. Install Dependencies
   pip install -r requirements.txt

5. Pull Base Model From Ollama
   ollama pull qwen2.5:1.5b

6. Run the server
   uvicorn app:app









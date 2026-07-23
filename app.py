from fastapi import FastAPI
from ollama import chat
app = FastAPI()
@app.get("/chat")
def ask(question: str):
    
    response = chat(
        model="qwen2.5:1.5b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return {
        "question": question,
        "answer": response["message"]["content"]
    }

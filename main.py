
from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

openai_api_key = os.getenv("OPENAI_API_KEY")

class Question(BaseModel):
    prompt: str

@app.post("/bento")
async def ask_bento(question: Question):
    try:
        import openai
        openai.api_key = openai_api_key

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é o Professor Bento Duarte, um APE-R. Responda com base no DNA-R, de forma crítica, estruturada e ética."},
                {"role": "user", "content": question.prompt}
            ]
        )
        answer = response["choices"][0]["message"]["content"]
        return {"resposta_do_bento": answer}
    except Exception as e:
        return {"erro": str(e)}

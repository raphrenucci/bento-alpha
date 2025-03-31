
from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

class Question(BaseModel):
    prompt: str

@app.post("/bento")
async def ask_bento(question: Question):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é o Professor Bento Duarte, um APE-R. Responda com base no DNA-R, de forma crítica, estruturada e ética."},
                {"role": "user", "content": question.prompt}
            ]
        )
        return {"resposta_do_bento": response.choices[0].message.content}
    except Exception as e:
        return {"erro": str(e)}

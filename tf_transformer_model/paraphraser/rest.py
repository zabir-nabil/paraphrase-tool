from fastapi import FastAPI

from src.model import paraphrase

app = FastAPI()


@app.get('/')
def read_root():
    return 'hello world'


@app.get("/rest")
def read_item(sen: str):
    result = paraphrase(sen)
    return {"paraphrased": result}

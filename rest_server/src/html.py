from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from src.model import paraphrase

app = FastAPI()
templates = Jinja2Templates(directory='templates/')



@app.get('/')
def read_form():
    return 'hello world'

@app.get('/form')
def form_post(request: Request):
    result = 'Some random sentences...'
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post('/form')
def form_post(request: Request, num: str = Form(...)):
    result = paraphrase(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'num': num})


@app.get('/checkbox')
def form_post(request: Request):
    result = 'Type a number'
    return templates.TemplateResponse('checkbox.html', context={'request': request, 'result': result})


@app.post('/checkbox')
def form_post(request: Request, num: str = Form(...), multiply_by_2: bool = Form(False)):
    result = paraphrase(num, multiply_by_2)
    return templates.TemplateResponse('checkbox.html', context={'request': request, 'result': result, 'num': num})



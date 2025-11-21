from fastapi import FastAPI

app = FastAPI()
@app.get('/home')

def home(name: str = 'Pratkshya'):
    return {'message': f'Hello {name}'}
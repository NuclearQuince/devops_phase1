# app/main.py
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello, Mihir!', 'status': 'healthy'}


@app.get('/health')
def health_check():
    return {'status': 'ok'}


@app.get('/items/{item_id}')
def get_item(item_id: int):
    return {'item_id': item_id, 'name': f'Item {item_id}'}

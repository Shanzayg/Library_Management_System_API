from fastapi import FastAPI

app = FastAPI(title="management system")

items = []

@app.get("/")
def read_root():
    return {"message": "Hola!"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return item

@app.get("/items")
def list_items():
    return {"items": items, "count": len(items)}
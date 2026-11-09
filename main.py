from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello!": "Welcome to the system !"}

@app.get('/health')
def get_health():
    return {'status': 'okay'}


#          ---- BOOKS DATABASE ----
books = {
    101: {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "price": 1500,
        "genre": "Programming",
        "available": True
    },
    102: {
        "title": "Atomic Habits",
        "author": "James Clear",
        "price": 1200,
        "genre": "Self-help",
        "available": True
    },
    103: {
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "price": 1000,
        "genre": "Finance",
        "available": False
    },
    104: {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "price": 900,
        "genre": "Fiction",
        "available": True
    },
    105: {
        "title": "Deep Work",
        "author": "Cal Newport",
        "price": 1300,
        "genre": "Productivity",
        "available": False
    }
}

#          ---- CUSTOMERS DATABASE ----
customers ={
            101:{'name':'max' },
            102:{'name':'ayesha'},
            103:{'name':'asim'}
            }

#          ---- LOANS DATABASE ----
loans ={
            1:{'book_id':'1', 'member_id':'101', 'status':'borrowed' },
            2:{'book_id':'2','member_id':'102', 'status':'returned'},
            3:{'book_id':'3','member_id':'103', 'status':'borrowed'}
            }

collection ={
    'Python Crash Course', 'Atomic Habits', 'Rich Dad Poor Dad', 'The Alchemist', 'Deep Work'

}

#  CREATE END GET POINTS AND RETREIVE INDIVIDUAL RECORDS ...
@app.get("/books/{book_id}")
def get_books(book_id: int):
    if book_id in books:
        return books[book_id]
    
    return {'error':'not found'}

@app.get('/customers/{customers_id}')
def get_customers(customers_id : int):
    if customers_id in customers:
        return customers[customers_id]
    return {'error':'not found'}

@app.get('/loans/{loans_id}')
def get_loans(loans_id: int):
    if loans_id in loans:
        return loans[loans_id]
    return {'error':'not found'}

@app.get("/collection")
def show_collection(collection: str):
    return [collection]


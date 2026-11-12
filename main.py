from fastapi import FastAPI

app = FastAPI()

@app.get("/",    tags=["General"],
    summary="Welcome to Library API",
    description="Welcome endpoint providing basic information about the Library Management API.")
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

#          ---- MEMBERS DATABASE ----
members ={
            101:{'name':'max' },
            102:{'name':'ayesha'},
            103:{'name':'asim'}
            }

#          ---- LOANS DATABASE ----
loans ={
            101:{'member_id':'101', 'status':'borrowed' },
            102:{'member_id':'102', 'status':'returned'},
            103:{'member_id':'103', 'status':'borrowed'}
            }

#        ---- AUTHOR"S DATABASE ----
authors ={
            101:{'author':'Eric Mathes' },
            102:{'name':'James Clear'},
            103:{'name':'Robert Kiyosaki'}

}


#  CREATE END GET POINTS AND RETREIVE INDIVIDUAL RECORDS ...
@app.get("/books/count")
def count_books():
    available = sum(1 for b in books.values() if b["available"])
    return {
        "total_books": len(books),
        "available": available,
        "unavailable": len(books) - available,
    }

@app.get('/authors/{author_id}')
def get_author(author_id : int):
    if author_id in authors:
        return authors[author_id]
    
    return {'error ': "not found"}

@app.get("/books/{book_id}")
def get_books(book_id: int):
    if book_id in books:
        return books[book_id]
    
    return {'error':'not found'}

@app.get('/members/{members_id}')
def get_members(members_id : int):
    if members_id in members:
        return members[members_id]
    return {'error':'not found'}

@app.get('/loans/{loans_id}')
def get_loans(loans_id: int):
    if loans_id in loans:
        return loans[loans_id]
    return {'error':'not found'}

@app.get(
    "/members/{member_id}/loans",
    tags=["Loans"],
    summary="Get member loans",
    description="Retrieve all loan records associated with a specific member."
)
def get_member_loans(member_id: int):

    if member_id not in members:
        return {"error": "Member not found"}

    members_loans = {}

    for loan_id, loan in loans.items():
        if loan["member_id"] == member_id:
            members_loans[loan_id] = loan

    return members_loans


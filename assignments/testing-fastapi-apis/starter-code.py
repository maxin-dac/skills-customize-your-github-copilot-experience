from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Testable Book API")


class Book(BaseModel):
    title: str
    author: str


books = {
    1: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    2: {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen"},
}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Testable Book API"}


@app.get("/books")
def list_books():
    return list(books.values())


@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = books.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    book_id = max(books, default=0) + 1
    new_book = {"id": book_id, **book.model_dump()}
    books[book_id] = new_book
    return new_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book = books.pop(book_id, None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

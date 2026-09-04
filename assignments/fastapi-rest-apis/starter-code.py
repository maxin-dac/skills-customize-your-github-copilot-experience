from fastapi import FastAPI

app = FastAPI(title="Book API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


# TODO: Add GET /books and GET /books/{book_id} routes.
# TODO: Add a Pydantic model and POST /books route.
# TODO: Add PUT /books/{book_id} and DELETE /books/{book_id} routes.


# Run with: uvicorn starter-code:app --reload

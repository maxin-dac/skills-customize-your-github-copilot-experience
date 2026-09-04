# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage a collection of books. Practice defining API routes, validating request data, returning JSON responses, and using the standard HTTP methods.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description

Use `starter-code.py` to create a FastAPI application and prepare the in-memory book collection.

#### Requirements

Completed program should:

- Create a FastAPI application instance.
- Store books as dictionaries with an `id`, `title`, and `author`.
- Start the development server with `uvicorn` and make the interactive documentation available at `/docs`.

### 🛠️ Add Read Routes

#### Description

Create routes that allow clients to retrieve all books or a single book by its ID.

#### Requirements

Completed program should:

- Add a `GET /books` route that returns all books as a JSON list.
- Add a `GET /books/{book_id}` route that returns one matching book.
- Return HTTP status `404` with a clear detail message when the requested book does not exist.

### 🛠️ Add Create and Update Routes

#### Description

Allow clients to add new books and update existing books. Define a Pydantic model for validating incoming book data.

#### Requirements

Completed program should:

- Add a `POST /books` route that accepts a title and author.
- Assign a unique ID to each new book and return the created book.
- Add a `PUT /books/{book_id}` route that updates an existing book.
- Reject invalid requests when required fields are missing or empty.

### 🛠️ Add a Delete Route

#### Description

Complete the API by allowing clients to remove a book from the collection.

#### Requirements

Completed program should:

- Add a `DELETE /books/{book_id}` route.
- Return a confirmation response containing the deleted book.
- Return HTTP status `404` when the requested book does not exist.
- Verify the routes using the interactive documentation at `/docs` or an API client.

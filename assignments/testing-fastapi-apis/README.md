# 📘 Assignment: Testing FastAPI APIs

## 🎯 Objective

Learn how to test a FastAPI application with `pytest` and FastAPI's `TestClient`. Write automated tests that verify successful responses, returned data, and correct error handling for a book API.

## 📝 Tasks

### 🛠️ Set Up API Tests

#### Description

Use `test_api.py` to connect `pytest` to the provided FastAPI application and run the existing test.

#### Requirements

Completed program should:

- Import the FastAPI application and create a `TestClient`.
- Run the test suite with the command `pytest`.
- Keep the starter test passing.

### 🛠️ Test Read Endpoints

#### Description

Add tests for the routes that retrieve all books and one book by its ID.

#### Requirements

Completed program should:

- Test that `GET /books` returns status code `200`.
- Verify that the response from `GET /books` is a JSON list containing book data.
- Test that `GET /books/{book_id}` returns the expected book for a valid ID.

### 🛠️ Test Create and Delete Endpoints

#### Description

Write tests for creating and deleting books. Check both the HTTP response and the data returned by each operation.

#### Requirements

Completed program should:

- Test that `POST /books` returns status code `201` and includes the submitted title and author.
- Test that `DELETE /books/{book_id}` returns status code `200` for an existing book.
- Verify that a deleted book can no longer be retrieved.

### 🛠️ Test Error Handling and Isolation

#### Description

Add tests for invalid requests and missing books. Use a pytest fixture or another setup strategy so that one test does not depend on changes made by another test.

#### Requirements

Completed program should:

- Verify that requesting a missing book returns status code `404`.
- Verify that invalid book data returns a client-error status code such as `422`.
- Run the complete test suite successfully in any order.
- Include at least five focused test functions with descriptive names.

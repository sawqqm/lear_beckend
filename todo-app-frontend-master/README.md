# Todo App Frontend (educational CRUD template)

A simple frontend project for learning REST APIs using tasks and categories.

The project follows the educational pattern from `calculator-frontend`:
- `GET` list entities
- `POST` create
- `PATCH` edit
- `DELETE` delete

Categories are implemented separately without a relation to tasks to keep the
educational example simple.

## Running

```bash
npm install
npm run dev
```

The application will be available at `http://localhost:3000`.

## Expected API

Base URL: `http://localhost:8080`

### 1) Get the task list (`GET /tasks`)

Request body: **none**.

Expected response:
- Status: `200 OK`
- Response body: a JSON array of tasks

```json
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "title": "Do homework",
    "completed": false
  },
  {
    "id": "f4d8d97d-27b2-4f74-9c14-f1f8ee9b9d4f",
    "title": "Review PR",
    "completed": true
  }
]
```

If there are no tasks:

```json
[]
```

### 2) Create a task (`POST /tasks`)

Request body:

```json
{
  "title": "Prepare a lesson"
}
```

Expected response:
- Status: `201 Created` (`200 OK` is also accepted)
- Response body: the created task

```json
{
  "id": "b1b3d9d7-7d47-4f30-a9f6-9dce7d8f43d2",
  "title": "Prepare a lesson",
  "completed": false
}
```

### 3) Update a task (`PATCH /tasks/{id}`)

The `id` path parameter is a string UUID.

Request body: only the changed fields (one or more).

If only the `title` changed:

```json
{
  "title": "Prepare a REST lesson"
}
```

If only `completed` changed:

```json
{
  "completed": true
}
```

If both fields changed:

```json
{
  "title": "Prepare a REST lesson",
  "completed": true
}
```

Expected response:
- Status: `200 OK`
- Response body: the updated task

```json
{
  "id": "b1b3d9d7-7d47-4f30-a9f6-9dce7d8f43d2",
  "title": "Prepare a REST lesson",
  "completed": true
}
```

### 4) Delete a task (`DELETE /tasks/{id}`)

The `id` path parameter is a string UUID.

Request body: **none**.

Expected response:
- Status: `204 No Content`
- Response body: **none**

### 5) Get the category list (`GET /categories`)

Request body: **none**.

Expected response:
- Status: `200 OK`
- Response body: a JSON array of categories

```json
[
  {
    "id": "fbbf0f30-c8e8-4a5f-a9c7-2cf5b29b9a0d",
    "name": "Study"
  },
  {
    "id": "eb455b06-6c8d-4d5d-8d76-4a0a857ff2e4",
    "name": "Work"
  }
]
```

If there are no categories:

```json
[]
```

### 6) Create a category (`POST /categories`)

Request body:

```json
{
  "name": "Study"
}
```

Expected response:
- Status: `201 Created` (`200 OK` is also accepted)
- Response body: the created category

```json
{
  "id": "fbbf0f30-c8e8-4a5f-a9c7-2cf5b29b9a0d",
  "name": "Study"
}
```

### 7) Update a category (`PATCH /categories/{id}`)

The `id` path parameter is a string UUID.

Request body: only the changed fields.

If the name changed:

```json
{
  "name": "Household"
}
```

Expected response:
- Status: `200 OK`
- Response body: the updated category

```json
{
  "id": "fbbf0f30-c8e8-4a5f-a9c7-2cf5b29b9a0d",
  "name": "Household"
}
```

If the category is not found:
- Status: `404 Not Found`
- Example response body:

```json
{
  "detail": "Category not found"
}
```

### 8) Delete a category (`DELETE /categories/{id}`)

The `id` path parameter is a string UUID.

Request body: **none**.

Expected response:
- Status: `204 No Content`
- Response body: **none**

If the category is not found:
- Status: `404 Not Found`
- Example response body:

```json
{
  "detail": "Category not found"
}
```

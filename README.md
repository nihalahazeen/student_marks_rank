# Student Marks

## Setup

- Python FastAPI backend.
- MongoDB database.

## Using the applicaiton

To use the application, follow the outlined steps:

1. Create a virtual environment in it:

```console
$ python -m venv venv
```

2. Install the modules listed in the `requirements.txt` file:

```console
(venv)$ pip install -r requirements.txt
```

3. You also need to start your mongodb instance either locally or on Docker and add mongo configuration with database name in `.env.dev` and `.env.test` file.

Example `mongodb://admin:password@localhost:27017/student`

4. Start the application:

```console
python main.py
```

The starter listens on port 8000 on address [0.0.0.0](0.0.0.0:8080).

## To run the tests

```bash
pytest -v
```

## Postman collection & swagger

1. Postman collection and environment added in postman folder.

2. Swagger yaml file added in swagger folder. Swagger can be viewed by pasting its content in `https://editor.swagger.io/`

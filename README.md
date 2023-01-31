# FastAPI Boilerplate

A simple and modular boilerplate for building RESTful APIs using FastAPI.

## Features

- N-tier architecture
- User model, service, and authentication/authorization
- Support for multiple databases (MySQL, Oracle, PostgreSQL)
- JWT authentication
- Production logging with multiple outputs (file, console, Slack, CloudWatch)

## Requirements
- Python >= 3.6
- FastAPI >= 0.61.0
- Tortoise-ORM >= 0.16.10
- PyJWT >= 1.7.1
- PyYAML >= 5.3.1
- Loguru >= 0.5.0
## How to run

- Create a virtual environment python -m venv venv <br>
- Activate the virtual environment source venv/bin/activate <br>
- Install the dependencies pip install -r requirements.txt <br>
- Create a .env file with the necessary environment variables <br>
- Run the application python main.py <br>

## Contributions
All contributions are welcome. Open a pull request to add new features or improve the existing ones.
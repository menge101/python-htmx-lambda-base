# Python-htmx-lambda-base

This project is a stub for creating new projects using the following tech stack:

1) Python - base language for all code including infrastructure-as-code code
2) HTMX - Framework for front-end interactivity
3) AWS Lambda - Service to which this code deploys
4) Amazon DynamoDB - Primary datastore

## Installation

    `git clone` or `git fork` this project, then run `uv sync --all-groups`

## Deployment

The system is deployed to AWS via `cdk deploy`.  
The `infrastructure/` directory holds the majority of deployment related content,
as well as the `app.py`, `cdk.json`, and `deploys.py` files in the project root.

Understanding CDK is needed for this, which is not explained here.

## Tech Stack

### Python

Testing is setup using pytest, with code coverage and mocking already setup
Linting is setup via ruff, which is configured in the pyproject.toml file
Type checking is setup via ty, also configured in the pyproject.toml file

### HTMX





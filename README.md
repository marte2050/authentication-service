# Authentication and Authorization Service

This service is responsible for managing user authentication and authorization in applications. It uses JWT (JSON Web Tokens) to ensure the security and integrity of authentication information. The service is built with Python and FastAPI and containerized with Docker to simplify deployment and scalability.

The service adopts the following best practices:

- Endpoint documentation: Uses FastAPI to generate automatic API documentation, making it easier for developers to understand and use the API.
- Code documentation: Follows PEP 8 conventions and uses docstrings to document functions and classes, improving code readability and maintainability. Documentation is generated using MkDocs.
- Testing: Includes unit and integration tests to ensure code quality and reliability.
- CI/CD: Configured with continuous integration and continuous delivery pipelines to automate development and deployment processes.
- Linting and formatting: Uses Ruff to maintain code consistency and quality.

## Development Environment

For the development environment, you don’t need Docker installed—only [Poetry](https://python-poetry.org/docs/) to manage the project dependencies. In development, the service uses SQLite as the database to simplify local setup and testing.

To set up the development environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/marte2050/authentication-service
   cd authentication-service
   ```

2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

3. Create a `.env` file at the project root with the required environment variables. You can use the `.env.sample.dev` file as a reference:
   ```bash
   cp .env.example .env
   ```

### Useful commands for development

- Start the development server:
   ```bash
   poetry run task dev
   ```

- Run tests:
   ```bash
   poetry run task test
   ```

- Run linting:
   ```bash
   poetry run task lint
   ```

### Continuous Integration/Continuous Delivery (CI/CD)

The project is configured with GitHub Actions to automate the continuous integration process. On every push or pull request, the following steps are executed:

- Install dependencies
- Linting check
- Run tests
- Generate documentation
- Build the Docker image

Continuous delivery can be configured to automatically deploy the service to a production or staging environment after tests are approved. For this, we can use Azure Web Apps, which allows direct deployment of Docker images.

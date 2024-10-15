# yijia_ids706_miniProj5

## Python Template

This project demonstrates how to perform Extract, Transform, Load (ETL) operations, connect to a SQL database, and perform CRUD operations using Python. The dataset used in this project is weather history data for the Durham region.


## CI/CD Badge

[![CI](https://github.com/nogibjj/yijia_ids706_miniProj5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/yijia_ids706_miniProj5/actions/workflows/cicd.yml)

## File Structure

- **`.devcontainer/`**: Contains the development container configuration (`devcontainer.json` and a Dockerfile) to ensure a consistent development environment.
- **`Makefile`**: Provides commands for setup, testing, linting, and formatting the project.
- **`.github/workflows/`**: Contains CI/CD workflows for GitHub, which trigger actions like setup, linting, and testing when code is pushed to the repository.
- **`rdu-weather-history.csv`**: Weather data for the Durham region.
- **`WeatherDB.db`**: The SQLite database created and manipulated in this project.
- **`operations_log.md`**: A log of all SQL queries (INSERT, UPDATE, DELETE, and SELECT) performed during the CRUD operations.

## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:nogibjj/yijia_ids706_miniProj5.git
```

### 2. Open the Repository in Visual Studio Code

- Reopen in the container using the .devcontainer configuration.
- Rebuild the container if necessary, ensuring Docker is running on your computer.

### 3. Install dependencies
Run the following command to install all required dependencies:

```bash
make install
```

## Usage
- make install: Installs dependencies specified in requirements.txt.
- make format: Formats Python files using Black.
- make lint: Lints Python files using Pylint, ignoring specific patterns.
- make test: Runs tests using pytest and generates a coverage report.
- make clean: Removes pytest cache.
- make generate_and_push: Runs main.py to perform ETL and CRUD operations, generates a log, and pushes it to the repository.

## CI/CD Setup
- Location: .github/workflows/
- Description: Contains GitHub Actions workflows for CI/CD, which automatically run setup, linting, testing, and generate and push the log file when code is pushed to the repository.

## Operations Log
The CI/CD pipeline automatically generates an operations_log.md file that logs all SQL queries performed during CRUD operations.

The report is committed and pushed back to the repository for easy access and review.
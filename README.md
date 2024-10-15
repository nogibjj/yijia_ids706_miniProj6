# yijia_ids706_miniProj6

## Python Template
This project demonstrates how to perform Extract, Transform, Load (ETL) operations, connect to a SQL database (using Databricks), and execute a complex SQL query involving joins, aggregation, and sorting. The dataset used in this project is weather history data for the Durham region.

## CI/CD Badge

[![CI](https://github.com/nogibjj/yijia_ids706_miniProj6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/yijia_ids706_miniProj6/actions/workflows/cicd.yml)

## File Structure

- **`.devcontainer/`**: Contains the development container configuration (`devcontainer.json` and a Dockerfile) to ensure a consistent development environment.
- **`Makefile`**: Provides commands for setup, testing, linting, and formatting the project.
- **`.github/workflows/`**: Contains CI/CD workflows for GitHub, which trigger actions like setup, linting, and testing when code is pushed to the repository.
- **`rdu-weather-history.csv`**: Weather data for the Durham region.

## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:nogibjj/yijia_ids706_miniProj6.git
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
- make test: Runs tests using pytest.

## SQL Query for Weather Data Aggregation
This SQL query aggregates the weather data for 2022 by calculating the average temperature, total precipitation, and average wind speed for each month. It joins this aggregated monthly data with the original daily weather records to provide detailed insights, combining both monthly and daily data. The results are sorted by average wind speed in descending order, showing the highest wind speeds first.

```sql
WITH monthly_aggregates AS (
    SELECT
        DATE_TRUNC('month', Date) AS month,
        AVG((Temperature_Minimum + Temperature_Maximum) / 2) AS avg_temperature,
        SUM(Precipitation) AS total_precipitation,
        AVG(Average_Wind_Speed) AS avg_wind_speed
    FROM
        rdu_weather
    WHERE
        YEAR(Date) = 2022
    GROUP BY
        DATE_TRUNC('month', Date)
)

SELECT 
    rw.Date, 
    rw.Temperature_Minimum, 
    rw.Temperature_Maximum, 
    ma.avg_temperature, 
    ma.total_precipitation, 
    ma.avg_wind_speed
FROM 
    rdu_weather rw
JOIN 
    monthly_aggregates ma 
ON 
    DATE_TRUNC('month', rw.Date) = ma.month
ORDER BY 
    ma.avg_wind_speed DESC
```

### Query Explanation
- Aggregation:
    - Grouping by Month: The query first groups weather data by month using DATE_TRUNC('month', Date) to group the records by month in 2022.
    - Average Temperature: It calculates the monthly average temperature by averaging the daily minimum and maximum temperatures using AVG((Temperature_Minimum + Temperature_Maximum) / 2).
    - Total Precipitation: The query sums up the daily precipitation for each month using SUM(Precipitation).
    - Average Wind Speed: The monthly average wind speed is calculated by averaging the daily wind speeds using AVG(Average_Wind_Speed).
- Join:
    - The query performs a JOIN between the original rdu_weather table and the monthly_aggregates table created in the WITH clause. The join is based on matching the month from the original weather data (DATE_TRUNC('month', rw.Date)) with the aggregated monthly data (ma.month).
- Sorting:
    - The final results are sorted by the average wind speed in descending order, ensuring that the months with the highest wind speeds appear first.

## CI/CD Setup
- Location: .github/workflows/
- Description: Contains GitHub Actions workflows for CI/CD, which automatically run setup, linting, testing.

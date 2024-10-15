from dotenv import load_dotenv
from databricks import sql
import os

# SQL query for aggregating and sorting the weather data
complex_query = """
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
"""

def query():
    """Query the database and fetch the top 5 weather data aggregations."""
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(complex_query)
            result = cursor.fetchall()

            for row in result:
                print(row)

            cursor.close()
            connection.close()
    return "query sucessful"

if __name__ == "__main__":
    query()

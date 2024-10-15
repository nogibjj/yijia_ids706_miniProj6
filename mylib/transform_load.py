import csv
import os
from dotenv import load_dotenv
from databricks import sql


# load the csv file and insert into a new databricks database
def load(dataset="./data/rdu-weather-history.csv"):
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)
    # print(*payload)
    load_dotenv()
    
    # Connect to Databricks
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            # CREATE TABLE 
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS rdu_weather (
                    Date STRING,
                    Temperature_Minimum INT,
                    Temperature_Maximum INT,
                    Precipitation DOUBLE,
                    Snowfall DOUBLE,
                    Snow_Depth DOUBLE,
                    Average_Wind_Speed DOUBLE
                );"""
            )

            # truncate the table to delete all existing rows
            # cursor.execute("TRUNCATE TABLE rdu_weather")
            # print("Table truncated, all rows deleted.")
            
            # Insert data into the table if it is not already loaded
            cursor.execute("SELECT COUNT(*) FROM rdu_weather")
            result = cursor.fetchone()
            row_count = result[0]
            print(f"Number of rows in the table: {row_count}")

            if not result[0]:  # If no data exists in the table
                    print("Inserting data into table...")
                    insert_query = "INSERT INTO rdu_weather (Date, Temperature_Minimum, Temperature_Maximum, Precipitation, Snowfall, Snow_Depth, Average_Wind_Speed) VALUES"
                    values = []

                    for row in payload:
                        date, temp_min, temp_max, precipitation, snowfall, snow_depth, wind_speed = row

                        # Replace empty values with None (which will map to NULL in SQL)
                        wind_speed = wind_speed if wind_speed else 'NULL'
                        
                        # Convert the values to appropriate type
                        values.append(
                            f"('{date}', {int(temp_min)}, {int(temp_max)}, {float(precipitation)}, {float(snowfall)}, {float(snow_depth)}, {float(wind_speed) if wind_speed != 'NULL' else wind_speed})"
                        )

                    # Join all value tuples into the insert query
                    string_sql = insert_query + ",\n".join(values) + ";"
                    print(string_sql)

                    # Execute the bulk insert query
                    cursor.execute(string_sql)
            cursor.close()
            connection.close()
    
    return "db loaded or already loaded"


if __name__ == "__main__":
    load()

"""
ETL-CRUD script
"""

import os
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD


def main():
    # Define file paths and database name
    dataset_url = "https://raw.githubusercontent.com/nogibjj/yijia_ids706_miniProj3/refs/heads/main/rdu-weather-history.csv"
    csv_file_path = "data/rdu-weather-history.csv"
    database_path = "WeatherDB.db"

    # Ensure the 'data' directory exists
    if not os.path.exists("data"):
        os.makedirs("data")

    # Step 1: Extract
    print("Extracting data from the source URL...")
    extract(url=dataset_url, file_path=csv_file_path)

    # Step 2: Transform and Load
    print(f"Transforming data and loading into {database_path}...")
    load(dataset=csv_file_path)

    # Step 3: CRUD Operations

    # Create
    print("Creating a new record...")
    create_CRUD(
        database_path, ("2024-10-03", 59.0, 77.5, 0.0, 0.0, 0.0, 12.0)
    )  # Example record for testing

    # Read
    print("Reading records from the database...")
    read_results = read_CRUD(database_path, "2024-10-03")
    print(f"Read results: {read_results}")

    # Update
    print("Updating a record in the database...")
    update_CRUD(database_path, "2024-10-03", (62.5, 80.0, 0.1, 0.0, 0.0, 15.0))

    # Read after update
    print("Reading records after update...")
    read_results_after_update = read_CRUD(database_path, "2024-10-03")
    print(f"Read after update: {read_results_after_update}")

    # Delete
    print("Deleting the record...")
    delete_CRUD(database_path, "2024-10-03")

    # Read after delete
    print("Reading records after deletion...")
    read_results_after_delete = read_CRUD(database_path, "2024-10-03")
    print(f"Read after delete: {read_results_after_delete}")


if __name__ == "__main__":
    main()

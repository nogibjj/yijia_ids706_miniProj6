import sqlite3
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD


# Test extracting
def test_extract():
    result = extract(
        url="https://raw.githubusercontent.com/nogibjj/yijia_ids706_miniProj3/refs/heads/main/rdu-weather-history.csv",
        file_path="rdu-weather-history.csv",
    )
    assert result is not None, "Extraction failed: No file downloaded."
    print("Extract test passed!")


# Test loading
def test_load_database():
    """Test loading the CSV into the SQLite3 database"""
    db_file = load("rdu-weather-history.csv")

    # Verify that the database file is created and contains data
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM WeatherDB")
    count = cursor.fetchone()[0]
    conn.close()

    assert count > 0, "Load test failed: No data found in the database."
    print("Load test passed!")


# Test create
def test_create_CRUD():
    """Test inserting a new record into the WeatherDB"""
    new_record = ("2024-10-04", 60.0, 85.0, 0.2, 0.0, 0.0, 12.5)
    create_CRUD("WeatherDB.db", new_record)

    # Verify
    conn = sqlite3.connect("WeatherDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM WeatherDB WHERE Date = ?", ("2024-10-04",))
    result = cursor.fetchone()
    conn.close()

    assert result == new_record, "Create test failed: Record does not match."
    print("Create test passed!")


# Test read
def test_read_CRUD():
    """Test reading records from the WeatherDB"""
    result = read_CRUD("WeatherDB.db", "2022-01-08")

    assert len(result) > 0, "Read test failed: No data found."
    print("Read test passed!")


# Test update
def test_update_CRUD():
    """Test updating an existing record in the WeatherDB"""
    updated_data = (65.0, 90.0, 0.1, 0.0, 0.0, 10.0)
    update_CRUD("WeatherDB.db", "2022-01-17", updated_data)

    # Verify
    conn = sqlite3.connect("WeatherDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM WeatherDB WHERE Date = ?", ("2022-01-17",))
    result = cursor.fetchone()
    conn.close()

    assert result[1:] == updated_data, "Update test failed: Data mismatch."
    print("Update test passed!")


# Test delete
def test_delete_CRUD():
    """Test deleting a record from the WeatherDB"""
    delete_CRUD("WeatherDB.db", "2022-01-26")

    # Verify
    conn = sqlite3.connect("WeatherDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM WeatherDB WHERE Date = ?", ("2022-01-26",))
    result = cursor.fetchone()
    conn.close()

    assert result is None, "Delete test failed: Record still exists."
    print("Delete test passed!")


if __name__ == "__main__":
    test_extract()
    test_load_database()
    test_create_CRUD()
    test_read_CRUD()
    test_update_CRUD()
    test_delete_CRUD()

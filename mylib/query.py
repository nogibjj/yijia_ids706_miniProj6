import sqlite3


LOG_FILE = "operations_log.md"

# Log each operation 
def log_operation(query, detail="", params=None):
    formatted_query = query
    if params:
        # Replace placeholders (?) with actual parameters in the query for logging purposes
        formatted_query = query.replace("?", "{}").format(*params)
    
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"```sql\n{formatted_query}\n")
        log_file.write(f"-- {detail}\n```\n\n")


# CREATE operation - Insert data into the database
def create_CRUD(database, data):
    """Insert data into the WeatherDB table"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = """
    INSERT INTO WeatherDB (Date, Temperature_Minimum, Temperature_Maximum, Precipitation, Snowfall, Snow_Depth, Average_Wind_Speed)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, data)
    
    conn.commit()

    log_operation(query, f"Inserted data for Date {data[0]}", data)

    conn.close()


# READ operation - Retrieve data for a specific date from the database
def read_CRUD(database, specific_date):
    """Query data from the WeatherDB table for a specific date"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = """
    SELECT * FROM WeatherDB WHERE Date = ?
    """
    cursor.execute(query, (specific_date,))
    results = cursor.fetchall()

    conn.close()

    log_operation(query, f"Read records for Date: {specific_date}", (specific_date,))

    return results


# UPDATE operation - Update data in the database
def update_CRUD(database, date, new_data):
    """Update a record in the WeatherDB table based on the Date"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = """
    UPDATE WeatherDB 
    SET Temperature_Minimum=?, Temperature_Maximum=?, Precipitation=?, Snowfall=?, Snow_Depth=?, Average_Wind_Speed=? 
    WHERE Date=?
    """
    cursor.execute(query, (*new_data, date))

    conn.commit()

    log_operation(query, f"Updated data for Date {date}", (*new_data, date))

    conn.close()


# DELETE operation - Delete data from the database
def delete_CRUD(database, date):
    """Delete a record from the WeatherDB table based on the Date"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    query = "DELETE FROM WeatherDB WHERE Date=?"
    cursor.execute(query, (date,))

    conn.commit()

    log_operation(query, f"Deleted record for Date {date}", (date,))

    conn.close()

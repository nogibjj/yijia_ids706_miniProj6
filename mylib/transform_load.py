"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/yijia_ids706_miniProj5/rdu-weather-history.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('WeatherDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS WeatherDB")
    c.execute("""
            CREATE TABLE WeatherDB (
                Date TEXT, 
                Temperature_Minimum REAL, 
                Temperature_Maximum REAL, 
                Precipitation REAL, 
                Snowfall REAL, 
                Snow_Depth REAL, 
                Average_Wind_Speed REAL
            )
        """)
    #insert
    c.executemany("""
            INSERT INTO WeatherDB 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, payload)
    conn.commit()
    conn.close()
    return "WeatherDB.db"


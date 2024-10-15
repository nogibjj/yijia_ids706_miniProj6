```sql

    INSERT INTO WeatherDB (Date, Temperature_Minimum, Temperature_Maximum, Precipitation, Snowfall, Snow_Depth, Average_Wind_Speed)
    VALUES (2024-10-04, 60.0, 85.0, 0.2, 0.0, 0.0, 12.5)
    
-- Inserted data for Date 2024-10-04
```

```sql

    SELECT * FROM WeatherDB WHERE Date = 2022-01-08
    
-- Read records for Date: 2022-01-08
```

```sql

    UPDATE WeatherDB 
    SET Temperature_Minimum=65.0, Temperature_Maximum=90.0, Precipitation=0.1, Snowfall=0.0, Snow_Depth=0.0, Average_Wind_Speed=10.0 
    WHERE Date=2022-01-17
    
-- Updated data for Date 2022-01-17
```

```sql
DELETE FROM WeatherDB WHERE Date=2022-01-26
-- Deleted record for Date 2022-01-26
```

```sql

    INSERT INTO WeatherDB (Date, Temperature_Minimum, Temperature_Maximum, Precipitation, Snowfall, Snow_Depth, Average_Wind_Speed)
    VALUES (2024-10-03, 59.0, 77.5, 0.0, 0.0, 0.0, 12.0)
    
-- Inserted data for Date 2024-10-03
```

```sql

    SELECT * FROM WeatherDB WHERE Date = 2024-10-03
    
-- Read records for Date: 2024-10-03
```

```sql

    UPDATE WeatherDB 
    SET Temperature_Minimum=62.5, Temperature_Maximum=80.0, Precipitation=0.1, Snowfall=0.0, Snow_Depth=0.0, Average_Wind_Speed=15.0 
    WHERE Date=2024-10-03
    
-- Updated data for Date 2024-10-03
```

```sql

    SELECT * FROM WeatherDB WHERE Date = 2024-10-03
    
-- Read records for Date: 2024-10-03
```

```sql
DELETE FROM WeatherDB WHERE Date=2024-10-03
-- Deleted record for Date 2024-10-03
```

```sql

    SELECT * FROM WeatherDB WHERE Date = 2024-10-03
    
-- Read records for Date: 2024-10-03
```


from fastapi import HTTPException
import pandas as pd
import json

def filter_csv(filename: str, targetfile: str, filters: list[dict]):
    #print(f"CSV_FILE_PATH: {CSV_FILE_PATH}, targetfile: {targetfile}, column: {column}, value: {value}")
    try:
        # Read CSV file into DataFrame
        df = pd.read_csv(filename)
        
        # Apply filters
        for f in filters:
            column = f.get("column")
            value = f.get("value")
            df = df[df[column] == value]
        
        # Convert to JSON and save to target file
        df.to_json(targetfile, orient="records", indent=4)
        
        return f"Filtering completed, output: {targetfile}"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

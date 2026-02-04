
import os
import pandas as pd
from pathlib import Path



def check_column(file_path, column_name):
    """
    Read CSV or XLSX and validate column.
    
    Args:
        file_path: Path to CSV or XLSX file
        column_name: Column name to validate
    
    Returns:
        Column data if valid, None if invalid
    """
    try:
        # Detect file type
        file_ext = Path(file_path).suffix.lower()
        
        if file_ext == '.csv':
            df = pd.read_csv(file_path)
            print(f"CSV file loaded")
        elif file_ext in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path)
            print(f"Excel file loaded")
        else:
            print(f"Unsupported file type: {file_ext}")
            return None
        
        if column_name in df.columns:
            print(f"Column '{column_name}' found")
            return df[column_name]
        else:
            print(f"Column '{column_name}' not found")
            print(f"Available columns: {df.columns.tolist()}")
            return None
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Read the Excel file
os.chdir('Stock-Prices-Analysis') # Change to your subfolder
excel_file = "netflix.csv"
column_name = "Close"

# Get Column data
column_data = check_column(excel_file, column_name)
print(column_data.head())


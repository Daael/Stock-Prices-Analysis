
import os
import pandas as pd
from pathlib import Path


def read_file(file_path, column_name):
    """
    Read CSV or XLSX and validate column.
    
    Args:
        file_path: Path to CSV or XLSX file
        column_name: Column name to validate
    
    Returns:
        True if column found and numeric, False otherwise
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
            return False
        
        if column_name in df.columns:
            column_data = df[column_name]
            # Check if column is fully numeric
            if pd.api.types.is_numeric_dtype(column_data):
                print(f"Column '{column_name}' is fully numeric")
                return True
            else:
                print(f"Column '{column_name}' is not numeric")
                return False
        else:
            print(f"Column '{column_name}' not found")
            print(f"Available columns: {df.columns.tolist()}")
            return False
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"Error reading file: {e}")
        return False


# Read the Excel file
os.chdir('Stock-Prices-Analysis') # Change to your subfolder
excel_file = "netflix.csv"
column_name = "Close"

# Get Column data
column_data = read_file(excel_file, column_name)
print(column_data)


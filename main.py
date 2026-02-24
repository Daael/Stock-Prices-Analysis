import script
import os

def main():
    print("Starting Stock Prices Analysis...")
    excel_file = "netflix.csv"
    column_name = "Closee"

    # Read the Excel file
    df = script.read_file(excel_file)

    # Check Column
    if script.check_column(df, column_name):
        column_data = df[column_name]
    else:
        print("Column validation failed. Exiting.")
        return



if __name__ == '__main__':
    os.chdir('Stock-Prices-Analysis') # Change to your subfolder
    main()
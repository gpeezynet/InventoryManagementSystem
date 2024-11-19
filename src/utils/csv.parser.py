import csv

def parse_csv(file_path):
    """Parse a CSV file and return a list of dictionaries representing each row."""
    parsed_data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                parsed_data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while parsing the CSV: {e}")
    
    return parsed_data

# Example usage
if __name__ == "__main__":
    file_path = 'example.csv'  # Replace with your actual CSV file path
    data = parse_csv(file_path)
    if data:
        for entry in data:
            print(entry)
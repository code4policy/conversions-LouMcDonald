import csv
import json

# Input and output file paths
input_file = "input.csv"  # CSV input file
output_file = "output.json"  # JSON output file

# Initialize an empty list to store the converted data
data = []

# Open the CSV file for reading
try:
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)  # Automatically reads the header row as keys

        # Loop through each row in the CSV
        for row in reader:
            # Append formatted data to the list
            data.append({
                "title": row["title"],
                "subtitle": row["subtitle"],
                "ranges": [
                    float(row["range_min"]),
                    float(row["range_mid"]),
                    float(row["range_max"])
                ],
                "measures": [
                    float(row["measure_min"]),
                    float(row["measure_max"])
                ],
                "markers": [
                    float(row["markers"])
                ]
            })
except KeyError as e:
    print(f"Missing column in CSV: {e}")
    exit(1)
except FileNotFoundError:
    print(f"Input file '{input_file}' not found.")
    exit(1)
except ValueError as e:
    print(f"Error converting data: {e}")
    exit(1)

# Write the JSON data to a file
try:
    with open(output_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
        print(f"Conversion complete! JSON data saved to '{output_file}'.")
except Exception as e:
    print(f"Error writing to output file: {e}")
    exit(1)

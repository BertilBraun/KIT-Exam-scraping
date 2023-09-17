import csv


def filter(title, ects) -> bool:
    return 'seminar' not in title.lower() and 'praktikum' not in title.lower() and float(ects) <= 6.0


def filter_csv(input_file, output_file):
    # Initialize an empty list to store the filtered entries
    filtered_data = []

    # Open the input CSV file for reading
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        # Loop through each row in the CSV
        for row in reader:
            if filter(row['Title'], row['ECTS']):
                filtered_data.append(row)

    # Write the filtered data to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['Title', 'ECTS', 'Link']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in filtered_data:
            writer.writerow(item)

    print(f"Filtered data has been saved to '{output_file}'.")


if __name__ == '__main__':
    # Specify the input and output file names
    input_file = 'extracted_data.csv'
    output_file = 'filtered_data.csv'

    # Call the filter_csv function
    filter_csv(input_file, output_file)

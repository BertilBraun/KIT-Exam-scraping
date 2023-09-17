import csv
from datetime import datetime


def read_csv(input_file):
    rows = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            rows.append(row)
    return rows


def write_csv(output_file, rows):
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        fieldnames = ['Module', 'Title', 'ECTS', 'Exam Type',
                      'Exam Date', 'Link to Modul', 'Link to Exam']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def parse_date(date_str):
    if date_str == "N/A":
        return None
    return datetime.strptime(date_str, "%d.%m.%Y")


def sort_rows(rows):
    # Sort by 'Exam Type', and then by parsed 'Exam Date'
    return sorted(rows, key=lambda x: (x['Exam Type'], parse_date(x.get('Exam Date', 'N/A'))))


if __name__ == '__main__':
    rows = read_csv('exam_info.csv')
    sorted_rows = sort_rows(rows)
    write_csv('sorted_exam_info.csv', sorted_rows)

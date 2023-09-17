import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


def get_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def process_row(row, writer):
    module, title = row['Title'].split(' – ', maxsplit=1)
    ects = row['ECTS']
    original_link = row['Link']

    # Adjust link for scraping
    scrape_link = original_link.replace('../../', 'https://campus.kit.edu/sp/')

    # Make request to the page
    soup = get_html(scrape_link)

    # Extract Exam Type
    table = soup.find('table', {'id': 'EXAMLIST'})
    try:
        exam_type = table.find_all('tr')[1].find_all('td')[-1].text
        exam_page_link = table.find_all(
            'tr')[1].find_all('td')[-1].find('a')['href']
    except:
        exam_type = "Not Found"
        exam_page_link = "Not Found"

    # If Exam Type is written, fetch Exam Date
    exam_date = "N/A"
    if "Schriftliche Prüfung" in exam_type and exam_page_link != "Not Found":
        # Adjust link for scraping exam info
        scrape_exam_link = exam_page_link.replace(
            '../../', 'https://campus.kit.edu/sp/')

        exam_soup = get_html(scrape_exam_link)

        exam_date_field = exam_soup.find(
            'div', {'id': 'RWEV_REGISTRATION-field'})
        if exam_date_field:
            exam_date = exam_date_field.find(
                'div', {'class': 'element'}).text.split('-')[1].strip().split(' ')[0]

    # Write to a new CSV
    writer.writerow({
        'Module': module,
        'Title': title,
        'ECTS': ects,
        'Exam Type': exam_type,
        'Exam Date': exam_date,
        'Link to Modul': original_link,
        'Link to Exam': exam_page_link
    })


def extract_exam_info(input_csv, output_csv):
    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['Module', 'Title', 'ECTS', 'Exam Type',
                      'Exam Date', 'Link to Modul', 'Link to Exam']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        line_count = len(open(input_csv).readlines()) - 1
        # Read existing CSV
        with open(input_csv, 'r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            rows = list(reader)

            with ThreadPoolExecutor() as executor:
                list(tqdm(executor.map(lambda row: process_row(row, writer), rows),
                     desc="Extracting Exam Info", unit="rows", total=line_count, dynamic_ncols=True))


if __name__ == '__main__':
    extract_exam_info('filtered_data.csv', 'exam_info.csv')

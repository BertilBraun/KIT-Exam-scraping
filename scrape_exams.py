from bs4 import BeautifulSoup
import csv
import pyperclip
import time


def main():
    print("Please copy the HTML content to your clipboard and press Enter to continue.")
    input()  # Wait for the user to press Enter

    # Read HTML content from the clipboard
    html_content = pyperclip.paste()

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table with class 'listview'
    table = soup.find('table', {'class': 'listview'})

    # Find all rows in the table
    rows = table.find_all('tr', {'class': 'electionrow'})

    # Initialize an empty list to hold the extracted data
    data = []

    # Loop through each row
    for row in rows:
        # Find the title cell
        title_cell = row.find('td').find_next_sibling('td')
        # Extract title and link
        title = title_cell.text.strip().replace(' Details anzeigen', '')
        link = title_cell.find('a')['href']

        # Find the number cell
        number_cell = title_cell.find_next_sibling('td', {'class': 'number'})
        number = number_cell.text.strip().replace(',', '.')

        # Append the data to the list
        data.append({'Title': title, 'ECTS': number, 'Link': link})

    # Write the extracted data to a CSV file
    with open('extracted_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'ECTS', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)

    print("Data has been saved to 'extracted_data.csv'.")


if __name__ == '__main__':
    main()

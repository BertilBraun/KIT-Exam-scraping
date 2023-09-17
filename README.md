# KIT Exam Scraping

## 🌟 Description and Reason for Existence

This project is dedicated to scraping and processing exam schedules at the Karlsruhe Institute of Technology (KIT). The aim is to streamline and automate the tedious task of manually searching for and gathering exam details. With a set of Python scripts, this tool allows you to effortlessly scrape, filter, and retrieve specific exam information.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Files](#files)

---

## Installation

Clone the repository to your local machine.

```bash
git clone https://github.com/your_username/KIT-Exam-Scraping.git
```

Install the required Python packages.

```bash
pip install -r requirements.txt
```

---

## Usage

The project consists of three main Python scripts:

1. `scrape_exams.py`
2. `filter.py`
3. `exam_info.py`

### Steps to Use

#### Step 1: Scrape Exams

First, run the `scrape_exams.py` script.

```bash
python scrape_exams.py
```

After starting the script, go to `campus.studium.kit.edu/exams/registration.php` and copy the HTML content of the page that you want to process.

Return to the script and press `Enter` to continue.

#### Step 2: Filtering

Open the `filter.py` file and adjust the filtering options as per your requirement. Save the file and then run the script.

```bash
python filter.py
```

#### Step 3: Query Exam Information

Finally, run the `exam_info.py` script to get the detailed exam information.

```bash
python exam_info.py
```

The final output will be saved in a file named `exam_info.csv`.

---

## Additional Utility: Sort Your Exams

After generating the `exam_info.csv`, you may want to sort the data for easier consumption. You can use the `order.py` script for this.

### Steps to Sort

#### Step 4: Sort Exam Information

Run the `order.py` script to sort the exams first by 'Exam Type' and then by 'Exam Date'.

```bash
python order.py
```

The sorted output will be saved in a file named `sorted_exam_info.csv`.

---

## Files

1. `scrape_exams.py` - Scrapes the initial exam data.
2. `filter.py` - Filters the scraped exams based on specified criteria.
3. `exam_info.py` - Fetches detailed exam information like type, date, etc.
4. `order.py` - Sorts the exam information based on 'Exam Type' and 'Exam Date'.
5. `requirements.txt` - Contains all the required Python packages.

---

Feel free to contribute or report any issues.

- [ ] Always extract the exam registration date for exams
- [ ] Parse the initial exam data less crudely from the HTML
- [ ] Simpler interface which does all in one go and allows neater filtering and sorting
- [ ] Add why there was no Exam information found

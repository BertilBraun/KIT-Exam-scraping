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

## Files

1. `scrape_exams.py` - Scrapes the initial exam data.
2. `filter.py` - Filters the scraped exams based on specified criteria.
3. `exam_info.py` - Fetches detailed exam information like type, date, etc.
4. `requirements.txt` - Contains all the required Python packages.

---

Feel free to contribute or report any issues.

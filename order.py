import pandas as pd


def sort_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # Convert 'Exam Date' column to datetime format for proper sorting
    df['Exam Date'] = pd.to_datetime(df['Exam Date'], errors='coerce')

    # Sort by 'Exam Type' and then 'Exam Date'
    df.sort_values(['Exam Type', 'Exam Date'], inplace=True)

    # Save the sorted DataFrame back to CSV
    df.to_csv(output_csv, index=False, encoding='utf-8')


if __name__ == '__main__':
    sort_csv('exam_info.csv', 'sorted_exam_info.csv')

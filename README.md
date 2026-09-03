# Sacramento Historical Weather Analysis

This Python project retrieves seven days of hourly historical temperature data for Sacramento, California, using the Open-Meteo Historical Weather API.

The program parses the API response, calculates summary temperature statistics, creates a scatter plot, and generates a two-page PDF report.

## Features

- Retrieves hourly historical temperature data
- Calculates the highest, lowest, and average temperatures
- Creates a scatter plot using Matplotlib
- Generates a PDF report using ReportLab

## Technologies

- Python
- Requests
- Matplotlib
- ReportLab
- Open-Meteo Historical Weather API

## How to Run

1. Install the required libraries:

   ```bash
   python -m pip install requests matplotlib reportlab
2. Run the program:

    ```bash
    python FINAL_PROJECT.py
    
Output

Running the program creates:

Final scatterplot.png
final.pdf

Data Period

The current version analyzes hourly temperatures in Sacramento from August 27, 2026, through September 2, 2026.

Because the revised project uses Open-Meteo, it does not require an API key or `.env` file.
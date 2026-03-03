📊 Excel-to-Dashboard Tool
This is a lightweight Python web application that transforms messy Excel or CSV files into interactive, clean bar charts.

🚀 How to Run This App
Install Python: Ensure you have Python 3.9+ installed on your Mac.

Install Dependencies: Open your terminal and run:

Bash
python3 -m pip install streamlit pandas openpyxl altair

Launch the App: Run this command in the terminal:

Bash
python3 -m streamlit run uploadxlsx.py

Access in Browser: Go to http://localhost:8501 in Google Chrome.

🛠 Features
Auto-Cleaning: Strips hidden spaces from column headers.

Header Selection: Adjust the header parameter to skip "Title" rows in Excel.

Type Safety: Automatically converts text-based numbers into math-ready decimals.

Dynamic Visualization: Pick your X and Y axes and change chart colors on the fly.

Data Export: Cleaned data can be downloaded as a fresh CSV.

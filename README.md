<H1> 📊 Excel-to-Dashboard Tool</H1> 
This is a lightweight Python web application that transforms messy Excel or CSV files into interactive, clean bar charts.

<H2> 🚀 How to Run This App</H2> 
<ol>
  <li><b>Install Python:</b> Ensure you have Python 3.9+ installed on your Mac.</li>
  <li><b>Install Dependencies:</b>Open your terminal and run:</li>
  
  <code>Bash
python3 -m pip install streamlit pandas openpyxl altair
</code>

  <li><b>Launch the App:</b> Run this command in the terminal:</li>
  
<code>Bash
python3 -m streamlit run uploadxlsx.py
</code>

 <li><b>Access in Browser:</b> Go to http://localhost:8501 in Google Chrome.</li>
</ol>

<H2> 🛠 Features</H2> 
<ul>
<li><b>Auto-Cleaning:</b> Strips hidden spaces from column headers.</li>

<li><b> Header Selection: </b> Adjust the header parameter to skip "Title" rows in Excel.</li>

<li><b>Type Safety: </b> Automatically converts text-based numbers into math-ready decimals.</li>

<li><b>Dynamic Visualization: </b> Pick your X and Y axes and change chart colors on the fly.</li>

<li><b>Data Export: </b> Cleaned data can be downloaded as a fresh CSV.</li>
</ul>

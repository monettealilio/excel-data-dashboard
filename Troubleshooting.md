<i>Keep this handy for when things go "wrong."</i>

<ol>
<li><b>The "White Screen of Death"</b></li>
<b>The Cause:</b> Usually a Syntax Error (a missing colon <code>:</code>, a missing quote <code>"</code>, or an extra parenthesis <code>)</code>).

<b>The Fix:</b> Look at your <b>Terminal</b>. It will tell you the exact Line Number where the mistake is. Check the line above and below that number for typos.

<li><code>ModuleNotFoundError: No module named 'openpyxl'</code></li>
<b>The Cause:</b> You are trying to upload an <code> .xlsx </code> file, but the library that reads Excel isn't installed in the specific version of Python you are running.

<b>The Fix:</b> Run this exact command in the terminal:
<code>python3 -m pip install openpyxl</code>
<i>Then, stop the app (Ctrl+C) and restart it.</i>

<li><code>ValueError: "0" is not one of the valid encoding data types</code></li>
<b>The Cause:</b> Your Y-axis (the numbers) has a column name that is a number (like "2024") or a blank space. Altair (the chart maker) needs column names to be <b>Text</b>.

<b>The Fix:</b> Ensure your "Cleaning" line is active: <br>
<code>df.columns = [str(c).strip() for c in df.columns]</code>

<li><code>NameError: name 'bar_color' is not defined</code></li>
<b>The Cause: Order of Operations.</b> You used the variable <code>bar_color</code> inside your chart code <i>before</i> you created the <code>st.sidebar.color_picker</code>.

<b>The Fix:</b> Move the color picker line to the very top of your script, right after the title.

<li><b>"Total" bar is ruining the chart scale</b></li>
<b>The Cause:</b> Your Excel file has a "Total" row at the bottom which is 10x bigger than the other bars.

<b>The Fix:</b> Use the "Not" filter (<code>~</code>) to remove it:
<code>df = df[~df[x_axis].astype(str).str.contains('Total', case=False)]</code>
</ol>

<H3>💡 Final Tips for Your Journey</H3>
<ul>
<li><b>Version Control:</b> If your code is working perfectly, <b>Duplicate the file</b> (e.g., <code>app_v1_backup.py</code>) before you try to add a new complex feature. That way, if you "break" it, you can always go back.</li>

<li><b>The "Key" to Success:</b> If a widget (like a button) isn't responding, give it a unique ID: <code>st.button("Click Me", key="unique_button_1")</code>.</li>

<li><b>Chrome is your Friend:</b> If the app feels "laggy," refresh Chrome (Cmd + R) and check the "Running" icon in the top right of the Streamlit app.</li>
</ul>

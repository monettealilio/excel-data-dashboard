# STEP 1: Imports (The Tools)
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Data Pro v1.0",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# STEP 2: The Title
st.title("📁 Excel Dashboard")
# Create a color picker in the sidebar
bar_color = st.sidebar.color_picker("Pick a Bar Color", "#0077ff")


# STEP 3: Define the variable (The "Question")
# This creates the box. Python now knows what 'uploaded_file' is.
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

# STEP 4: The Logic (The "Answer")
# Now that 'uploaded_file' exists, we can check if it's empty or not.

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, header=2) if uploaded_file.name.endswith('.xlsx') else pd.read_csv(uploaded_file, header=2)
    
    # 1. Clean the column names (the fix from before)
    df.columns = [str(c).strip() for c in df.columns]

    # 2. Let the user pick axes
    columns = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis (Labels):", columns, index=0)
    y_axis = st.selectbox("Select Y-axis (Numbers):", columns, index=1)

    # 3. ✨ THE MAGIC FIX: Force the Y-axis to be Numeric ✨
    # This converts "1,000" or "$50" into actual numbers (1000 or 50)
    # 'coerce' means: "If you find something that isn't a number, turn it into a blank (NaN)"
    df[y_axis] = pd.to_numeric(df[y_axis], errors='coerce')
    
    # 4. Remove any rows that ended up with a blank number after the conversion
    df = df.dropna(subset=[y_axis])

    df = df.round(2)
    st.dataframe(df)

    
    # 1. Clean the column names
    df.columns = [str(c).strip() for c in df.columns]

    # ✨ THE "TOTAL" REMOVER ✨
    # This keeps only the rows where the X-axis value is NOT "Total"
    # We use .str.contains to be safe in case it says "TOTAL" or "Total Sales"
    df = df[~df[x_axis].astype(str).str.contains('Total', case=False, na=False)]
    df = df.dropna(how='all') # Deletes rows that are 100% empty


    # 5. Build the Chart

    chart = alt.Chart(df).mark_bar(color=bar_color).encode(
    x=alt.X(x_axis, title=x_axis),
    y=alt.Y(y_axis, title=y_axis, axis=alt.Axis(format=".2f")),
    tooltip=[x_axis, alt.Tooltip(y_axis, format=".2f")]
    ).interactive()


    # 6. DISPLAY the chart you just built
    st.altair_chart(chart, use_container_width=True)

    st.divider()
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Cleaned CSV", csv, "data.csv", "text/csv")
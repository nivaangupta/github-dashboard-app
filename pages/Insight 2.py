import streamlit as st
import pandas as pd


# Reading Data
df = pd.read_csv('data/final_data.csv')

# Header
st.set_page_config(page_title='Anomaly Detection',
                   page_icon=':bar_chart:', layout='wide')

# Sidebar
st.sidebar.markdown('''
    ---
    December 2023\n
    Created by Nivaan Gupta\n 
    Data credits: https://www.kaggle.com/datasets/nikhil25803/github-dataset/code
''')

# Body
st.title(":bar_chart: Github Repositories")
st.subheader("Anomaly detections")

st.markdown('''
---
''')
st.markdown("""
```
# Checking the Dashboard's scatterplot for correlation, and diving deep in the anomalies
```
""")
st.image('assets/anomaly.png')

st.markdown('''
---
''')

st.markdown("""
```
# Diving in Stars-Watchers correlation
# We find through the plot that there are Unpopular Repositories with a lot of watchers
df[(df['stars_count'] < 29)].sort_values(by='watchers', ascending=False).head(5)
```
""")
st.dataframe(df[(df['stars_count'] < 29)].sort_values(by='watchers', ascending=False).head(5))

st.markdown("""
```
# Now that we have the Top 5 Anomalies, we can take a look at these repositories to find some pattern
```
""")
a1, a2 = st.columns(2)
a1.image('assets/m1.png')
a2.image('assets/m2.png')
b1, b2, b3 = st.columns(3)
b1.image('assets/m3.png')
b2.image('assets/m4.png')
b3.image('assets/m5.png')

st.markdown("""
```
# We notice that each of these projects belong to Microsoft with customer support and maintenance documents
```
""")

st.markdown('''
---
''')



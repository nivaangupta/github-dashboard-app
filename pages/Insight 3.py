import streamlit as st
import pandas as pd


# Reading Data
df = pd.read_csv('data/final_data.csv')

# Header
st.set_page_config(page_title='Covid Impact',
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
st.subheader("Diving deep to understand the impact of the Pandemic on repository data")

st.markdown('''
---
''')
st.markdown("""
```
# Diving into the dashboard to notice the trend of project creation by the year
```
""")
st.image('assets/COVID.png')

st.markdown("""
```
# We can see an unusual sudden spike in the number of projects during 2020, the year of pandemic
```
""")
st.markdown("""
```
# To further investigate the reason for this spike we dive deeper into the popular projects created during this time
df['Year'] = pd.to_datetime(df['created_at']).dropna().dt.year.astype(int)
df.loc[df['Year'] == 2020].sort_values(by='stars_count', ascending=False).head(5)
```
""")
df['Year'] = pd.to_datetime(df['created_at']).dropna().dt.year.astype(int)
st.dataframe(df.loc[df['Year'] == 2020].sort_values(by='stars_count', ascending=False).head(5))

st.markdown('''
---
''')
st.markdown("""
```
# We first check the TOP 3 to look for a pattern
```
""")
a1, a2, a3 = st.columns(3)
a1.image('assets/learn1.png')
a2.image('assets/learn2.png')
a3.image('assets/learn3.png')
st.markdown("""
```
# We notice that each of these repositories are modules to learn programming language
# The same can be largely a factor of 2 things:
# 1. During lockdown people decided to learn a new skill and many levitated towards learning programming
# 2. Companies around the world started hiring more people to fill the productivity gap caused by remote work
#    This led to many people preparing for interviews that involved coding. 
```
""")
st.markdown('''
---
''')
st.markdown("""
```
# We then check the Top 5th Repository in the list
```
""")
st.image('assets/cov.png')
st.markdown("""
```
# Upon looking at the project we find that the project was made explicitly for COVID19
```
""")
st.markdown('''
---
''')
st.markdown("""
```
# It is important to note that the most popular projects were in "Learning" & "Covid Help" Category
# Both activities, The learning & Covid Help, being induced as a result of the Pandemic
```
""")
st.markdown("""
```
# With that said the sudden spike in activity can be justified by the following 2 reasons
# 1. The Pandemic induced the need for projects that focus on Covid-19 related tasks.
#    This created an entire new categories of projects that were being created during pandemic for pandemic
# 2. People picking up programming to learn and/or interview for coding jobs would lead to a fresh new 
#    population learning about programming and making projects either to practise coding or work on 
#    their portfolio. 
# A cumulative of both these reasons are a large factor of why there was a spike in activity during 2020
# as both these reasons are specific to 2020 & the pandemic.
```
""")

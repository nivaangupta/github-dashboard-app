import streamlit as st
import pandas as pd
# Below are required inputs for plotting the countplot graph
# import matplotlib.pyplot as plt
# import seaborn as sns


# Reading Data
df = pd.read_csv('data/final_data.csv')

# Header
st.set_page_config(page_title='Language Insights',
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
st.subheader("Diving deeper into programming languages")

st.markdown('''
---
''')
st.markdown("""
```
df.head(5)
```
""")
st.dataframe(df.head(5))

st.markdown("""
``` 
# Making a Language-specific DF to dive deeper
```
""")

st.markdown("""
```
language_df = df.groupby('primary_language').agg({'stars_count':'sum',
                                                  'forks_count':'sum',
                                                  'watchers':'sum',
                                                  'pull_requests':'sum',
                                                  'commit_count':'sum',
                                                  'name':'count'}).sort_values(by='name', ascending=False)
language_df.head(5)
```
""")
language_df = df.groupby('primary_language').agg({'stars_count':'sum',
                                                  'forks_count':'sum',
                                                  'watchers':'sum',
                                                  'pull_requests':'sum',
                                                  'commit_count':'sum',
                                                  'name':'count'}).sort_values(by='name', ascending=False)
st.dataframe(language_df.head(5))

st.markdown("""
``` 
# Comparing Python & JavaScript vs a project's creation year, as they are significantly more popularly used language
```
""")

st.markdown("""
```
a = df.loc[df['primary_language'].isin(['Python', 'JavaScript'])].reset_index(drop=True).dropna()
a['month_year'] = a['created_at'].apply(lambda x: pd.to_datetime(x).strftime('%Y')) # e.g. 2021
ax = sns.countplot(x=a['month_year'], hue= a['primary_language'], orient='v', order=sorted(a['month_year'].unique()))
ax.tick_params(axis='x', rotation=45)
ax.set_xlabel('date')
plt.show()
```
""")

# THE CODE FOR ACTUAL GRAPH IS AS FOLLOWS:
# a = df.loc[df['primary_language'].isin(['Python', 'JavaScript'])].reset_index(drop=True).dropna()
# a['month_year'] = a['created_at'].apply(lambda x: pd.to_datetime(x).strftime('%Y'))
# fig = plt.figure(figsize=(10, 6))
# ax = sns.countplot(x=a['month_year'], hue=a['primary_language'], orient='v', order=sorted(a['month_year'].unique()))
# ax.tick_params(axis='x', rotation=45)
# ax.set_xlabel('date')
# st.pyplot(fig)
# Using an Image as the graph isn't manipulated dynamically to save load on server

st.image('assets/countplot1.png')

st.markdown("""
``` 
# It is interesting to take note of the trend where JavaScript's popularity is on a decline whereas python's popularity is soring every year 
```
""")
st.markdown("""
``` 
# Further diving deep into why is this the case, we reference the dashboard to draw insights 
```
""")
a1, a2 = st.columns(2)
a1.image('assets/python.png')
a2.image('assets/js.png')
b1, b2 = st.columns(2)
b1.image('assets/python25.png')
b2.image('assets/js25.png')
c1, c2 = st.columns(2)
b1.image('assets/python75.png')
b2.image('assets/js75.png')
st.markdown("""
``` 
# From above, We can observe that Python requires significantly lesser number of commits per project
# JavaScript requires a higher number of edits for every project made with it as a primary language
# On top of that, even when the commits/project is less for python, the stars & watchers remain unaffected
```
""")
st.markdown("""
``` 
# From above we can say that it is "Easier" (less commits/project) to use Python than JavaScript
# Hence, we can state that Python's popularity & increase in use than JavaScript is a function of its ease
```
""")



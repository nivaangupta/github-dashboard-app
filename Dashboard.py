import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


# Defining Functions
def format_large_number(number):
    suffixes = ['', 'K', 'M', 'B', 'T', 'Q']
    suffix_index = 0
    while number >= 1000 and suffix_index < len(suffixes) - 1:
        suffix_index += 1
        number /= 1000.0
    return f'{number:.0f}{suffixes[suffix_index]}'


# Reading Data
df = pd.read_csv('data/final_data.csv')

# Header
st.set_page_config(page_title='Github Repository Dashboard',
                   page_icon=':bar_chart:', layout='wide')

# Sidebar
st.sidebar.header("Data Analytics")

# Create DF for Language Filter
language = st.sidebar.multiselect(
    "Filter Data by Primary Language", df['primary_language'].fillna('None').unique())
if not language:
    df2 = df.copy()
else:
    df2 = df[df["primary_language"].fillna('None').isin(language)]

# Create DF for Licence Filter
licence = st.sidebar.multiselect(
    "Filter Data by Licence used", df2['licence'].fillna('None').unique())
if not licence:
    df3 = df2.copy()
else:
    df3 = df2[df2["licence"].fillna('None').isin(licence)]

# Create DF for Popularity filter
popularity = st.sidebar.multiselect(
    "Filter Data by Repository's Popularity", df3['is_popular'].unique())
if not popularity:
    df4 = df3.copy()
else:
    df4 = df3[df3['is_popular'].isin(popularity)]

# Filtering entire dataset to make 1
filtered_df = df

if language:
    filtered_df = filtered_df[filtered_df["primary_language"].fillna('None').isin(language)]
if licence:
    filtered_df = filtered_df[filtered_df["licence"].fillna('None').isin(licence)]
if popularity:
    filtered_df = filtered_df[filtered_df['is_popular'].isin(popularity)]

# Copyright
st.sidebar.markdown('''
    ---
    December 2023\n
    Created by Nivaan Gupta\n 
    Data credits: https://www.kaggle.com/datasets/nikhil25803/github-dataset/code
''')

# Body Begins
# Row A
a1, a2, a3 = st.columns(3)
a1.title(":bar_chart: Github Repositories")

a21, a22 = a2.columns(2)
filtered_df['created_at'] = pd.to_datetime(filtered_df["created_at"].dropna())
# Get the first & the last date by getting the Min & Max date
startDate = pd.to_datetime(filtered_df["created_at"].dropna()).min()
endDate = pd.to_datetime(filtered_df["created_at"].dropna()).max()
with a21:
    date1 = pd.to_datetime(st.date_input("Set Start Date", startDate))
with a22:
    date2 = pd.to_datetime(st.date_input("Set End Date", endDate))
filtered_df = filtered_df[(filtered_df['created_at'] >= date1) & (filtered_df['created_at'] <= date2)]

pd.set_option('display.float_format', lambda x: '%.0f' % x)
a3.metric("Number of projects", f"{format_large_number(len(filtered_df))}", "")
st.markdown(
    '<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

# Row B
b1, b2, b3, b4 = st.columns(4)
pd.set_option('display.float_format', lambda x: '%.0f' % x)
b1.metric("Total Stars", f"{format_large_number(sum(filtered_df['stars_count']))}")
b2.metric("Total Commits", f"{format_large_number(int(sum(filtered_df['commit_count'].dropna())))}")
b3.metric("Total Forks", f"{format_large_number(sum(filtered_df['forks_count']))}")
b4.metric("Total Pulls", f"{format_large_number(sum(filtered_df['pull_requests']))}")

# Required Data for ahead
# Top Language DF
language_df = filtered_df.groupby('primary_language').agg({'stars_count': 'sum',
                                                           'forks_count': 'sum',
                                                           'watchers': 'sum',
                                                           'pull_requests': 'sum',
                                                           'commit_count': 'sum',
                                                           'name': 'count'}).sort_values(by='name', ascending=False)
# Top Licence DF
licence_df = filtered_df.groupby('licence').agg({'stars_count': 'sum',
                                                 'forks_count': 'sum',
                                                 'watchers': 'sum',
                                                 'pull_requests': 'sum',
                                                 'commit_count': 'sum',
                                                 'name': 'count'}).sort_values(by='name', ascending=False)

# Row C
c1, c2 = st.columns(2)

fig1 = plt.figure(figsize=(10, 8))
ax = sns.barplot(data=licence_df.head(5), x='name', y='licence', palette='viridis')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=10)
plt.ylabel('Licence')
plt.xlabel('Count of Projects')
plt.tight_layout()
annotations1 = [
    ("MIT Licence have significantly more \nprojects than other licences", (4, 4), (300, 300)),
]
for text, xy, xytext in annotations1:
    ax.annotate(text, xy=xy, xytext=xytext, textcoords='offset points', ha='center', fontsize=12, weight='bold')

c1.subheader('Top 5 Licence VS Repositories')
c1.write(fig1)

fig2 = plt.figure(figsize=(10, 8))
ax = sns.barplot(data=language_df.head(5), y='name', x='primary_language', palette='viridis')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=10)
plt.xlabel('Language')
plt.ylabel('Count of Projects')
plt.tight_layout()
annotations2 = [
    ("Python & JavaScript have significantly more \nprojects than other programming languages ", (3, 4), (-20, 400)),
]
for text, xy, xytext in annotations2:
    ax.annotate(text, xy=xy, xytext=xytext, textcoords='offset points', ha='center', fontsize=12, weight='bold')
c2.subheader('Top 5 Language VS Repositories')
c2.write(fig2)

# Row D
d1, d2 = st.columns(2)
# filtered_df['Year'] = pd.to_datetime(filtered_df['created_at']).dropna().dt.year.astype(int)
# yearly_counts = filtered_df['Year'].value_counts().sort_index()
#
# fig3 = plt.figure(figsize=(10, 6))
# plt.plot(yearly_counts.index, yearly_counts.values, marker='o', linestyle='-')
# plt.xlabel('Year of Creation')
# plt.ylabel('Count of Projects')
# plt.xticks(yearly_counts.index, rotation=45)
# plt.tight_layout()
# insights1 = {2018: "Project creation grows flat first time from 2018",
#             2020: "Significant all time rise during the pandemic for project creation"}
# for year, insight in insights1.items():
#     plt.text(year, yearly_counts[year], insight, ha='right', va='bottom', fontsize=12, weight='bold')
# d1.subheader("Projects created each year")
# d1.write(fig3)
filtered_df['Year'] = pd.to_datetime(filtered_df['created_at']).dropna().dt.year.astype(int)
yearly_counts = filtered_df['Year'].value_counts().sort_index()
commits_per_year = filtered_df.groupby('Year')['commit_count'].sum()
fig3, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(yearly_counts.index, yearly_counts.values, marker='o', linestyle='-', color='blue')
ax1.set_xlabel('Year of Creation')
ax1.set_ylabel('Count of Projects', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xticks(yearly_counts.index)
ax1.set_xticklabels(yearly_counts.index, rotation=45)

ax2 = ax1.twinx()
ax2.bar(commits_per_year.index, commits_per_year.values, alpha=0.5, color='orange')
ax2.set_ylabel('Commits', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, _: format(int(x), ',')))
d1.subheader("Projects & Commits Made each year")
d1.pyplot(fig3)

filtered_df['Year'] = pd.to_datetime(filtered_df['created_at']).dropna().dt.year.astype(int)
yearly_stars = filtered_df.groupby('Year')['stars_count'].sum()
yearly_watchers = filtered_df.groupby('Year')['watchers'].sum()

fig4, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(yearly_stars.index, yearly_stars.values, marker='o', linestyle='-', color='blue')
ax1.set_xlabel('Year of Creation')
ax1.set_ylabel('Total Stars Count', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xticks(yearly_stars.index)
ax1.set_xticklabels(yearly_stars.index, rotation=45)
plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, _: format(int(x), ',')))
ax2 = ax1.twinx()
ax2.bar(yearly_watchers.index, yearly_watchers.values, alpha=0.5, color='orange')
ax2.set_ylabel('Total Watchers', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

plt.gca().get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, _: format(int(x), ',')))
d2.subheader('Stars and Watchers Count per Year')
d2.pyplot(fig4)

# Row E
st.markdown('''
---
''')
st.subheader("The Data Analytics bar Doest change the scatter plot")
e1, e2 = st.columns(2)

correlation_starVSwatchers = filtered_df['stars_count'].corr(filtered_df['watchers'])
# fig5 = plt.figure(figsize=(8, 6))
# sns.scatterplot(data=filtered_df, x='stars_count', y='watchers', hue='is_popular')
# plt.title(f'Correlation: {correlation_starVSwatchers:.2f}')
# plt.xlabel('Stars Count')
# plt.ylabel('Watchers')
e1.subheader(f"Star-Watchers \ncorrelation: {round(correlation_starVSwatchers, 2) }")
# e1.write(fig5)

e1.image('assets/star-watch.png')

correlation_starVSforks = filtered_df['stars_count'].corr(filtered_df['forks_count'])
# fig6 = plt.figure(figsize=(8, 6))
# sns.scatterplot(data=filtered_df, x='stars_count', y='forks_count', hue='is_popular')
# plt.title(f'Correlation: {correlation_starVSforks:.2f}')
# plt.xlabel('Stars Count')
# plt.ylabel('Forks')
e2.subheader(f"Star-Forks \ncorrelation:{round(correlation_starVSforks, 2)}")
# e2.write(fig6)

e2.image('assets/star-fork.png')


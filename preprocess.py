import pandas as pd
import numpy as np
import ast


def count_languages(languages):
    try:
        languages_list = ast.literal_eval(languages)
        return len(languages_list)
    except (SyntaxError, ValueError):
        return np.nan


df1 = pd.read_csv('data/github_dataset.csv').drop_duplicates()
df2 = pd.read_csv('data/repository_data.csv').drop_duplicates()
df2['created_at'] = pd.to_datetime(df2['created_at']).dt.strftime('%Y-%m-%d')
df1['name'] = df1['repositories'].apply(lambda x: x.split('/')[1])
df1_ = df1[['name', 'stars_count', 'forks_count', 'pull_requests', 'language']].copy()
df1_.columns = ['name', 'stars_count', 'forks_count', 'pull_requests', 'primary_language']
df = pd.concat([df2, df1_])
df['languages_count'] = df['languages_used'].apply(count_languages)
pd.set_option('display.float_format', lambda x: '%.0f' % x)
df['is_popular'] = 'Bottom 75% in Popularity'
df.loc[df['stars_count'] >= 29, 'is_popular'] = 'Top 25% in Popularity'

df.to_csv('data/final_data.csv')

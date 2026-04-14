import pandas as pd

df = pd.read_csv('most_viewed_videos_1000.csv')
print(df.head())

print(df.info())
df = df.dropna()
print(df.info())
top10_videos = df.sort_values(by='views', ascending=False).head(10)
print(top10_videos[['title', 'views']])

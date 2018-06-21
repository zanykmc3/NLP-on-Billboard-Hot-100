import billboard
import pandas as pd

chart = billboard.ChartData('hot-100')
df = pd.DataFrame(columns=["title","artist","rank","peakPos","lastPos","weeks","date"])
df2 = pd.DataFrame(columns=["title","artist","rank","peakPos","lastPos","weeks","date"])

while chart.previousDate:
    print(chart.previousDate)
    for i in range(0,99):
        df.loc[i] = [chart[i].title,chart[i].artist,chart[i].rank,chart[i].peakPos,chart[i].lastPos,chart[i].weeks, chart.date]
    df2 = pd.concat([df2,df], ignore_index=True)
    chart = billboard.ChartData('hot-100', chart.previousDate)

df2.to_csv('billboard_data.csv')

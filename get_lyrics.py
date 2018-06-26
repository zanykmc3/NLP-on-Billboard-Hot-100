import requests
import pandas as pd
import lyricwikia as lw
from itertools import islice

# read in dataframe and add empty lyric column
df_billboard = pd.read_csv('billboard_data.csv')
df_billboard['lyrics'] = ""
first_artist_str = ""


# iterate through dataframe
# for batch processing: for index, row in islice(df_subset.iterrows(),240000,270000,1):
for index, row in df_billboard.iterrows():    

    # save csv every 10000 records
    if index % 10000 == 0:
        df_billboard.to_csv("lyric_dataset.csv")
        print("saved")
        
    # try to search for song lyrics, if no match: try again
    try:
        lyrics = lw.get_lyrics(row['artist'],row['title'])
        df_billboard.ix[index,'lyrics'] = lyrics
        print("match")
        
    # no match, but look for first artist listed
    except:      
        # find primary artist name
        spl = row['artist'].split()
        for i in range(len(spl)):
            if spl[i]=="Featuring":
                first_artist = spl[0:i]
            else:
                first_artist = spl
        for j in range(len(first_artist)):
            first_artist_str = first_artist_str + " " + first_artist[j]

        # try again
        try:
            lyrics = lw.get_lyrics(first_artist_str,row['title']) 
            df_billboard.ix[index,'lyrics'] = lyrics
            print("match")
            
        # no match
        except:
            print("no match")
            
        first_artist_str = ""

df_billboard.to_csv("lyric_dataset.csv")

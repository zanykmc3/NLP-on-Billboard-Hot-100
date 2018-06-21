import requests
import pandas as pd
import lyricwikia as lw

##def request_song_info(song_title, artist_name):
##    base_url = 'https://api.genius.com'
##    headers = {'Authorization': 'Bearer ' + 'INSERT YOUR TOKEN HERE'}
##    search_url = base_url + '/search'
##    data = {'q': song_title + ' ' + artist_name}
##    response = requests.get(search_url, data=data, headers=headers)
##
##    return response

df = pd.read_csv('billboard_data.csv')
df['lyrics'] = ""
yes = 0
no = 0
first_artist_str = ""
df_subset = df

for index, row in df_subset.iterrows():
    if index % 10000 == 0:
        df_subset.to_csv("lyric_match")
        print("saved")

    try:
        lyrics = lw.get_lyrics(row['artist'],row['title'])
        df_subset.ix[index,'lyrics'] = lyrics
        yes = yes + 1

    except:
  
        spl = row['artist'].split()
        for i in range(len(spl)):
            if spl[i]=="Featuring":
                first_artist = spl[0:i]
        for j in range(len(first_artist)):
            first_artist_str = first_artist_str + " " + first_artist[j]

        try:
            lyrics = lw.get_lyrics(first_artist_str,row['title'])
     
            df_subset.ix[index,'lyrics'] = lyrics
            yes = yes + 1
        except:
            no = no + 1

        first_artist_str = ""
    
df_subset.to_csv("lyric_match")

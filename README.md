# NLP-on-Billboard-Hot-100-1958-2018-
How has music changed? Natural Language Processing on Lyrics from The Billboard Hot 100 Songs from 1958 to 2018.

<h3>Description:</h3>
<h4>create_dataframe.py</h4>
<p>create_dataframe.py uses billboard-charts which is a Python API for accessing music charts (https://github.com/guoguo12/billboard-charts)</p>
<p>create_dataframe.py creates pandas dataframe of all Billboard Hot 100 records from 1958 to 2018.
  <br/>includes columns: title, artist, rank, peakPos, lastPos, weeks, date</p>
<p>outputs: billboard_data.csv which is csv version of dataframe</p>

<h4>get_lyrics.py</h4>
<p>get_lyrics.py takes in billboard_data.csv and uses lyricwikia which is a Python API to access song lyrics (https://github.com/enricobacis/lyricwikia)</p>
<p>get_lyrics.py creates pandas dataframe of all Billboard Hot 100 records from 1958 to 2018 with the entire song's lyrics.
  <br/>includes columns: title, artist, rank, peakPos, lastPos, weeks, date, lyrics</p>
<p><h4>inputs:</h4> billboard_data.csv which is csv version of dataframe</p>
<p>outputs: lyric_match.csv which is csv version of dataframe with lyrics</p>

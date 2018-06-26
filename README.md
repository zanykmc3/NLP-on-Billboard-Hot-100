# NLP-on-Billboard-Hot-100-1958-2018-
How has music changed? Natural Language Processing on Lyrics from The Billboard Hot 100 Songs from 1958 to 2018.

<h2>Description:</h2>
<h3>create_dataframe.py</h3>
<p>create_dataframe.py uses billboard-charts which is a Python API for accessing music charts (https://github.com/guoguo12/billboard-charts). create_dataframe.py creates pandas dataframe of all Billboard Hot 100 records from 1958 to 2018. Includes columns: title, artist, rank, peakPos, lastPos, weeks, date</p>
<p><b>outputs:</b> billboard_dataset.csv which is csv version of dataframe</p>

<h3>get_lyrics.py</h3>
<p>get_lyrics.py takes in billboard_data.csv and uses lyricwikia which is a Python API to access song lyrics (https://github.com/enricobacis/lyricwikia). get_lyrics.py creates pandas dataframe of all Billboard Hot 100 records from 1958 to 2018 with the entire song's lyrics. Includes columns: title, artist, rank, peakPos, lastPos, weeks, date, lyrics</p>
<p><b>inputs:</b> billboard_dataset.csv which is csv version of dataframe</p>
<p><b>outputs:</b> lyric_dataset.csv which is csv version of dataframe with lyrics</p>
<br/>
<p>Datasets can be downloaded<a href="https://drive.google.com/file/d/1QOEdjxJ9BadbiWk6a_Dm9ddxjWhFzeAs/view?usp=sharing" target="_blank"> here.</a></p>

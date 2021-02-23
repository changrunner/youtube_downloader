# playlist_config

## Purpose

* This folder contains a list of playlist to download.
* It does not get committed to git

## Sample config file

Create a new json file called playlist.json in this /app/playlist_config directory with the following content:

```
[
    {"playlist_name":"YourPlaylistName","playlist_id":"YouTubePlaylistID","save_format":"mp3","download_it":"false"},
]
```

#### Parameters

* playlist_name: You name this what ever you want. This is the folder it will be saved into in the mp3_download_directory or mp4_download_directory folder you specify in the app.{enviroment}.config

* playlist_id: The id of the playlist. Example: from https://www.youtube.com/playlist?list=PLl8cze0Ot7HeM9Yd0SJnawGyneHQMtvY12R the id is PLl8cze0Ot7HeM9Yd0SJnawGyneHQMtvY12R

* save_format: mp3 or mp4

* download_it: true or false
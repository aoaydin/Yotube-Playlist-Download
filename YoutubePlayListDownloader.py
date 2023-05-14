#!/usr/bin/python
# YoutubePlayListDownloader.py
# Created by Abdurrahman Aydın  @aoaydin 
# Edited by Abdurrahman Aydın   @aoaydin
## Tags - YouTube - Python - Playlist - Downloader


from pytube import Playlist, YouTube
from pytube.exceptions import VideoUnavailable
import os

playlist_url = input("Enter the playlist URL: ")

try:
    playlist = Playlist(playlist_url)
except KeyError:
    print("Invalid playlist URL.")
    exit()

playlist_title = playlist.title if playlist.title else 'Untitled'
folder_name = playlist_title.replace("/", "-")  # Geçersiz karakterleri çıkar

if playlist_title and not os.path.exists(folder_name):
    os.makedirs(folder_name)

total_videos = len(playlist.video_urls)

for i, video_url in enumerate(playlist.video_urls, start=1):
    try:
        yt = YouTube(video_url)
    except VideoUnavailable:
        print(f'Video {video_url} is unavailable, skipping.')
    else:
        video_title = yt.title if yt.title else f'Video {i}'
        print(f'Downloading video ({i}/{total_videos}): {video_title}')

        video = yt.streams.get_highest_resolution()
        video.download(output_path=folder_name)

        print('Download complete!')

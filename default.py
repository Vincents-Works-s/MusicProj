import vlc
import pafy

import urllib
import json
import re

import time
import random

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = "50ce6b13e4714c3d87aa102059b01fe0"
client_secret = "7febc9be981f453d93b19d92c2d4c20b"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


def get_track_ids(user, playlist_id):
    tracks = get_playlist_tracks(user, playlist_id)
    ids = []
    for i in range(len(tracks)):
        ids.append(tracks[i].get('track').get('id'))
    return ids


def get_track_features(id):
    meta = sp.track(id)
    features = sp.audio_features(id)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track


ids = get_track_ids('yellowazns123', '2x02jcUK9zbZg7r72Y0LTK')

while True:

    #get random song_id from playlist, remove from list
    song_id = random.choice(ids)
    ids.remove(song_id)
    song = get_track_features(song_id)
    track_name = song[0]
    artist = song[2]
    print(f"Track: {track_name}")
    print(f"Artist: {artist}")

    search_input = f"{track_name} {artist} audio"
    print(search_input)
    query_string = urllib.parse.urlencode({"search_query" : search_input})
    html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    video_ids = re.findall(r"watch\?v=(\S{11})", html_content.read().decode('utf-8'))
    url = "https://www.youtube.com/watch?v=" + video_ids[0]
    print(video_ids[0])

    #play song
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.audio_set_volume(80)
    player.play()

    #get length of track
    video_id = video_ids[0]
    API_KEY = "AIzaSyA5wF_FN1oZ0OhnEV9zsbpS3r0bNj45GBw"
    
    search_url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={API_KEY}&part=contentDetails'
    req = urllib.request.Request(search_url)
    response = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(response)
    all_data = data['items']
    duration = all_data[0]['contentDetails']['duration']
    print(duration)
    minutes = int(duration[2:].split('M')[0])
    seconds = duration[2:].split('M')[1].split('S')[0]
    if seconds == '':
        seconds = 0
    else:
        seconds = int(seconds)
    song_length = minutes * 60 + seconds
    print(song_length)

    #wait, repeat
    time.sleep(song_length - 5)
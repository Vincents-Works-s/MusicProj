import vlc
import pafy

import urllib
import re
import time

import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say somthing! ")
    audio = recognizer.listen(source)

print("Google Speech Recognition thinks you said: ")
print(recognizer.recognize_google(audio))

search_input = recognizer.recognize_google(audio) + "audio"
query_string = urllib.parse.urlencode({"search_query" : search_input})
html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
video_ids = re.findall(r"watch\?v=(\S{11})", html_content.read().decode('utf-8'))
url = "https://www.youtube.com/watch?v=" + video_ids[0]
print(video_ids[0])

video = pafy.new(url)
best = video.getbest()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.audio_set_volume(90)
player.play()

time.sleep(1000)
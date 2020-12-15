import vlc
import time
import datetime

eq = vlc.AudioEqualizer()
eq.set_amp_at_index(-20, 3)
eq.set_amp_at_index(-20, 2)
eq.set_amp_at_index(-20, 1)
eq.set_amp_at_index(-20, 0)


player = vlc.MediaPlayer()
media = vlc.Media("animals.mp3")
player.set_media(media)

player.audio_set_volume(100)
start = datetime.datetime.now()
player.play()

player2 = vlc.MediaPlayer()
media2 = vlc.Media('animals.mp3')
player2.set_media(media2)
player2.audio_set_volume(0)
#vlc.libvlc_media_player_set_equalizer(player2, eq)

difference = 0
last = 0
song_time = 0

while song_time <= 75068:
    delta = datetime.datetime.now() - start
    player_time = player.get_time()
    if player_time != last:
        last = player_time
        difference = delta.total_seconds() * 1000 - player_time

    song_time = int(delta.total_seconds() * 1000 - difference)
    song_time += 144
    #print(song_time)
    
player2.play()
player2.set_time(3959)
print('playing')

vol = 0
    
for _ in range(15):
    time.sleep(1)
    vol += 5
    player2.audio_set_volume(vol)
player.pause()
print(player2.audio_get_volume())

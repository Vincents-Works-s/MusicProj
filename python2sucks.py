import vlc
import time
import datetime

song = 'C:/Users/Admin/Desktop/Projects/Music Shit/Martin Garrix - Animals (Original Mix).mp3'

eq = vlc.AudioEqualizer()
eq.set_amp_at_index(-20, 0)
eq.set_amp_at_index(-20, 1)
eq.set_amp_at_index(-20, 2)
eq.set_amp_at_index(-20, 3)
eq.set_amp_at_index(-20, 4)
eq.set_amp_at_index(0, 5)
eq.set_amp_at_index(0, 6)
eq.set_amp_at_index(0, 7)

player = vlc.MediaPlayer(song)
player.audio_set_volume(100)

vlc.libvlc_media_player_set_equalizer(player, eq)
start = datetime.datetime.now()
player.play()
player.set_time(60000)

song2 = 'C:/Users/Admin/Desktop/Projects/Music Shit/Tremor (Sensation 2014 Anthem).mp3'

player2 = vlc.MediaPlayer(song2)
media2 = vlc.Media(song2)
player2.set_media(media2)
player2.audio_set_volume(20)
player2.play()

while player.get_time() <= 27000:
    pass
print('Changing eq')

x = -20
while x < 0:
    x += 1
    print(x)
    time.sleep(0.1)
    eq.set_amp_at_index(x, 0)
    eq.set_amp_at_index(x, 1)
    eq.set_amp_at_index(x, 2)
    eq.set_amp_at_index(x, 3)
    eq.set_amp_at_index(x, 4)
    #vlc.libvlc_media_player_set_equalizer(player, eq)

time.sleep(1000)
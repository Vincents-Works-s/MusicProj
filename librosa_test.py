import vlc
import librosa
import time
import datetime

song = 'C:/Users/Admin/Desktop/Projects/Music Shit/Music/Martin Garrix - Animals (Original Mix).mp3'
data, sr = librosa.load(song, sr=None, res_type='kaiser_fast')
print(sr)
tempo, beats = librosa.beat.beat_track(y=data, sr=sr)
print(tempo)

beats = librosa.frames_to_time(beats, sr=sr)

beats = [int(time * 1000) for time in beats]
print(beats[0])


eq = vlc.AudioEqualizer()
eq.set_amp_at_index(-20, 0)
eq.set_amp_at_index(-20, 1)
eq.set_amp_at_index(-20, 2)
eq.set_amp_at_index(-20, 3)

player = vlc.MediaPlayer()
media = vlc.Media(song)
player.set_media(media)
player.audio_set_volume(100)

vlc.libvlc_media_player_set_equalizer(player, eq)
start = datetime.datetime.now()
player.play()
player.set_time(beats[0])

while player.get_time() <= (beats[28] - 1000):
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
    vlc.libvlc_media_player_set_equalizer(player, eq)

time.sleep(25)
player.pause()
time.sleep(3)
player.play()
player.set_time(beats[64])
print(beats[64])

time.sleep(1000)
import vlc
import librosa
import time
import datetime

data, sr = librosa.load('Desktop/music_thing/animals.mp3', sr=None, res_type='kaiser_fast')
print(sr)
tempo, beats = librosa.beat.beat_track(y=data, sr=sr)

beats = librosa.frames_to_time(beats, sr=sr)

beats = [int(time * 1000) for time in beats]
print(tempo, beats)

##a = f'{beats[0]:.5f}'
##print(a)
##print(f'{beats[10]:.2f}')

eq = vlc.AudioEqualizer()
eq.set_preamp(0)
eq.set_amp_at_index(-20, 3)


player = vlc.MediaPlayer()
media = vlc.Media('Desktop/music_thing/beautiful creatures.mp3')
player.set_media(media)
player.audio_set_volume(75)

#vlc.libvlc_media_player_set_equalizer(player, eq)
start = datetime.datetime.now()
#player.play()
player.set_time(90859)

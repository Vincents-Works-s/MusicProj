import vlc

player = vlc.MediaPlayer()
media = vlc.Media("Desktop/music_thing/beautifil creatures.mp3")
player.set_media(media)
player.audio_set_volume(100)
player.play()
player.set_time(90302)

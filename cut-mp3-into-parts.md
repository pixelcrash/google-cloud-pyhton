# MP3 Cutter 

Change the +segment_time+ and the %03d file naming counter

ffmpeg -i "audio.mp3" -f segment -segment_time 60 -c copy speech2text_%03d.mp3


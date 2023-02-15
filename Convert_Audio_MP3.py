
#convert the wav file to mp3
from pydub import AudioSegment


# Load the WAV file
audio = AudioSegment.from_wav("Audio_Files/waveNet_Audio.wav")

# boost volume by 6dB
audio = audio + 6

# repeat the clip twice
audio = audio * 2

# 2 sec fade in
audio = audio.fade_in(2000)

# Save the WAV file as MP3
audio.export("Audio_Files/waveNet_Audio.mp3", format="mp3")
print('\nAudio conversion completed\n')
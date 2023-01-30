#brew install ffmpeg
#pip install pydub
from pydub import AudioSegment

audio = AudioSegment.from_wav("waveNet_sample.wav")

# boost volume by 6dB
audio = audio + 6

# repeat the clip twice
audio = audio * 2

# 2 sec fade in
audio = audio.fade_in(2000)

audio.export("waveNet_sample.mp3", format="mp3")
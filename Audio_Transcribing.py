
import os
from google.cloud import speech 
from google.cloud import storage

#connect to the OS Virtual Environment
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\mbenc\OneDrive - Atlantic TU\Semester 6\Project\WaveNet_Speech_Synthesis\wavenet-speech-synthesis-apikey.json'
from google.oauth2.service_account import Credentials

#print the google api key
creds = Credentials.from_service_account_file(
    'wavenet-speech-synthesis-apikey.json')
print(creds)


#Audio processing 
speech_client = speech.SpeechClient()

#Audio transcribed .... almost perfect
#audio_uri = 'gs://wavenet_speech_processing_bucket/waveNet_sample.mp3'
audio_uri = 'gs://wavenet_speech_processing_bucket/waveNet_Audio.mp3'
wav_uri_media = speech.RecognitionAudio(uri=audio_uri)

config_wav = speech.RecognitionConfig(
    #sample_rate_hertz = 48000,
    enable_automatic_punctuation=True,
    language_code='en-US',
    use_enhanced=True,
    model='video'
)
print('Audio Transcription....')
transcription = speech_client.long_running_recognize(
    config=config_wav,
    audio=wav_uri_media
)

transcript = transcription.result(timeout=2000)
print(transcript)

#to display only the transcription and confidence..
for t in transcript.results:
    print(t.alternatives[0].transcript)
    print(t.alternatives[0].confidence)
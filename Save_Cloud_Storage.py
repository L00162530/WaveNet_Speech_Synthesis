
import os
from google.cloud import speech 
from google.cloud import storage

#connect to the OS Virtual Environment
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\mbenc\OneDrive - Atlantic TU\Semester 6\Project\WaveNet_Speech_Synthesis\wavenet-speech-synthesis-apikey.json'
from google.oauth2.service_account import Credentials

#print the google api key
creds = Credentials.from_service_account_file(
    'wavenet-speech-synthesis-apikey.json')
print('Connected To GCP \n')


# Upload the audio file to GCP cloud storage
# Define your Google Cloud Storage bucket name
speech_bucket = "wavenet_speech_processing_bucket"

# Create a client for your Google Cloud Storage bucket
storage_client = storage.Client()
bucket = storage_client.bucket(speech_bucket)

# Define the file name and path
file_name = "waveNet_Audio.mp3"
file_path = "Audio_Files/waveNet_Audio.mp3"

# Upload the file to the Google Cloud Storage bucket
blob = bucket.blob(file_name)
blob.upload_from_filename(file_path)

# Confirm that the file has been uploaded
print(f"Audio file {file_name} has been uploaded to GCP Bucket -  {speech_bucket}. \n")
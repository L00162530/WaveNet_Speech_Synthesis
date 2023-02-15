
#synthesising text to speech sample
import os
from google.cloud import texttospeech

# set the environment variable for authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\mbenc\OneDrive - Atlantic TU\Semester 6\Project\WaveNet_Speech_Synthesis\wavenet-speech-synthesis-apikey.json'

# Instantiates a client
client = texttospeech.TextToSpeechClient()

#build the text
textInput = 'Text-to-Speech now offers the Custom Voice feature. Custom Voice allows you to train a custom voice model using your own studio-quality audio recordings to create a unique voice. You can use your custom voice to synthesize audio using the Text-to-Speech API. Warning: Custom Voice is a private feature. The online documentation is publicly available, but you will not be able to implement Custom Voice until you contact a member of the sales team. See the Text-to-Speech Custom Voice documentation.'

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=textInput)
print('Text to be transcribed \n'+textInput)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("Audio_Files/synthesisedAudio.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "synthesisedAudio.mp3"')
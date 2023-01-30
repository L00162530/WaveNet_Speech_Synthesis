import wave

# Explain
# - wave file structure 
# - number of channels - the number of independent channels 1 = mone 2 or more is stereo
# - sample width - the number of byte for each sample
# - framerate/sample_rate - this is the frequency of the sound
# - number of frames - total number of frames
# - values of a frame 

# open wave file
obj = wave.open("waveNet_sample.wav",'rb')

#print the properties of the sound
print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate.", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters:", obj.getparams())
frames = obj.readframes(obj.getnframes())

audio_time = obj.getnframes()/obj.getframerate()
print('time ',audio_time)

print(len(frames) / obj.getsampwidth(), frames[0], type(frames[0]))
obj.close()


# write wave file
sample_rate = 16000.0 # hertz
obj1 = wave.open("new_waveNet_sample.wav",'wb')
obj1.setnchannels(1) # mono
obj1.setsampwidth(2)
obj1.setframerate(sample_rate)
obj1.writeframes(frames)
obj1.close()
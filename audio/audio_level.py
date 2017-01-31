import struct

import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096
RECORD_SECONDS = 20
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print("recording...")

for i in range(RECORD_SECONDS):

    s = 0
    for j in range(RATE // CHUNK):
        data = stream.read(CHUNK)
        frames = struct.unpack("<" + str(CHUNK) + "h", data)
        for frame in frames:
            s+=abs(frame)
    print(s//RATE)


print("finished recording")



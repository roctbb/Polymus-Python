import pyaudio, wave

FORMAT = pyaudio.paInt16  # глубина звука = 16 бит = 2 байта
CHANNELS = 1  # моно
RATE = 48000  # частота дискретизации - кол-во фреймов в секунду
CHUNK = 4000  # кол-во фреймов за один "запрос" к микрофону - тк читаем по кусочкам
RECORD_SECONDS = 5  # длительность записи
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

# открываем поток для чтения данных с устройства записи по умолчанию
# и задаем параметры
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("recording...")

chunks = []  # список байтовых строк

# для каждого "запроса"
for i in range(0, RATE // CHUNK * RECORD_SECONDS):  # RATE // CHUNK - кол-во запросов в секунду
    data = stream.read(CHUNK)  # читаем строку из байт длиной CHUNK * FORMAT = 4000*2 байт
    chunks.append(data)  # добавляем строку в список

print("finished recording")

stream.stop_stream()
stream.close()
audio.terminate()

full_wave = b''.join(frames)  # склеиваем байт-строки в одну

# записываем в файл
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(full_wave)  # записываем
waveFile.close()

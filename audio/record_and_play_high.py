import struct, pyaudio

FORMAT = pyaudio.paInt16  # глубина звука = 16 бит = 2 байта
CHANNELS = 1  # моно
RATE = 48000  # частота дискретизации - кол-во фреймов в секунду
CHUNK = 4000  # кол-во фреймов за один "запрос" к микрофону - тк читаем по кусочкам
RECORD_SECONDS = 5  # длительность записи

audio = pyaudio.PyAudio()

# открываем поток для чтения данных с устройства записи по умолчанию
# и задаем параметры
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

# открываем поток для записи на устройство вывода - динамик - с такими же параметрами
out_stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, output=True)
print("recording...")

# список всех отсчетов
frames = []

# для каждого "запроса"
for i in range(0, RATE // CHUNK * RECORD_SECONDS):
    data = stream.read(CHUNK)  # читаем строку из байт длиной CHUNK * FORMAT = 4000*2 байт
    current_frames = struct.unpack("<" + str(CHUNK) + "h",
                                   data)  # строка -> список из CHUNK отсчетов, h - это short int
    frames += current_frames  # добавляем прочитанные отсчеты в общий список

print("finished recording")

# удаляем каждый 4ый отсчет - увеличиваем частоту на 25%
newframes = []
for i in range(0, len(frames)):
    if i % 4 != 0:
        newframes.append(frames[i])

full_wave = struct.pack("<" + str(len(newframes)) + "h", *newframes)  # список отсчетов -> строка из байт

out_stream.write(full_wave)  # отправляем на динамик

stream.stop_stream()
stream.close()
audio.terminate()

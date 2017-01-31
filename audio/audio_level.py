import struct, pyaudio

FORMAT = pyaudio.paInt16  # глубина звука = 16 бит = 2 байта
CHANNELS = 1  # моно
RATE = 48000  # частота дискретизации - кол-во фреймов в секунду
CHUNK = 4000  # кол-во фреймов за один "запрос" к микрофону - тк читаем по кусочкам
RECORD_SECONDS = 20  # длительность записи

audio = pyaudio.PyAudio()

# открываем поток для чтения данных с устройства записи по умолчанию
# и задаем параметры
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print("recording...")

# каждую секунду
for i in range(RECORD_SECONDS):
    s = 0  # сумма отсчетов за секунду

    # для каждого "запроса"
    for j in range(RATE // CHUNK):  # RATE//CHUNK - количество "запросов" к микрофону в секунду
        data = stream.read(CHUNK)  # читаем строку из байт длиной CHUNK * FORMAT = 4000*2 байт
        frames = struct.unpack("<" + str(CHUNK) + "h", data)  # строка -> список из CHUNK отсчетов, h - это short int

        # суммируем модули отсчетов - они могут быть отрицптельными
        for frame in frames:
            s += abs(frame)

    print(s // RATE)  # выводим среднюю громкость секунды

print("finished recording")

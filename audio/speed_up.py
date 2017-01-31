import wave,struct

#открываем файл для чтения
source = wave.open("file.wav", mode="rb")
#создаем новый файл, в который будем писать
result = wave.open("result.wav", mode="wb")

#берем параметры аудиопотока исходного файла (число каналов, част. дискр, глубина и тд.)
params = source.getparams()
#и задаем для нового такие же
result.setparams(params)

# узнаем количество отсчетов в файле
nframes = source.getnframes()

frames = struct.unpack("<"+str(nframes)+"h", source.readframes(nframes)) # строка из байт -> список отсчетов

newframes = []

newframes = frames[::2] # удаляем каждый второй

data = struct.pack("<"+str(len(newframes))+"h", *newframes) # список отсчетов -> строка из байт

result.writeframes(data) # отправляем на динамик
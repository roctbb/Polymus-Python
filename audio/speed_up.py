import wave,struct

#открываем файл для чтения
source = wave.open("file.wav", mode="rb")
#создаем новый файл, в который будем писать
result = wave.open("result.wav", mode="wb")

#берем параметры аудиопотока исходного файла (число каналов, част. дискр, глубина и тд.)
params = source.getparams()
#и задаем для нового такие же
result.setparams(params)

nframes = source.getnframes()

data = struct.unpack("<"+str(nframes)+"h", source.readframes(nframes))
newdata = []

newdata = data[::2]

newframes = struct.pack("<"+str(len(newdata))+"h", *newdata)

result.writeframes(newframes)
import queue  # fila de mensagens

import sounddevice as sd  # módulo para captura de som do mic
# reconhecimento de fala
from vosk import Model, KaldiRecognizer, SetLogLevel

SetLogLevel(-1)  # desabilita os logs do vosk

q = queue.Queue()  # instanciação da fila


# Função usada pelo RawInputStream
def callback(indata, frames, time, status):
    q.put(bytes(indata))


# Descobrir a taxa de amostragem
device_info = sd.query_devices(sd.default.device[0], 'input')
samplerate = device_info['default_samplerate']

with sd.RawInputStream(dtype = 'int16', channels = 1, callback = callback):
    # Inicializa o modelo e o reconhecedor
    modelo = Model("modelo")
    rec = KaldiRecognizer(modelo, samplerate)
    try:
        while True:
            # Coleta os dados e testa se o texto foi
            # convertido com sucesso
            data = q.get()
            if rec.AcceptWaveform(data):
                print(rec.FinalResult())
    except KeyboardInterrupt:
        print("Encerrando a captura de áudio…")

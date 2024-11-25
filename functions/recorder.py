import pyaudio, wave, tkinter
import tkinter.ttk as ttk

def recorder_old(text):
    audio= pyaudio.PyAudio()
    stream= audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input=True, frames_per_buffer=1024)

    frames= []

    print("Recording")

    try:
        while True:
            data= stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file= wave.open('myrecording.wav', 'wb')
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)

    sound_file.writeframes(b''.join(frames))
    sound_file.close()
    return


def threads(text):
    global running
    if running:
        running= False
    else:
        running= True
    recorder(text)

def recorder(text: tkinter.StringVar):
    text.set("Recording")
    audio= pyaudio.PyAudio()
    stream= audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input=True, frames_per_buffer=1024)

    frames = []

    try:
        while True:
            text.set("Recording")
            data= stream.read(1024)
            frames.append(data)
    
    except KeyboardInterrupt:
        text.set("Stopped Recording")
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()
    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file= wave.open('recordings/myrecording.wav', 'wb')
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)

    sound_file.writeframes(b''.join(frames))
    sound_file.close()

    return
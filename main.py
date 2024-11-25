import tkinter.ttk as ttk
import tkinter
from functions import recorder

def VoiceRecorder():
    window= tkinter.Tk()
    icon = tkinter.PhotoImage(file= "assets/icon.png")

    mic_on= tkinter.PhotoImage(file="assets/mic_on.png")
    mic_off= tkinter.PhotoImage(file="assets/mic_off.png")
    text= tkinter.StringVar()
    text.set("Not Currently Recording")

    # window.geometry("300x300")
    window.title("Voice Recorder")
    window.iconphoto(True, icon)
    ttk.Label(window, textvariable=text, borderwidth=0).grid(row=0, column=0)
    ttk.Button(window, image=mic_off, command=lambda: recorder.recorder(text)).grid(row=1, column=0)

    window.mainloop()

VoiceRecorder()
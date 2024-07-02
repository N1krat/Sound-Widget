from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
import tkinter as tk

class App(tk.Tk): 
    def __init__(self):
        super().__init__()
app = App()

# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

sessions = AudioUtilities.GetAllSessions()

for session in sessions: 
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    if session.Process and session.Process.name() == "Spotify.exe": 
        volume.SetMasterVolume(1, None)
    elif session.Process and session.Process.name() == "chrome.exe":
        volume.SetMasterVolume(1, None)


app.mainloop()
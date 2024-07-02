from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


class App(tk.Tk): 
    def __init__(self):
        super().__init__()

app = App()

is_playing = False

def play():
    print("play")

def pause(): 
    print("pause")

def forward(): 
    print("forward")

def rewind(): 
    print("rewind")

def update_play_pause_button():
    if is_playing:
        play_pause_button.config(image=pause_image)
    else:
        play_pause_button.config(image=play_image)

def toggle_play_pause(): 
    global is_playing
    if is_playing:
        pause()
    else: 
        play()
    is_playing = not is_playing
    update_play_pause_button()

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


# Load buttn images
button_width, button_height = 50, 50
play_image = resize_image("Sound-Widget/img/play.png", button_width, button_height)
pause_image = resize_image("Sound-Widget/img/pause.png", button_width, button_height)
next_image = resize_image("Sound-Widget/img/fast-forward.png", button_width, button_height)
rewind_image = resize_image("Sound-Widget/img/rewind-button.png", button_width, button_height)

# Creting bttns
play_pause_button = tk.Button(app, image=play_image, command=toggle_play_pause)
next_button = tk.Button(app, image=next_image, command=forward)
rewind_button = tk.Button(app, image=rewind_image, command=rewind)

# anti-garbage collectin
play_pause_button.image = play_image
next_button.image = next_image
rewind_button.image = rewind_image

# Bttn positions and padding
bottom_frame = tk.Frame(app)
bottom_frame.pack(side=tk.BOTTOM, pady=20)  

rewind_button.pack(side=tk.LEFT, padx=10)  
play_pause_button.pack(side=tk.LEFT, padx=10)
next_button.pack(side=tk.LEFT, padx=10)

# Gettin defalt audio and sessions to change the volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

sessions = AudioUtilities.GetAllSessions()

for session in sessions: 
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    if session.Process and session.Process.name() == "Spotify.exe": 
        volume.SetMasterVolume(1, None)



# Apps global settings
app.geometry("400x200")
app.resizable(False, False)
app.title("Audio Player")
app.wm_attributes('-toolwindow', 'True')
app.mainloop()

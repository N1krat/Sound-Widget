from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import spotilib

class App(tk.Tk): 
    def __init__(self):
        super().__init__()

app = App()

is_playing = False

def play():
    spotilib.play()

def pause(): 
    spotilib.play()

def forward(): 
    spotilib.forward()

def rewind(): 
    spotilib.previous()

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

# volume funct
def volume(value): 
    volume.SetMasterVolume(volume_slider.get() / 100, None)

def mute(): 
    spotilib.mute()


# Load buttn images
button_width, button_height = 50, 50
play_image = resize_image("img/play.png", button_width, button_height)
pause_image = resize_image("img/pause.png", button_width, button_height)
next_image = resize_image("img/fast-forward.png", button_width, button_height)
rewind_image = resize_image("img/rewind-button.png", button_width, button_height)
mute_image = resize_image("img/volume-mute.png", button_width, button_height)

# Creting bttns
play_pause_button = tk.Button(app, image=play_image, command=toggle_play_pause)
next_button = tk.Button(app, image=next_image, command=forward)
rewind_button = tk.Button(app, image=rewind_image, command=rewind)
mute_button = tk.Button(app, image=mute_image, command=mute)

# anti-garbage collectin
play_pause_button.image = play_image
next_button.image = next_image
rewind_button.image = rewind_image
mute_button.image = mute_image

# Bttn positions and padding
print(spotilib.song())

bottom_frame = tk.Frame(app)
bottom_frame.pack(side=tk.BOTTOM, pady=20)  

rewind_button.pack(side=tk.LEFT, padx=10)  
play_pause_button.pack(side=tk.LEFT, padx=10)
next_button.pack(side=tk.LEFT, padx=10)
mute_button.pack(side=tk.LEFT, padx=10)

volume_slider = tk.Scale(app, from_=0, to=100, orient=tk.VERTICAL, command=volume)
volume_slider.pack(padx=10, pady=10, fill=tk.Y)
volume_slider.set(100)

volume_slider.config(length=500, showvalue=0, tickinterval=20, digits=3)

# Gettin defalt audio and sessions to change the volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

sessions = AudioUtilities.GetAllSessions()

for session in sessions: 
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    if session.Process and session.Process.name() == "spotify.exe": 
        volume.SetMasterVolume(1, None)
    # IN THE FUTURE who wants to change the volume to specific apps not only spotify or global volume
    # you can add and elif with other procceses if you can find the one that is working
    



# Apps global settings
app.geometry("400x200")
app.resizable(False, False)
app.title(" ")
app.wm_attributes('-toolwindow', 'True')
app.mainloop()
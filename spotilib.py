import win32gui
import win32api

### Virtual-KeyCodes ###
Media_Next = 0xB0
Media_Previous = 0xB1
Media_Pause = 0xB3  # Play/Pause
Media_Mute = 0xAD


# spotify song and author info !!!NOT WORKING!!!   
def getwindow(Title="SpotifyMainWindow"):
	window_id = win32gui.FindWindow(Title, None)
	return window_id
	
def song_info():
	try:
		song_info = win32gui.GetWindowText(getwindow())
	except:
		pass
	return song_info

def artist():
	try:
		temp = song_info()
		artist, song = temp.split(" - ",1)
		artist = artist.strip()
		return artist
	except:
		return "There is noting playing at this moment"
	
def song():
	try:
		temp = song_info()
		artist, song = temp.split(" - ",1)
		song = song.strip()
		return song
	except:
		return "There is noting playing at this moment"

# Media Cntrl
def hwcode(Media):
    hwcode = win32api.MapVirtualKey(Media, 0)
    return hwcode


def forward():
    try:
        win32api.keybd_event(Media_Next, hwcode(Media_Next))
    except Exception as e:
        print(f"Error pressing next song key: {e}")


def previous():
    try:
        win32api.keybd_event(Media_Previous, hwcode(Media_Previous))
    except Exception as e:
        print(f"Error pressing previous song key: {e}")


def play():
    try:
        win32api.keybd_event(Media_Pause, hwcode(Media_Pause))
    except Exception as e:
        print(f"Error pressing pause/play key: {e}")


def mute():
    try:
        win32api.keybd_event(Media_Mute, hwcode(Media_Mute))
    except Exception as e:
        print(f"Error pressing mute/unmute key: {e}")

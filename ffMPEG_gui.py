
import tkinter as tk
from tkinter import filedialog
import subprocess
import os



### TO IMPROVE:
# warn user of file overwrite

#%% - Dependencies
import os
import tkinter as tk
from tkinter import filedialog

#%% - Functions
def find_ffmpeg():
    # Define the possible installation paths
    possible_folders = [
        r'C:\Program Files\ffmpeg\\',
        r'C:\Program Files (x86)\ffmpeg\\',
        r'C:\Program Files\\',
        r'C:\Program Files (x86)\\',
    ]

    def find_ffmpeg_recursive(folder):
        for root, dirs, files in os.walk(folder):
            if 'ffmpeg.exe' in files:
                return os.path.join(root, 'ffmpeg.exe')
        return None

    # Try to find ffmpeg.exe in the predefined folders and their subfolders
    ffmpeg_path = None

    for folder in possible_folders:
        ffmpeg_path = find_ffmpeg_recursive(folder)
        if ffmpeg_path:
            break

    # If not found, prompt the user to locate it
    if ffmpeg_path is None:
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        file_path = filedialog.askopenfilename(
            title="Locate ffmpeg.exe",
            filetypes=[("Executable Files", "ffmpeg.exe")]
        )

        if file_path:
            ffmpeg_path = file_path

    # Save the found path to a file for future use (even if it was found in predefined folders)
    if ffmpeg_path:
        with open('ffmpeg_path.txt', 'w') as f:
            f.write(ffmpeg_path)
    return ffmpeg_path

#%% - Main - Locate ffmpeg.exe
if os.path.exists('ffmpeg_path.txt'):
    with open('ffmpeg_path.txt', 'r') as f:
        ffmpeg_path = f.read()
else:
    ffmpeg_path = find_ffmpeg()

#%% - Main - Select files

### SELECT VIDEO FILE
root = tk.Tk()
root.withdraw()  # Hide the main window
video_file_path = filedialog.askopenfilename(title="Select a video file", filetypes=([("Video Files", "*.mp4 *.avi *.mkv *.mov *.wmv *.flv *.webm *.ogg *.ogv *.mpeg *.mpg *.m4v *.3gp *.3g2 *.ts *.vob *.mxf *.tsv *.mts *.m2ts *.m2v *.divx *.f4v *.rmvb *.asf *.rm *.m1v *.m2v *.m2t *.amv *.mpv *.nut *.dv *.drc")]))
if video_file_path:
    print(f"Selected file: {video_file_path}")
else:
    print("No file selected")

### SELECT AUDIO FILE
root = tk.Tk()
root.withdraw()  # Hide the main window
audio_file_path = filedialog.askopenfilename(title="Select a audio file", filetypes=([("Audio Files", "*.ac3 *.eac3 *.flac *.ape *.aac *.wma *.pcm *.wav *.mp3 *.m4a *.ogg *.oga *.wv *.tta *.mka *.opus *.ra *.aif *.aiff *.caf *.au *.alac *.mpc *.tak *.shn *.wv *.wma *.aac *.m4a *.dts *.dtshd *.w64 *.sds")]))
if video_file_path:
    print(f"Selected file: {audio_file_path}")
else:
    print("No file selected")


#%% - Main - Select output file location

# Extract the file extension from the loaded video path3
file_extension = os.path.splitext(video_file_path)[-1]

root = tk.Tk()
root.withdraw()  # Hide the main window
# Open a file dialog to select the output file location
output_file_path = filedialog.asksaveasfilename(defaultextension=file_extension, title="Select a output file location", filetypes=[("Video file", file_extension)])
if output_file_path:
    print(f"Selected file location: {output_file_path}")
else:
    print("No file location selected")


#%% - Main - Run ffmpeg
# Command to run ffmpeg with full paths
command = [ffmpeg_path, '-i', f'{video_file_path}', '-i', f'{audio_file_path}', '-c:v', 'copy', '-map', '0:v:0', '-map', '1:a:0', f'{output_file_path}']

# Run the command
result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

# Print the output of the command
print(result.stdout)

#%% - Main - Finished
# Popup to inform the user that the process is finished
root = tk.Tk()
root.withdraw()  # Hide the main window
tk.messagebox.showinfo(title="Finished", message="The process is finished")

# Exit the program
exit()

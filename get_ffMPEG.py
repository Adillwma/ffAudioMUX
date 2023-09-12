import subprocess
import os
import subprocess
import os
import shutil

# Specify the URL of the gyan.dev repository
ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

# Specify the directory where you want to install FFmpeg
install_dir = "C:\Remove\\"

# create the directory if it doesn't exist
os.makedirs(install_dir, exist_ok=True)

# Define the command to download and extract the FFmpeg binaries
download_command = [
    "curl",
    "-L",
    "-o",
    "ffmpeg.zip",
    ffmpeg_url,
]
extract_command = [
    "tar",
    "xf",
    "ffmpeg.zip",
    "-C",
    install_dir,
]

# Run the download and extract commands
try:
    subprocess.run(download_command, check=True)
    subprocess.run(extract_command, check=True)

    # Find the subdirectory in the installation directory
    subdirs = [d for d in os.listdir(install_dir) if os.path.isdir(os.path.join(install_dir, d))]

    if len(subdirs) == 1:
        subdir_name = subdirs[0]
        
        # Move all files and subdirectories from the subdirectory to the main directory
        subdir_path = os.path.join(install_dir, subdir_name)
        for item in os.listdir(subdir_path):
            item_path = os.path.join(subdir_path, item)
            if os.path.isfile(item_path) or os.path.isdir(item_path):
                shutil.move(item_path, install_dir)

        # Remove the now-empty subdirectory
        os.rmdir(subdir_path)

        
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
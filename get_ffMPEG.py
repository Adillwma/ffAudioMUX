import subprocess
import os
# Specify the URL of the gyan.dev repository
ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

# Specify the directory where you want to install FFmpeg
install_dir = "C:\Remove\\"


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
    os.remove("ffmpeg.zip")  # Remove the downloaded ZIP file
    print("FFmpeg installed successfully!")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
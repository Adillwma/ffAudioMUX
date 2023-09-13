# ffAudioMUX: Replace Audio in Videos Without Re-encoding

[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)

Very lightweight python GUI that simplifies the process of using ffMPEG to replace the audio of a video, without the need for time-consuming re-encoding. Super usefull workflow tool to fix mistakes or to sync audio, does no harm to the video!

- Automatically retrieves the latest version of ffmpeg.exe if it's not already installed, no need to build from source.

- Bundled as a Windows executable (.exe) file, so you don't need to worry about installing Python or delving into code.

- GUI removes the need to use the command line, making the process of replacing audio in a video much more accessible.

#

<img src="Images/ffAudioMUX _V1_Img.png" alt="GUI V1">

#


## How to use
For Windows Users

- Download: Simply download the ffAudioMUX_v1.exe file from our releases page.

- Run: Execute the ffAudioMUX_v1.exe file.

- Program usage: Select the video file you want to replace the audio of, then select the audio file you want to replace it with. Finally, select the output file name and location, and click the "RUN the MUX" button. The program will then run the ffmpeg command to replace the audio of the video file without re-encoding it, you will see the ffmpeg process executing in the terminal but do not need to interact with it. Once the process is finsihed you will be notified.






## Additional Notes
- For proper result your audio files should already the same length and syncronized with the video files audio track. If you need to syncronize your audio files with the video file, you can use the free software [Audacity](https://www.audacityteam.org/) or any other DAW or wave editor to do so.

- The first time you run ffAudioMUX.exe, it will search for the ffmpeg.exe executable. This initial setup might take a moment. If it doesn't find ffmpeg.exe, don't worry; ffAudioMUX will automatically install it from the latest build.

- Your ffmpeg.exe file's location is saved in a text file within the same folder as ffAudioMUX.exe after the initial setup. This way, it won't need to search for it again on future runs.

- If you ever move the location of your ffmpeg.exe file in the future, you can safely delete the saved text file. The next time you run ffAudioMUX.exe, it will locate your ffmpeg.exe file without any issues.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. 

## Contributions
Contributions to this codebase are welcome! If you encounter any issues, bugs or have suggestions for improvements please open an issue or a pull request on the [GitHub repository](https://github.com/Adillwma/ffAudioMUX).

## Contact
For any further inquiries or for assistance, please feel free to reach out to me at adillwmaa@gmail.com.
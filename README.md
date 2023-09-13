# ffAudioMUX: Replace Audio in Videos Without Re-encoding

[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)

Simple windows tool with GUI to effortlessly replace audio in a video without the need for time-consuming re-encoding. Super usefull workflow tool to fix mistakes or to sync audio, does no harm to the video!

- Very simple python wrapper that utilises ffMPEG to replace the audio of a video without reencoding. 

- Bundled it as a Windows executable (.exe) file, so you don't need to worry about installing Python or delving into code.

- Much faster than re-encoding the video, and no video degradation from addition encode passes.

<img src="Images/ffAudioMUX _V1_Img.png" alt="GUI V1">


## How to use
For Windows Users

    Download: Simply download the ffAudioMUX_v1.exe file from our releases page.

    Run: Execute the ffAudioMUX_v1.exe file.



## Additional Notes

- The first time you run ffAudioMUX.exe, it will search for the ffmpeg.exe executable. This initial setup might take a moment. If it doesn't find ffmpeg.exe, don't worry; ffAudioMUX will automatically install it from the latest build.

- Your ffmpeg.exe file's location is saved in a text file within the same folder as ffAudioMUX.exe after the initial setup. This way, it won't need to search for it again on future runs.

- If you ever move the location of your ffmpeg.exe file in the future, you can safely delete the saved text file. The next time you run ffAudioMUX.exe, it will locate your ffmpeg.exe file without any issues.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. 

## Contributions
Contributions to this codebase are welcome! If you encounter any issues, bugs or have suggestions for improvements please open an issue or a pull request on the [GitHub repository](REPO URL!!!! INSERT HERE !!!!!).

## Contact
For any further inquiries or for assistance, please feel free to reach out to me at adillwmaa@gmail.com.
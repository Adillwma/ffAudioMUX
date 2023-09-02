# ffAudioMUX
Replace audio in a video without reencoding. 
Super usefull workflow tool to fix mistakes or to sync audio without having to wait for a long video reencode. Does no harm to the video!

Very simple python wrapper that utilises ffMPEG to replace the audio of a video without reencoding. 
Bundled as a windows exe file so that users are not put off by having to install python or look at code. 

If you do not already have ffMPEG downloaded to your PC you can run the handy get_ffMPEG.exe that is included in the tools folder or download it manually via {(https://ffmpeg.org/download.html)}. This must be done before running ffAudioMUX.

# To use
Just download the ffAudioMUX folder. It contains the get_ffMPEG.exe if you do not already have ffmpeg on your computer, and the ffAudioMUX.exe file which allows you to replace the audio of a video file. 

# Notes
When ffAudioMUX.exe is run for the first time it will search for ffmpeg.exe, this may take a moment. If the file is not found it will prompt you to locate it manually. This only happens the first time the program is run, the location is saved in a txt file in the same folder as you have ffAudioMUX.exe, and loaded from there on future use. 

If you move the location of your ffmpeg.exe file in the future then you can safely delete the .txt fileand the next time you run ffAudioMux.exe it will relocate your ffmpeg.exe file.

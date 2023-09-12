# ffAudioMUX
Replace audio in a video without re-encoding. 
Super usefull workflow tool to fix mistakes or to sync audio without having to wait for a long video reencode. Does no harm to the video!

Very simple python wrapper that utilises ffMPEG to replace the audio of a video without reencoding. 
Bundled as a windows exe file so that users are not put off by having to install python or look at code. 


<img src="Images/ffAudioMUX _V1_Img.png" alt="GUI V1">

# To use
For Windows Users:


Just download the ffAudioMUX_v1.exe file and run. 


# Notes
When ffAudioMUX.exe is run for the first time it will search for ffmpeg.exe, this may take a moment. If the file is not found it will install it from the latest build. This only happens the first time the program is run, the location is saved in a txt file in the same folder as you have ffAudioMUX.exe, and loaded from there on future use. 

If you move the location of your ffmpeg.exe file in the future then you can safely delete the .txt fileand the next time you run ffAudioMux.exe it will relocate your ffmpeg.exe file.


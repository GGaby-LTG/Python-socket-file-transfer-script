# Python-socket-file-transfer-script
This is a script I made, it allows a client to request a file from a host computer and receive it. It's quite simplistic but it works pretty well.


To use all you need is a relatively modern version of python (3.11 and up) as well as the "tqdm" module though it is only used once for purely esthetic purposes so you could delet the istance at which it appears and the script would function perfectly fine.

The script can normally transfer any file of any size but I have only tested it with png, jpg, txt, py, mp3, mp4, docx and pdf with a max tested file size of 1.4 gigabytes. If you have any problems with the files corrupting the best way to fix this is to reduce the chunk size though this normally never happens with the default 128 byte size.
If you have any questions you can comment and I'll try to reply and fix the isue.

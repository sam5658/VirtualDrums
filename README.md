# Virtual Drums
This project creates a Virtual Drumset Window. In the window there are two drums(snare, kick) shown in a small boxes, When one Hits The boxes with the defined colour It gerates a sound. This Project is unique as Compared to other Virtual Drums because It uses MultiThreading To generate sound and The sound is only played once every hit and makes the drum set More realistic.

## Installation
clone the project and then navigate to VirtualDrums
```
pip install -r requirements.txt 
```

You can Then select The colour of the object you want use with colordetection.py, you have to choose the object you want to use to play the drums and then run the code below, it will open three windows mask, videocapture, and the bars, move the bars and selct the hsv values with the best mask. Default colur is green with hsv values are[ 32 , 78 , 90 ,  79  ,   255 , 255 ] 

```
python colordetection.py
```

Finally you can use the VirtualDrums by typing the command

```
python VirtualDrums.py
```

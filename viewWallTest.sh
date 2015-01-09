#!/bin/sh

ssh -fx user@epenguin-10.rit.edu "pkill x11vnc " &
ssh -fx user@epenguin-16.rit.edu "pkill x11vnc " &
ssh -fx user@epenguin-18.rit.edu "pkill x11vnc " &
ssh -fx user@epenguin-13.rit.edu "pkill x11vnc " &
ssh -fx user@epenguin-05.rit.edu "pkill x11vnc " &
ssh -fx user@epenguin-07.rit.edu "pkill x11vnc " 

ssh -fx user@epenguin-10.rit.edu "x11vnc --once --safer -display :0 --scale 1/4 " &
ssh -fx user@epenguin-16.rit.edu "x11vnc --once --safer -display :0 --scale 1/4 " &
ssh -fx user@epenguin-18.rit.edu "x11vnc --once --safer -display :0 --scale 1/4 " &
ssh -fx user@epenguin-13.rit.edu "x11vnc --once --safer -display :0 --scale 1/4 " &
ssh -fx user@epenguin-05.rit.edu "x11vnc --once --safer -display :0 --scale 1/4 " &
ssh -fx user@epenguin-07.rit.edu "x11vnc --once --safer -display :0 --scale 1/4 " &
sleep 10

#ssh -fxX user@129.21.47.26 "gnome-system-monitor" &
#ssh -fxX user@129.21.47.45 "gnome-system-monitor" &
#ssh -fxX user@129.21.47.168 "gnome-system-monitor" &
#ssh -fxX user@129.21.47.15 "gnome-system-monitor" &
#ssh -fxX user@129.21.47.80 "gnome-system-monitor" &
#ssh -fxX user@129.21.47.11 "gnome-system-monitor" &

vncviewer epenguin-10.rit.edu &
vncviewer epenguin-16.rit.edu &
vncviewer epenguin-18.rit.edu &
vncviewer epenguin-13.rit.edu &
vncviewer epenguin-05.rit.edu &
vncviewer epenguin-07.rit.edu &
~                                                                               
~                                                           

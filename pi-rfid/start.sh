#!/bin/bash

while true
do
    sudo python3 /home/pi/pi-rfid/Read.py &
    pidRead=$!
    wait $pidRead

    sudo python3 /home/pi/pi-rfid/Send.py &
    pidSend=$!
    wait $pidSend

    sleep 2
done

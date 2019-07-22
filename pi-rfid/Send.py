#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import signal
import sys

def exitProgram(sig, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, exitProgram)
signal.signal(signal.SIGTERM, exitProgram)

reader = SimpleMFRC522()

try:
    id, text = reader.read()
    print(id)
finally:
    GPIO.cleanup()

with open("idfile.txt", "w") as f:
    f.write(str(id))
    f.close()

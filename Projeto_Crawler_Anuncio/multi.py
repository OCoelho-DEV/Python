import threading
import time

def request_web():
    print('Doing request...')
    time.sleep(3)
    print('Finishing request')

thread_1 = threading.Thread(target=request_web)
thread_1.start()

thread_2 = threading.Thread(target=request_web)
thread_2.start()

thread_3 = threading.Thread(target=request_web)
thread_3.start()
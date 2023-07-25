import time
def print_time():
    now = time.localtime()
    print(f"The time is {now.hour}:{now.minute}:{now.second}")
print_time()
while True:
    time.sleep(1)
    print_time()
​
import time

def timed_print(string, delay=0.075):
    # prints character by character based on delay speed.
    for c in string:
        print(c, end='', flush=False)
        time.sleep(delay)
    print()


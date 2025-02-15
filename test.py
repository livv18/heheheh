import time
from threading import Thread
import sys

lyrics = [
    ("And all i do", 0.09),
    ("Was sit and think about you", 0.09),
    ("If i knew, what you'd do?", 0.09),
    ("Collapse my veins wearing beautiful shoes", 0.08),
    ("IT's not living if it's not with you", 0.1)
]
delays = [0, 5.0, 11.0, 17.0, 20.8]

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
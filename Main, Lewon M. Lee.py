import time
from Storyline import *
from Map import *
from Ending import *

print("ㄒ卄乇 爪卂几丂丨ㄖ几 ㄖ千 ᗪ乇卂ᗪᗪ卂ㄚ")
time.sleep(1)
print("By: Lewon M. Lee")
time.sleep(1)
print("A 2020 text-based game.")
time.sleep(1)

start_screen_error = True
while start_screen_error:
    begin_or_exit = input("\nStart or Exit game? (type 'Start' or 'Exit'): ")
    if begin_or_exit == 'Start':
        time.sleep(1)
        storyline1()  # introduction1
        storyline2()  # introduction2
        create_linear()  # map
        storyline3()  # ending
    elif begin_or_exit == 'Exit':
        start_screen_error = False
        print("You left the game")
        raise SystemExit
    else:
        print("Invalid Answer")

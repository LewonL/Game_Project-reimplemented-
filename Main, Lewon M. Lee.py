import time

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
        start_screen_error = False
        time.sleep(1)
        import Storyline.py
        import Map.py
        time.sleep(5)

    elif begin_or_exit == 'Exit':
        start_screen_error = False
        print("You left the game")
        raise SystemExit
    else:
        print("Invalid Answer")

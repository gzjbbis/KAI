import time
from datetime import datetime

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def show_current_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f"Current time: {current_time}")

# 专注时钟示例，设置为25分钟
pomodoro_timer(25)

# 显示当前时间
show_current_time()

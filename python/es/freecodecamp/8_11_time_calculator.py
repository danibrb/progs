#TODO complete the assignment

def add_time(start, duration):
    start = '8:16 PM'
    duration = '466:02'
    day = ''
    n_days = 0
    start = start.replace(':',' ').split()
    print(start)
    start_hour, start_minute, ampm = start
    print(start_hour,start_minute, ampm)
    duration_hour, duration_minute =  duration.replace(':',' ').split()
    print(duration_hour,duration_minute)
    final_hour = int(start_hour) + int(duration_hour)
    if final_hour > 12:
        if ampm == 'AM':
            ampm = 'PM'
        else:
            ampm = 'AM'
            day = ' (next day)'
        final_hour += 12
    n_days =  int(final_hour)//24
    if n_days:
        day = f' ({n_days} days later)'
        final_hour %= 24
        
    final_minute = int(start_minute) + int(duration_minute)
    if final_minute > 59:
        final_minute -= 60
        final_hour += 1
    new_time = f'{final_hour}:{final_minute:02} {ampm}{day}'

    return new_time


print(add_time('3:00 PM', '3:10'))
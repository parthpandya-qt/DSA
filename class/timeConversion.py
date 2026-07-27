def time(time_str):
    time1 = list(map(int, time_str.split(":")))
    hour = time1[0]
    minute = time1[1]
    second = time1[2] if len(time1) > 2 else 0

    
    if hour == 0:
        hour = 12
        period = "AM"
    elif hour < 12:
        period = "AM"
    elif hour == 12:
        period = "PM"
    else:
        hour = hour - 12
        period = "PM"
    
    
    if len(time1) > 2:
        return f"{hour:02d}:{minute:02d}:{second:02d} {period}"
    else:
        return f"{hour:02d}:{minute:02d} {period}"


print(time("24:30:00")) 

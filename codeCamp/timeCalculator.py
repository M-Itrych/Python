def add_time(start_time, duration, start_day=""):
    start_time = start_time.split(" ")

    hours_duration = int(duration.split(":")[0])
    minutes_duration = int(duration.split(":")[1])

    hours_time = int(start_time[0].split(":")[0])
    minutes_time = int(start_time[0].split(":")[1])
    part_of_day = start_time[1]

    day = 0
    day_string = start_day.lower().capitalize()
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if day_string in day_of_week:
        day_index = day_of_week.index(day_string)

    for i in range(minutes_duration):
        minutes_time += 1
        if minutes_time == 60:
            minutes_time = 0
            hours_time += 1
            if part_of_day == "PM" and hours_time == 12:
                part_of_day = "AM"
                day += 1
                hours_time = 0
            if part_of_day == "AM" and hours_time == 12:
                part_of_day = "PM"
                hours_time = 0

    for i in range(hours_duration):
        hours_time += 1
        if part_of_day == "PM" and hours_time == 12:
            part_of_day = "AM"
            day += 1
            hours_time = 0
        if part_of_day == "AM" and hours_time == 12:

            part_of_day = "PM"
            hours_time = 0
    res = ""
    if (part_of_day == "PM" or part_of_day == "AM") and hours_time == 0:
        print(hours_time)
        res += "12:"
    else:
        res += f"{hours_time}:"

    if minutes_time < 10:
        res += f"0{minutes_time} "
    else:
        res += f"{minutes_time} "

    res += f"{part_of_day}"
    if day_string in day_of_week:
        for i in range(day):
            day_index += 1
            if day_index == 7:
                day_index = 0
        if day == 0:
            res += f", {day_of_week[day_index]}"
        if day != 1 and day != 0:
            res += f", {day_of_week[day_index]} ({day} days later)"
        if day == 1:
            res += f", {day_of_week[day_index]} (next day)"
    else:
        if day != 0:
            res += " "

    if day_string not in day_of_week:
        if day == 0:
            res += ""
        elif day != 1:
            res += f"({day} days later)"
        elif day == 1:
            res += "(next day)"

    return res


print(add_time("11:55 AM", "3:12"))

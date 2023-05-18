def add_time(initial_hour: str, difference: str, initial_day: str = ""):
    hour_difference = int(difference.split(":")[0])
    minute_difference = int(difference.split(":")[1])
    

    days_passed = hour_difference // 24
    hours_passed = hour_difference % 24

    hour_initial = int(initial_hour.split(":")[0])
    minute_initial = int(initial_hour.split(":")[1].split(" ")[0])
    am_pm_initial = initial_hour.split(":")[1].split(" ")[1]

    final_minute = str((minute_initial + minute_difference) % 60)

    if len(final_minute) == 1:
        final_minute = '0' + final_minute

    final_hour = ((minute_initial + minute_difference) // 60 + hours_passed + hour_initial) % 12
    flip_am_pm = (((minute_initial + minute_difference) // 60 + hours_passed + hour_initial) // 12) % 2
    final_am_pm: str = ""

    if am_pm_initial == 'AM' and flip_am_pm == 1:
        final_am_pm = "PM"

    elif am_pm_initial == "PM" and flip_am_pm == 1:
        final_am_pm = "AM"
        days_passed += 1

    else:
        final_am_pm = am_pm_initial

    if final_hour == 0:
        final_hour += 12

    new_time = f"{final_hour}:{final_minute} {final_am_pm}"
    
    if initial_day != "":
        week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        final_day: int
        
        for i in range(7):
            if initial_day.upper() == week_days[i].upper():
                final_day = i + days_passed
                
                if final_day > 6:
                    final_day = final_day % 7
        
        new_time += f", {week_days[final_day]}"

    if days_passed == 1:
        new_time += " (next day)"
    if days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
def add_time(initial_hour: str, difference: str, initial_day: str = ""):
    hour_difference = int(difference.split(":")[0])
    minute_difference = int(difference.split(":")[1])

    days_passed = hour_difference // 24

    hour_initial = int(initial_hour.split(":")[0])
    minute_initial = int(initial_hour.split(":")[1])
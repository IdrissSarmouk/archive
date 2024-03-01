def add_time(start_time, duration, day=None):
    # Days of the week
    week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    # Split the start time
    parts = start_time.split()
    if len(parts) == 2:
        start_time_hr, start_time_mn = map(int, parts[0].split(':'))
        start_time_period = parts[1].strip().lower()
    elif len(parts) == 1:
        start_time_hr, start_time_mn = map(int, parts[0].split(':'))
        start_time_period = 'am'  # Assume "AM" if not specified

    # Convert time to 24-hour format
    if start_time_period == 'pm' and start_time_hr != 12:
        start_time_hr += 12
    elif start_time_period == 'am' and start_time_hr == 12:
        start_time_hr = 0

    # Parse the duration
    duration_hr, duration_mn = map(int, duration.split(':'))
    no_of_days = duration_hr // 24
    duration_hr %= 24

    # Calculate the result time
    result_hr = start_time_hr + duration_hr
    result_mn = start_time_mn + duration_mn

    # Adjust result time if minutes exceed 60
    if result_mn >= 60:
        result_hr += 1
        result_mn %= 60

    # Calculate AM/PM and adjust hours
    am_pm = 'AM' if 0 <= result_hr < 12 else 'PM'
    result_hr %= 12
    if result_hr == 0:
        result_hr = 12

    # Calculate the number of days and message
    if start_time_period == 'pm' and am_pm == 'AM':
        no_of_days += 1

    message = None
    if no_of_days == 1:
        message = '(next day)'
    elif no_of_days > 1:
        message = f'({no_of_days} days later)'

    # Calculate the new day
    if day is not None:
        day = day.lower()
        day_no = (week.index(day) + no_of_days) % 7
        result_day = week[day_no].capitalize()
    else:
        result_day = ''

    # Create the final result
    final_result = [f'{result_hr}:{result_mn:02d} {am_pm}']
    if result_day:
        final_result.append(f', {result_day}')
    if message:
        final_result.append(f' {message}')

    return ''.join(final_result)

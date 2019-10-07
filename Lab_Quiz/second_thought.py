def second_thought(secs):
    rem_secs = secs%60
    mins = secs//60
    rem_mins = mins%60
    hours = mins//60
    return (hours,rem_mins,rem_secs)

secs = int(input('Input total seconds: '))
hours,rem_mins,rem_secs  = second_thought(secs)
print(f'{secs} equals {hours} hours(s) {rem_mins} minutes and {rem_secs} second(s)')

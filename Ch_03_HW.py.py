# Define minutes in an hour
minutes_in_hour = 60
# get user input for average speed, speed limit, and distance traveled
average_speed = float(input('enter the average speed (mph): '))
speed_limit = float(input('enter the speed limit (mph): '))
distance = float(input('enter the distance traveled (miles): '))

# check if average speed is greater than the speed limit
if average_speed > speed_limit:
    # calculate the time taken at average speed and speed limit
    time_at_avg_speed = distance / average_speed
    time_at_speed_limit = distance / speed_limit

    # calculate the time saved in hours
    time_saved_hours = time_at_speed_limit - time_at_avg_speed

    # convert time saved to minutes from hours
    time_saved_minutes = time_saved_hours * minutes_in_hour

    # display time saved in minutes
    print(f'you saved {time_saved_minutes:.2f} minutes\n'
          f'by traveling at {average_speed} mph\n'
          f'instead of {speed_limit} mph.')
else:
    print(f'no time saved, \n'
          f'your average speed of {average_speed} mph\n'
          f'is not above the {speed_limit} mph speed limit.')
    

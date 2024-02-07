from datetime import datetime, timedelta

# Get the current datetime object
now = datetime.now()

# Define a list of strings to convert
s_list = ['1h 36m ago', '2h 15m ago', '3h 45m ago']

# Define an empty list to store the time objects
time_list = []

# Loop through the strings in the list
for s in s_list:
    # Parse the string and extract the hours and minutes
    h, m = map(int, [s.split('h')[0], s.split('h')[1].replace('m ago', '')])
    # Subtract the hours and minutes from the current datetime
    time_object = now - timedelta(hours=h, minutes=m)
    # Append the time object to the list
    time_list.append(time_object)

# Define the format for the output
output_format = '%Y-%m-%d %H:%M:%S'

# Print the list of time objects in the desired format
print([dt.strftime(output_format) for dt in time_list])

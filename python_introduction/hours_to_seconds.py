############################################################################

seconds = 60
minutes = 60

# Calculate the number of seconds in one hour
second_per_hour = seconds * minutes


hours = 2 # Number of hours to convert to seconds

seconds = hours * second_per_hour

# Using f-strings to dynamically update the output when changing 'hours'
print(f'{hours} hour(s) is {seconds} seconds')

############################################################################
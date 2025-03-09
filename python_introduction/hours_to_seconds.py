############################################################################

seconds = 60
minutes = 60


second_per_hour = seconds * minutes

# Number of hours to convert to seconds
hours = 2

seconds = hours * second_per_hour

print(f'{hours} hour(s) is {seconds} seconds')

############################################################################

# Another simple way to calculate seconds in an hour
hours = 2

seconds = hours * 3600

# Using f-strings to dynamically update the output when changing 'hours'
print(f'{hours} hour(s) is {seconds} seconds')

############################################################################
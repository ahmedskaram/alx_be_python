from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')
display_current_datetime()

def calculate_future_date():
    number_of_days = int(input('Ent number of days (as an integer): '))
    current_date = datetime.datetime.now()
    future_date  = current_date + datetime.timedelta(days=number_of_days)
    print(f'Future date: {future_date}.strftime("%Y-%m-%d")')
calculate_future_date()

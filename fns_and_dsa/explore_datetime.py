from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f'Current date and time: {current_date.strftime("%d-%m-%Y %H:%M:%S")}')
    return current_date.strftime("%d-%m-%Y %H:%M:%S")

#display_current_datetime()


def calculate_future_date():
    current_date = display_current_datetime()
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    future_date = datetime.strptime(current_date, "%d-%m-%Y %H:%M:%S") + timedelta(days=number_of_days)
    print(f'future date {future_date.strftime("%d-%m-%Y")}')
    

calculate_future_date() 
    

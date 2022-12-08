from datetime import date

def time_stamp():
    today = date.today()
    today = str(today).split("-")
    today = today[1]+today[2]+today[0]
    return today

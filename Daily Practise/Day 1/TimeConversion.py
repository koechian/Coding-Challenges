from datetime import datetime


def timeConversion(s):
    t = datetime.strptime(s, "%I:%M:%S%p")
    # Format the datetime object into a 24-hour time string
    print(t.strftime("%H:%M:%S"))


timeConversion("07:05:45PM")

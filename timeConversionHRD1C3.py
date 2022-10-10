def timeConversion(s):
    if "PM" in s:
        hour = s[0:2]

        hour = int(hour)

        if hour != 12:
            hour +=12

        s = str(hour) + s[2:len(s)-2]
        print(s)
        return s

    if "AM" in s:
        hour = s[0:2]
        hour = int(hour)
        if hour ==12:
            hour = hour - 12

        s = str(hour).zfill(2) + s[2:len(s)-2]
        return s


if __name__ == '__main__':

    timeConversion("07:45:54PM")

    #timeConversion("01:01:00AM")
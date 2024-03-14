def main():
    time = input("What time is it? (##:##):  ")
    converted_time = convert(time)
    if converted_time >= 7 and converted_time <= 8: 
        print("Breakfast")
    elif converted_time >= 12 and converted_time <= 13:
        print("Lunch")
    elif converted_time >= 18 and converted_time <= 19:
        print("Dinner")
    else: 
        pass



def convert(time):

    time = time.replace(":", '.')
    hours, minutes = time.split('.')
    minutes, time = minutes.split(" ")
    hours = float(hours)
    minutes = float(minutes)
    if "am" in time:

        minutes = minutes / 60
        AM  = hours + minutes 
        return AM
    if "pm" in time:
        if hours == 12:
            return hours + minutes
        else:

            PM  = (hours + minutes) + 12 
        return PM


if __name__ == "__main__":
    main()
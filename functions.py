ages = 23

def counting():
    if ages < 25:
        print("old")
    else:
        print("heelo")
        


hours = [30,44,43,50,22,22,30,44,48]

most_hours = []

def practice():
    for i in hours:
        if hours.count(i) > 1:
            most_hours.append(i)
    print(most_hours)
practice()  
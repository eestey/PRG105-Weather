weather = {'January': '50', 'February': '52', 'March': '54', 'April': '57', 'May': '63', 'June': '70', 'July': '75', 'August': '75', 'September': '72', 'October': '64', 'November': '57', 'December': '54'}


# Variables
average = 0
high = dict()


def avg(month):
    global average 
    total = 0
    for temp in month:
        total += int(month[temp])
    average = total / len(weather)
    print(" The average temperature for Monte Carlo this year was: " + str(avg))


def over(today):
    global average
    for be in today:
        if today[be] > average:
            high[be] = (today[be])
    print high


avg(weather)
over(weather)

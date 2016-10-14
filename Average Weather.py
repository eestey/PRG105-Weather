weather = {'January': '50', 'February': '52', 'March': '54', 'April': '57', 'May': '63', 'June': '70', 'July': '75', 'August': '75', 'September': '72', 'October': '64', 'November': '57', 'December': '54'}
print weather

# Variables
avg_temp = 75
high = dict()


def avg_temp(month):
    total = 0
    for temp in month:
        total += month[temp]
    avg = total / len(weather)
    print(" The average temperature for Monte Carlo this year was: " + str(avg))


def over(today):
    global top_range
    for be in today:
        if today[be] > top_range:
            high[be] = (today[be])
    print high


avg_temp(weather)
over(weather)

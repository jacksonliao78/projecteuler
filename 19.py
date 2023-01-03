
import math

#we use zellers to find the dow

#q -> day of the month, y -> year, m -> month
def day_of_week(y, m, q):
    K = y % 100
    J = y // 100

    m = [13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12][m]

    return(q + math.floor(13 * (m + 1) / 5) + K + math.floor(K / 4) + math.floor(J / 4) - 2 * J)


def sundays_on_first(start, end):
    count, dow = 0, 2
    for i in range(start, end + 1):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
            days[1] = 29
        for j in range(0, 12):
            if dow % 7 == 0:
                count += 1
            dow += days[j]
    return count

print(sundays_on_first(1901, 2000))
    
        



from random import random
from math import sqrt

def estimate_pi(precision):
    nHits = 0
    nTotal = 1000
    for i in range(nTotal):
        # generates coordinates for x and y in the circle/square
        x = random()
        y = random()
        #print(x, " ", y) test to see if coordinates are generated correctly
        #centre of circle is coordinate (0.5,0.5), so if the distance is greater than the radius

        if (x - 0.5) < 0: #ensures the difference in coordinates is positive, so no error when sqrt
            x_difference = 0.5 - x
        else:
            x_difference = x - 0.5
        if (y - 0.5) < 0:
            y_difference = 0.5 - y
        else:
            y_difference = y - 0.5
        #if distance between two points > 0.5, it is out of circle and in the square
        if sqrt((x_difference**2)+(y_difference**2)) <= 0.5:
            #inside circle
            nHits += 1
    #print(nHits) test for nHits to be less than total
    #rounds pi to the asked amount of decimal places
    pi_approx = round((4*nHits)/nTotal,precision)
    return pi_approx


precision = int(input("Enter the precision you wish to have for the pi approximation "))
pi = estimate_pi(precision)
print("Pi approximation is ",pi)

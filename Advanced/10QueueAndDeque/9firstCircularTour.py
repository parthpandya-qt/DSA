def firstCircularTour(petrol, distance):
    start = 0
    currFuel = 0
    totalFuel = 0

    for i in range(len(petrol)):
        gain = petrol[i] - distance[i]

        currFuel += gain
        totalFuel += gain

        if currFuel < 0:
            start = i + 1
            currFuel = 0

    if totalFuel < 0:
        return -1

    return start
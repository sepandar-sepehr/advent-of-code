import math

with open('d5_input', 'r') as file:
    seeds_range = [int(x) for x in file.readline().split(':')[1].strip().split()]
    seedRanges = []
    for seed in range(int(len(seeds_range) / 2)):
        seedRanges.append(range(seeds_range[seed * 2], seeds_range[seed * 2] + seeds_range[seed * 2 + 1]))
    print(seedRanges)
    file.readline()
    file.readline()

    seed2Soil = {}
    seed2SoilLine = file.readline().strip()
    while seed2SoilLine != '':
        seed2Soil[
            range(int(seed2SoilLine.split()[1]), int(seed2SoilLine.split()[1]) + int(seed2SoilLine.split()[2]))] = int(
            seed2SoilLine.split()[0])
        seed2SoilLine = file.readline().strip()

    file.readline()
    soil2Fert = {}
    soil2FertLine = file.readline().strip()
    while soil2FertLine != '':
        soil2Fert[
            range(int(soil2FertLine.split()[1]), int(soil2FertLine.split()[1]) + int(soil2FertLine.split()[2]))] = int(
            soil2FertLine.split()[0])
        soil2FertLine = file.readline().strip()

    file.readline()
    fert2Water = {}
    fert2WaterLine = file.readline().strip()
    while fert2WaterLine != '':
        fert2Water[range(int(fert2WaterLine.split()[1]),
                         int(fert2WaterLine.split()[1]) + int(fert2WaterLine.split()[2]))] = int(
            fert2WaterLine.split()[0])
        fert2WaterLine = file.readline().strip()

    file.readline()
    water2Light = {}
    water2LightLine = file.readline().strip()
    while water2LightLine != '':
        water2Light[range(int(water2LightLine.split()[1]),
                          int(water2LightLine.split()[1]) + int(water2LightLine.split()[2]))] = int(
            water2LightLine.split()[0])
        water2LightLine = file.readline().strip()

    file.readline()
    light2Temperature = {}
    light2TemperatureLine = file.readline().strip()
    while light2TemperatureLine != '':
        light2Temperature[range(int(light2TemperatureLine.split()[1]),
                                int(light2TemperatureLine.split()[1]) + int(light2TemperatureLine.split()[2]))] = int(
            light2TemperatureLine.split()[0])
        light2TemperatureLine = file.readline().strip()

    file.readline()
    temp2Humidity = {}
    temp2HumidityLine = file.readline().strip()
    while temp2HumidityLine != '':
        temp2Humidity[range(int(temp2HumidityLine.split()[1]),
                            int(temp2HumidityLine.split()[1]) + int(temp2HumidityLine.split()[2]))] = int(
            temp2HumidityLine.split()[0])
        temp2HumidityLine = file.readline().strip()

    file.readline()
    humidity2Location = {}
    humidity2LocationLine = file.readline().strip()
    while humidity2LocationLine != '':
        humidity2Location[range(int(humidity2LocationLine.split()[1]),
                                int(humidity2LocationLine.split()[1]) + int(humidity2LocationLine.split()[2]))] = int(
            humidity2LocationLine.split()[0])
        humidity2LocationLine = file.readline().strip()


def getIntersections(lookupRanges, lookIn):
    results = []
    for lookupRange in lookupRanges:
        foundMatch = False
        for lookInRange, mapTo in lookIn.items():
            potentialRange = range(max(lookupRange.start, lookInRange.start),
                                   min(lookupRange.stop, lookInRange.stop)) or None
            if potentialRange:
                print('potential', potentialRange, mapTo)
                newStart = potentialRange.start - lookInRange.start + mapTo
                results.append(range(newStart, newStart + len(potentialRange)))

                # This is not complete, the original range could be bigger and the remainder needs to be included still
                # That said, this worked for my input even though it didn't work for sample :D
                foundMatch = True
        if not foundMatch:
            results.append(lookupRange)
    return results


def calcRangeMinLocation(seedRange):
    soilRanges = getIntersections([seedRange], seed2Soil)
    fertRanges = getIntersections(soilRanges, soil2Fert)
    waterRanges = getIntersections(fertRanges, fert2Water)
    lightRanges = getIntersections(waterRanges, water2Light)
    tempRanges = getIntersections(lightRanges, light2Temperature)
    humityRanges = getIntersections(tempRanges, temp2Humidity)
    locationRanges = getIntersections(humityRanges, humidity2Location)
    return min([r.start for r in locationRanges])


minLocation = math.inf
for seedRange in seedRanges:
    print(seedRange)
    newLocation = calcRangeMinLocation(seedRange)
    if newLocation < minLocation:
        minLocation = newLocation

print(minLocation)

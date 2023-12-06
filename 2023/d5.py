with open('d5_input', 'r') as file:
    seeds = [int(x) for x in file.readline().split(':')[1].strip().split()]
    print(seeds)
    file.readline()
    file.readline()

    seed2Soil = {}
    seed2SoilLine = file.readline().strip()
    while(seed2SoilLine != ''):
        seed2Soil[int(seed2SoilLine.split()[1])] = (int(seed2SoilLine.split()[0]), int(seed2SoilLine.split()[2]))
        seed2SoilLine = file.readline().strip()

    print(seed2Soil)
    file.readline()
    soil2Fert = {}
    soil2FertLine = file.readline().strip()
    while(soil2FertLine != ''):
        soil2Fert[int(soil2FertLine.split()[1])] = (int(soil2FertLine.split()[0]), int(soil2FertLine.split()[2]))
        soil2FertLine = file.readline().strip()

    file.readline()
    fert2Water = {}
    fert2WaterLine = file.readline().strip()
    while(fert2WaterLine != ''):
        fert2Water[int(fert2WaterLine.split()[1])] = (int(fert2WaterLine.split()[0]), int(fert2WaterLine.split()[2]))
        fert2WaterLine = file.readline().strip()

    file.readline()
    water2Light = {}
    water2LightLine = file.readline().strip()
    while(water2LightLine != ''):
        water2Light[int(water2LightLine.split()[1])] = (int(water2LightLine.split()[0]), int(water2LightLine.split()[2]))
        water2LightLine = file.readline().strip()

    file.readline()
    light2Temperature = {}
    light2TemperatureLine = file.readline().strip()
    while (light2TemperatureLine != ''):
        light2Temperature[int(light2TemperatureLine.split()[1])] = (int(light2TemperatureLine.split()[0]), int(light2TemperatureLine.split()[2]))
        light2TemperatureLine = file.readline().strip()

    print(light2Temperature)
    file.readline()
    temp2Humidity = {}
    temp2HumidityLine = file.readline().strip()
    while (temp2HumidityLine != ''):
        temp2Humidity[int(temp2HumidityLine.split()[1])] = (int(temp2HumidityLine.split()[0]), int(temp2HumidityLine.split()[2]))
        temp2HumidityLine = file.readline().strip()

    file.readline()
    humidity2Location = {}
    humidity2LocationLine = file.readline().strip()
    while (humidity2LocationLine != ''):
        humidity2Location[int(humidity2LocationLine.split()[1])] = (int(humidity2LocationLine.split()[0]), int(humidity2LocationLine.split()[2]))
        humidity2LocationLine = file.readline().strip()

def getMapVal(lookupDict, val):
    for k, v in lookupDict.items():
        if (val in range(k, k+v[1])):
            offset = val-k
            return v[0] + offset
    return val
def calcLocation(seed):
    soil = getMapVal(seed2Soil, seed)
    fert = getMapVal(soil2Fert, soil)
    water = getMapVal(fert2Water, fert)
    light = getMapVal(water2Light, water)
    temp = getMapVal(light2Temperature, light)
    humidity = getMapVal(temp2Humidity, temp)
    return getMapVal(humidity2Location, humidity)

locations = []
for seed in seeds:
    locations.append(calcLocation(seed))
    print(locations)
print(min(locations))
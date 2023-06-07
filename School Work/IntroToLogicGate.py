turbineSpeed = int(input("give me turbine speed"))
bearingTemperature = int(input("give me bearing temperature"))
windSpeed = int(input("give me wind speed"))

S = turbineSpeed > 1000
T = bearingTemperature > 80
W = windSpeed > 120
X = (not S and T) or (S and W) or (not T and W)

print(X)

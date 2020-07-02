from e6b import e6b

#Simple unit tests

#Degrees
windSpeed = 10
windBearing = 90
trueAirSpeed = 15
desiredBearing = 180

correctedBearing,correction = e6b.getCorrectedBearing(windSpeed,windBearing,trueAirSpeed,desiredBearing)
groundSpeed = e6b.getGroundSpeed(windSpeed,windBearing,trueAirSpeed,desiredBearing,correction)

print("In degrees:")
print(f"Bearing: {correctedBearing} degrees\nGround Speed: {groundSpeed}")


#Radians
windSpeed = 10
windBearing = 1.5708
trueAirSpeed = 15
desiredBearing = 3.14159

correctedBearing,correction = e6b.getCorrectedBearing(windSpeed,windBearing,trueAirSpeed,desiredBearing,True)
groundSpeed = e6b.getGroundSpeed(windSpeed,windBearing,trueAirSpeed,desiredBearing,correction,True)

print("\nIn radians:")
print(f"Bearing: {correctedBearing} degrees\nGround Speed: {groundSpeed}")

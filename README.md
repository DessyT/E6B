# E6B
Simple python project to perform E6B flight calculations

## Installation
```bash
$ pip install e6b
```

## Usage

### Calculate required flight bearing and final ground speed
```python
from e6b import e6b

windSpeed = 10
windBearing = 90
trueAirSpeed = 15
desiredBearing = 180

correctedBearing,correction = getCorrectedBearing(windSpeed,windBearing,trueAirSpeed,desiredBearing)
groundSpeed = getGroundSpeed(windSpeed,windBearing,trueAirSpeed,desiredBearing,correction)

print(correctedBearing)
>>  138.18968510422138
print(groundSpeed)
>>  11.180339887498947
```

### Using radians instead of degrees

```python
from e6b import e6b

windSpeed = 10
windBearing = 1.5708
trueAirSpeed = 15
desiredBearing = 3.14159

correctedBearing,correction = getCorrectedBearing(windSpeed,windBearing,trueAirSpeed,desiredBearing,True)
groundSpeed = getGroundSpeed(windSpeed,windBearing,trueAirSpeed,desiredBearing,correction,True)

print(correctedBearing)
>>  2.4118623437909346
print(groundSpeed)
>>  11.180276619728994
```

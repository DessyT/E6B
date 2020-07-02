#Simulates the E6B flight calculator

import math as m

def getCorrectedBearing(windSpeed,windBearing,trueAirspeed,desiredBearing,radians=False):

    """
    Calculate the wind correction angle

    :param windSpeed:           Speed of the wind
    :param windBearing:         Bearing of the wind
    :param trueAirspeed:        The flight speed of the aircraft
    :param desiredBearing:      The desired flight bearing
    :param radians:             Desired unit - radians or degrees. Default is degrees

    :return correctedBearing:   The required flight bearing when accounting for wind
    :return correction:         The amount of correction required from desiredBearing
    """

    if radians == False:
        #Convert to rads
        windBearing,desiredBearing = m.radians(windBearing),m.radians(desiredBearing)

    #Calculate difference of bearing required
    correction = m.asin(windSpeed * m.sin(windBearing - desiredBearing) / trueAirspeed)

    #Get the actual angle
    correctedBearing = desiredBearing + correction

    if radians == False:
        #Convert degrees and return
        return m.degrees(correctedBearing),m.degrees(correction)
    else:
        #Return as radians
        return correctedBearing,correction

def getGroundSpeed(windSpeed,windBearing,trueAirspeed,desiredBearing,correction,radians=False):

    """
    Calculate the final ground speed
    :param windSpeed:           Speed of the wind
    :param windBearing:         Bearing of the wind
    :param trueAirspeed:        The flight speed of the aircraft
    :param desiredBearing:      The desired flight bearing
    :param correction:          The amount of correction required from desiredBearing
    :param radians:             Desired unit - radians or degrees. Default is degrees

    :return groundSpeed:        The flight speed when accounting for wind
    """

    if radians == False:
        #Convert to rads
        windBearing,desiredBearing,correction = m.radians(windBearing),m.radians(desiredBearing),m.radians(correction)

    #Calculate final ground speed
    groundSpeed = m.sqrt(m.pow(trueAirspeed,2) + m.pow(windSpeed,2) - 2 *
                        trueAirspeed * windSpeed * m.cos(desiredBearing - windBearing + correction))

    return groundSpeed

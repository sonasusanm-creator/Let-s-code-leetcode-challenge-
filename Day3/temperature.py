class Solution(object):
    def convertTemperature(self,celcius):
        kelvin=celcius+273.15
        fahrenheit=celcius*1.80+32.0
        return[kelvin,fahrenheit]

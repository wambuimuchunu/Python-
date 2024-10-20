class Temperature:
    def convertfahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
    
    def convertcelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")


temp = Temperature()
temp.convertfahrenheit(35)   
temp.convertcelsius(40) 

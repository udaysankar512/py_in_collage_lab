# Q.3. Write a program that converts a list of temperatures in Fahrenheit
# degrees to their equivalent Celsius degrees using list comprehension.

fahrenheit = [32, 68, 86, 104, 122]
celsius = [(temp - 32) * 5 / 9 for temp in fahrenheit]  #Formula : (0°C × 9/5) + 32 = 32°F  
                                                        # (Fahrenheit - 32) × 5 ÷ 9 = Celsius


print("Fahrenheit:", fahrenheit)
print("Celsius:", celsius)

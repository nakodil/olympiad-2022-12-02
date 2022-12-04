doors_sec = int(input())
wheels_min = int(input())
seats_hr = int(input())

doors = int(input())
wheels = int(input())
seats = int(input())

doors_day = doors_sec * 60 * 60 * 24
wheels_day = wheels_min * 60 * 24
seats_day = seats_hr * 24

result = [doors_day / doors, wheels_day / wheels, seats_day / seats]
print(int(min(result)))

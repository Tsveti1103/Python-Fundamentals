number_of_snowballs = int(input())
snowball_value = 0
snowball_quality = 0
snowball_weight = 0
snowball_time = 0
for i in range(number_of_snowballs):
    current_snowball_weight = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())
    current_snowball_value = int(pow(current_snowball_weight / current_snowball_time, current_snowball_quality))
    if current_snowball_value > snowball_value:
        snowball_value = current_snowball_value
        snowball_quality = current_snowball_quality
        snowball_weight = current_snowball_weight
        snowball_time = current_snowball_time
print(f"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})")

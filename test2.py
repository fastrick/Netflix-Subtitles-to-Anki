n1 = 7
number_list = [3, 9, 12, 5, 18]

closest_number = None
minimum_difference = float('inf')

for num in number_list:
    difference = abs(n1 - num)
    if difference < minimum_difference:
        minimum_difference = difference
        closest_number = num

print("Closest Number:", closest_number)

import re

def round_timestamp(timestamp):
    # Extract the numerical value from the timestamp
    value = int(re.search(r'\d+', timestamp).group())

    # Round the value to the nearest ten
    rounded_value = round(value, -1)

    # Replace the numerical value in the timestamp with the rounded value
    rounded_timestamp = re.sub(r'\d+', str(rounded_value), timestamp)
    print("Rounded timestamp: " + rounded_timestamp)
    return rounded_timestamp

# Example inputs
begin1 = "708624582t"
end1 = "725307916t"
begin2 = "707373332t"
end2 = "724056666t"

# Round the begin and end timestamps
rounded_begin1 = round_timestamp(begin1[:-1])
rounded_end1 = round_timestamp(end1[:-1])
rounded_begin2 = round_timestamp(begin2[:-1])
rounded_end2 = round_timestamp(end2[:-1])
print("Rounded begin1: " + rounded_begin1)
print("Rounded end1: " + rounded_end1)
print("Rounded begin2: " + rounded_begin2)
print("Rounded end2: " + rounded_end2)


# Check if the rounded timestamps match
if rounded_begin1 == rounded_begin2 and rounded_end1 == rounded_end2:
    print("Timestamps match with rounding.")
else:
    print("Timestamps do not match.")

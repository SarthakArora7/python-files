weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
weather_f = {key: ((temp_c*9/5) + 32) for (key, temp_c) in weather_c.items()}

print(weather_f)



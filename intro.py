# Create a list with specified elements
my_list = [
    [1, 2, 3],           # First element is a list of integers
    [0.1, 0.2, 0.3],     # Second element is a list of floats
    "Hello, World!",     # Third element is a string
    ["apple", "banana", "cherry"]  # Fourth element is a list of strings
]

# # Convert the third element (string) into a list and add another string to it
# my_list[2] = [my_list[2], "New String"]

# # Print the modified list
# print(my_list)

# my_dict={"cs":"Weir Hall",
#          "j":"Farley Hall",
#          "CE":"Carrier Hall"}

# del my_dict["CE"]
# print(my_dict)

# Create the 'countries' dictionary with nested data
# Create the 'countries' dictionary
countries = {
    'USA': {
        'Name': 'United States of America',
        'Population (million)': 325,
        'Capital': 'Washington D.C.'
    },
    'BGD': {
        'Name': 'Bangladesh',
        'Population (million)': 164,
        'Capital': 'Dhaka'
    },
    'IND': {
        'Name': 'India',
        'Population (million)': 1339,
        'Capital': 'New Delhi'
    },
    'PER': {
        'Name': 'Peru',
        'Population (million)': 32,
        'Capital': 'Lima'
    }
}

# Print the keys of the dictionary
country_keys = list(countries.keys())
print("Keys of the 'countries' dictionary:")
print(country_keys)

# Print the values of the dictionary
country_values = list(countries.values())
print("\nValues of the 'countries' dictionary:")
print(country_values)


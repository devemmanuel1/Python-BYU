# # Read the dataset
# data_list = []
# filename = 'life-expectancy.csv'

# with open(filename, 'r') as file:
#     for line_count, line in enumerate(file):
#         line = line.strip()
#         if line_count == 0:  # Skip the header line
#             continue
#         if line:
#             data = line.split(',')
#             country = data[0]
#             year = int(data[2])
#             life_exp = float(data[3])
#             data_list.append({'country': country, 'year': year, 'life_exp': life_exp})

# # Find the year and country with the lowest life expectancy
# lowest_exp = data_list[0]
# for data in data_list:
#     if data['life_exp'] < lowest_exp['life_exp']:
#         lowest_exp = data

# lowest_year = lowest_exp['year']
# lowest_country = lowest_exp['country']
# print("The year and country with the lowest life expectancy:", lowest_year, lowest_country)

# # Find the year and country with the highest life expectancy
# highest_exp = data_list[0]
# for data in data_list:
#     if data['life_exp'] > highest_exp['life_exp']:
#         highest_exp = data

# highest_year = highest_exp['year']
# highest_country = highest_exp['country']
# print("The year and country with the highest life expectancy:", highest_year, highest_country)

# # Allow the user to input a year
# year = float(input("Enter the year of interest: "))

# # Calculate the average life expectancy for the given year
# total_exp = 0
# count = 0

# for data in data_list:
#     if data['year'] == year:
#         total_exp += data['life_exp']
#         count += 1

# if count > 0:
#     average_exp = total_exp / count
#     print("The average life expectancy for", year, ":", average_exp)

#     # Find the country with the minimum and maximum life expectancies for the given year
#     min_country = None
#     max_country = None
#     min_exp = float('inf')
#     max_exp = float('-inf')

#     for data in data_list:
#         if data['year'] == year:
#             if data['life_exp'] < min_exp:
#                 min_exp = data['life_exp']
#                 min_country = data['country']
#             if data['life_exp'] > max_exp:
#                 max_exp = data['life_exp']
#                 max_country = data['country']

#     print("The country with the minimum life expectancy for", year, ":", min_country)
#     print("The country with the maximum life expectancy for", year, ":", max_country)
# else:
#     print("No data available for the given year.")


# Read the dataset
dataset = []
filename = 'life-expectancy.csv'

file = open(filename, 'r')
lines = file.readlines()
file.close()

for line_count in range(1, len(lines)):
    line = lines[line_count].strip()
    if line:
        data = line.split(',')
        country = data[0]
        year = int(data[2])
        life_expectancy = float(data[3])
        dataset.append({'country': country, 'year': year,
                       'life_expectancy': life_expectancy})

# Find the year and country with the lowest life expectancy
lowest_life_exp = dataset[0]
for data in dataset:
    if data['life_expectancy'] < lowest_life_exp['life_expectancy']:
        lowest_life_exp = data

# Find the year and country with the highest life expectancy
highest_life_exp = dataset[0]
for data in dataset:
    if data['life_expectancy'] > highest_life_exp['life_expectancy']:
        highest_life_exp = data

print("The highest life expectancy:", highest_life_exp)

lowest_year = lowest_life_exp['year']
lowest_country = lowest_life_exp['country']
print("The year and country with the lowest life expectancy:",
      lowest_country, lowest_year)

highest_year = highest_life_exp['year']
highest_country = highest_life_exp['country']
print("The year and country with the highest life expectancy:",
      highest_year, highest_country)

# Allow the user to input a year
year_of_interest = float(input("Enter the year of interest: "))

# Calculate the average life expectancy for the given year
total_life_exp = 0
count = 0

for data in dataset:
    if data['year'] == year_of_interest:
        total_life_exp += data['life_expectancy']
        count += 1

if count > 0:
    average_life_exp = total_life_exp / count
    print("The average life expectancy for",
          year_of_interest, ":", average_life_exp)

    # Find the country with the minimum and maximum life expectancies for the given year
    min_country = None
    max_country = None
    min_life_exp = float('inf')
    max_life_exp = float('-inf')

    for data in dataset:
        if data['year'] == year_of_interest:
            if data['life_expectancy'] < min_life_exp:
                min_life_exp = data['life_expectancy']
                min_country = data['country']
            if data['life_expectancy'] > max_life_exp:
                max_life_exp = data['life_expectancy']
                max_country = data['country']

    print("The country with the minimum life expectancy for",
          year_of_interest, ":", min_country)
    print("The country with the maximum life expectancy for",
          year_of_interest, ":", max_country)
else:
    print("No data available for the given year.")

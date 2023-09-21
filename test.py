# from PIL import Image
import pandas as pd
# data = pd.read_csv('data/items/info.txt', index_col='index')
# print(data)
# # image = Image.open('data/items/1.jpg')
# # image.show()
# data = {
#     1: {'age': 25, 'height': 170},
#     2: {'age': 30, 'height': 175},
#     3: {'age': 35, 'height': 180},
#     4: {'age': 40, 'height': 185},
#     5: {'age': 45, 'height': 190}
# }

# # Specify the file path where you want to save the text file
# file_path = 'data.txt'

# # Open the file in write mode
# with open(file_path, 'w') as file:
#     # Write the column headers
#     file.write('Index\tAge\tHeight\n')
    
#     # Write the data rows
#     for index, values in data.items():
#         file.write(f'{index}\t{values["age"]}\t{values["height"]}\n')

# print(f'The data has been saved to {file_path}.')
import pandas as pd

data = {
    1: {'age': 25, 'height': 170},
    2: {'age': 30, 'height': 175},
    3: {'age': 35, 'height': 180},
    4: {'age': 40, 'height': 185},
    5: {'age': 45, 'height': 190}
}

# Specify the file path where you want to save the text file
file_path = 'data.csv'

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write the column headers
    file.write('Index,Age,Height\n')
    
    # Write the data rows
    for index, values in data.items():
        file.write(f'{index},{values["age"]},{values["height"]}\n')

print(f'The data has been saved to {file_path}.')

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame
print(df)


import os
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(
    '/Users/guntar/Documents/pythonapp/renameFolder/Rename Folder Blitar.csv')

# Iterate over the rows in the DataFrame
for index, row in df.iterrows():
    if 'Folder Lama' in row:
        old_folder_name = row['Folder Lama']
    else:
        print("Key 'Folder Lama' does not exist in row")
        continue  # Skip the rest of this loop iteration

    new_folder_name = row['Folder Baru']

    old_folder_path = os.path.join('/Users/guntar/Documents/pythonapp/renameFolder/ALL DATA SCAN BLITAR', old_folder_name)
    new_folder_path = os.path.join('/Users/guntar/Documents/pythonapp/renameFolder/ALL DATA SCAN BLITAR', new_folder_name)

    # Check if the old folder exists
    if os.path.exists(old_folder_path):
        # Rename the folder
        os.rename(old_folder_path, new_folder_path)
        print(f'Successfully renamed folder {old_folder_name} to {new_folder_name}')
    else:
        print(f'Folder {old_folder_name} not found')
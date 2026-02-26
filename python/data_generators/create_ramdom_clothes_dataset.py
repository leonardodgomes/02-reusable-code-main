import pandas as pd
import random
import string
import os
from datetime import datetime, timedelta

def get_path():
    # Get the absolute path of the script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    current_directory = current_directory.replace('\\', '/') + '/'

    print('Path - OK!')
    print('  Full Path   :' + current_directory)

    return current_directory


def create_dataset(num_rows):
    # Define the categories, seasons, and locations
    categories = {
                'Spring': ['T-shirt', 'Jeans', 'Dress', 'Sweater', 'Skirt', 'Coat'],
                'Summer': ['T-shirt', 'Jeans', 'Dress', 'Sweater', 'Skirt'],
                'Autumn': ['T-shirt', 'Jeans', 'Dress', 'Sweater', 'Skirt', 'Coat'],
                'Winter': ['T-shirt', 'Jeans', 'Dress', 'Sweater', 'Skirt', 'Coat', 'Sweater', 'Sweater']
                }

    seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
    locations = ['Lisbon', 'Porto', 'Faro', 'Coimbra', 'Braga']

    # Create an empty DataFrame
    data = pd.DataFrame()

    # Create an empty DataFrame
    data = pd.DataFrame()

    # Generate random data
    for _ in range(num_rows):
        item_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        price = random.uniform(10, 100)
        season = random.choice(seasons)
        category = random.choice(categories[season])
        location = random.choice(locations)
        sale_date = datetime.now() - timedelta(days=random.randint(1, 30))
        
        row = {'Item ID': item_id, 'Price': price, 'Category': category, 'Season': season, 'Location': location, 'Sale Date': sale_date}
        data = pd.concat([data, pd.DataFrame(row, index=[0])], ignore_index=True)



    return data

def export_csv(dt_frame, path, type):
    
    if type == 'Trainning':    
        csv_name = 'generated_data_'+ type + '.csv'
        print('Final file: ' + csv_name)
        dt_frame.to_csv(path + csv_name, index=False)# Export the DataFrame to CSV file
    else:
        csv_name = 'generated_data_'+ type + '.csv'
        print('Final file: ' + csv_name)
        dt_frame.to_csv(path + csv_name, index=False)# Export the DataFrame to CSV file

    
    

    print("CSV file generated successfully.")


def main():
    #Call the function to get the path to the script
    path_complete = get_path()
     
    #Create the dataset for Trainning
    dataframe = create_dataset(2000)
    #Export the dataset to a CSV file
    export_csv(dataframe,path_complete,'trainning')


    #Create the 'real' dataset 
    dataframe = create_dataset(66589)
    #Export the dataset to a CSV file
    export_csv(dataframe,path_complete,'real')

if __name__ == '__main__':
    main()

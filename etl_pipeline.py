import requests
import pandas as pd
from sqlalchemy import create_engine

def get_data() -> list:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("API error: " + str(response.status_code))

if __name__ == "__main__":
    
    # Extract and load data into DataFrame
    df = pd.DataFrame(get_data())
    print("Columns:", df.columns)
    
    # Transform data
    df_transformed = df[['id', 'name', 'email', 'address']].copy()
    df_transformed['city'] = df_transformed['address'].apply(lambda x: x.get('city'))
    df_transformed.drop('address', axis=1, inplace=True)

    # Load data into SQLite database
    engine = create_engine('sqlite:///etl_example.db', echo=True)
    df_transformed.to_sql('users', con=engine, if_exists='replace', index=False)

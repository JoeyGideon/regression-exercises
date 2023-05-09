import pandas as pd
from env import host, username, password
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
def get_zillow_data():
    """
    This function connects to the zillow database and retrieves data from the properties_2017 table for
    all 'Single Family Residential' properties. The resulting DataFrame contains the bedroomcnt, bathroomcnt,
    calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, and fips columns and is returned by
    the function.
    """
   
    # create the connection url
    url = f'mysql+pymysql://{username}:{password}@{host}/zillow'

    # read the SQL query into a DataFrame
    query = '''
            SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
            FROM properties_2017
            WHERE propertylandusetypeid = 261
            '''
    df = pd.read_sql(query, url)

    return df



# function to read from csv file
def read_csv_file():
    df = pd.read_csv('zillow_data.csv')
    return df


from sklearn.preprocessing import MinMaxScaler




def prep_zillow(df):
    """
    This function takes in the Zillow DataFrame and does the following:
    - Drops any rows with missing values
    - Returns the cleaned DataFrame
    """
    
    # Drop any rows with missing values
    df.dropna(inplace=True)
    
    # Separate the numerical columns from the categorical columns
    num_cols = ['bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet', 'taxvaluedollarcnt', 'yearbuilt', 'taxamount']
    cat_cols = ['fips']
    num_df = df[num_cols]
    cat_df = df[cat_cols]
    
    # Combine the numerical columns and categorical columns
    cleaned_df = pd.concat([num_df, cat_df], axis=1)
    
    # Return the cleaned DataFrame
    return cleaned_df



def split_data(df):
    """
    This function takes in the cleaned and scaled DataFrame and does the following:
    - Splits the data into train, validate, and test sets (60/20/20 split)
    - Returns the train, validate, and test sets
    """
    
    # Split the data into train and test sets (80/20 split)
    train, test = train_test_split(df, test_size=0.2, random_state=123)
    
    # Split the train set into train and validate sets (75/25 split)
    train, validate = train_test_split(train, test_size=0.25, random_state=123)
    
    # Return the train, validate, and test sets
    return train, validate, test

def wrangle_zillow():
    """
    This function retrieves data from the Zillow database, prepares the data by dropping missing values and scaling
    the numerical columns using StandardScaler, and returns the cleaned and scaled DataFrame.
    """
    
    # Get the Zillow data
    df = get_zillow_data()
    
    # Prepare the Zillow data
    df_prep = prep_zillow(df)
    
    # Return the cleaned and scaled DataFrame
    return df_prep



def min_max_scaler(df):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df)
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns, index=df.index)
    return scaled_df


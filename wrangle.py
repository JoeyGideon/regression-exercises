import pandas as pd
from env import host, username, password
from sklearn.preprocessing import StandardScaler

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

def prep_zillow(df):
    """
    This function takes in the Zillow DataFrame and does the following:
    - Drops any rows with missing values
    - Scales the numerical columns using StandardScaler
    - Returns the cleaned and scaled DataFrame
    """
    
    # Drop any rows with missing values
    df.dropna(inplace=True)
    
    # Separate the numerical columns from the categorical columns
    num_cols = ['bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet', 'taxvaluedollarcnt', 'yearbuilt', 'taxamount']
    cat_cols = ['fips']
    num_df = df[num_cols]
    cat_df = df[cat_cols]
    
    # Scale the numerical columns using StandardScaler
    scaler = StandardScaler()
    num_df_scaled = pd.DataFrame(scaler.fit_transform(num_df), columns=num_cols, index=num_df.index)
    
    # Combine the scaled numerical columns and categorical columns
    cleaned_df = pd.concat([num_df_scaled, cat_df], axis=1)
    
    # Return the cleaned and scaled DataFrame
    return cleaned_df

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
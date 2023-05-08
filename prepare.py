import pandas as pd
from env import host, username, password
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


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
    
    # Split the data into train and test sets (80/20 split)
    train, test = train_test_split(df, test_size=0.2, random_state=123)
    
    # Learn the scaling parameters from the training data only
    scaler = StandardScaler()
    scaler.fit(train[num_cols])
    
    # Scale the numerical columns using the learned scaling parameters
    num_df_scaled = pd.DataFrame(scaler.transform(num_df), columns=num_cols, index=num_df.index)
    
    # Combine the scaled numerical columns and categorical columns
    cleaned_df = pd.concat([num_df_scaled, cat_df], axis=1)
    
    # Return the cleaned and scaled DataFrame
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

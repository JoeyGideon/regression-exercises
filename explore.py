import pandas as pd
from env import host, username, password
import prepare
import wrangle
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr, spearmanr

def plot_variable_pairs(df):
    sns.pairplot(df, kind="reg", diag_kind="kde")



def plot_categorical_and_continuous_vars(df, cat_col, cont_col, sample_size=1000):
    """
    Plots 3 different visualizations for the relationship between a categorical and continuous variable.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The dataframe to use for plotting.
        
    cat_col : str
        The name of the categorical column to plot.
        
    cont_col : str
        The name of the continuous column to plot.
        
    sample_size : int
        The number of rows to sample from the dataframe. Defaults to 100000.
    """
    # Take a random sample of the dataframe
    df = df.sample(n=sample_size, replace=False, random_state=42)
    
    # Plot a boxplot for the continuous variable by category
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=cat_col, y=cont_col, data=df)
    plt.title(f"{cont_col} by {cat_col}")
    plt.show()
    
    # Plot a violin plot for the continuous variable by category
    plt.figure(figsize=(10, 6))
    sns.violinplot(x=cat_col, y=cont_col, data=df)
    plt.title(f"{cont_col} by {cat_col}")
    plt.show()
    
    # Plot a swarmplot for the continuous variable by category
    plt.figure(figsize=(10, 6))
    sns.swarmplot(x=cat_col, y=cont_col, data=df)
    plt.title(f"{cont_col} by {cat_col}")
    plt.show()    
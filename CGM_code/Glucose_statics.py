import numpy as np
import pandas as pd
def compute_glucose_summary(df):
    """
    Compute the summary statistics of glucose levels including mean, median, minimum, maximum, first quartile,
    and third quartile.

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    DataFrame: A DataFrame containing the mean, median, minimum, maximum, first quartile, and third quartile
    of glucose levels.
    """
    meanG = df['glucose'].mean()
    medianG = df['glucose'].median()
    minG = df['glucose'].min()
    maxG = df['glucose'].max()
    Q1G = df['glucose'].quantile(0.25)
    Q3G = df['glucose'].quantile(0.75)

    return pd.DataFrame({'meanG': [meanG],
                         'medianG': [medianG],
                         'minG': [minG],
                         'maxG': [maxG],
                         'Q1G': [Q1G],
                         'Q3G': [Q3G]})
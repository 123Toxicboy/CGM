import numpy as np

def compute_mge(df, sd=1):
    """
    Compute the Mean of Glycemic Excursions (MGE).

    Parameters:
    df (DataFrame): DataFrame containing glucose data.
    sd (float): Standard deviation indicating glycemic excursion. Default is 1.

    Returns:
    float: Numeric value representing MGE.
    """
    up = df['glucose'].mean() + sd * np.std(df['glucose'])
    dw = df['glucose'].mean() - sd * np.std(df['glucose'])
    mge = df[(df['glucose'] >= up) | (df['glucose'] <= dw)]['glucose'].mean()
    return mge


def compute_mgn(df):
    """
    Compute the Mean of Normal Glucose (MGN).

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    float: Numeric value representing MGN.
    """
    up = df['glucose'].mean() + np.std(df['glucose'])
    dw = df['glucose'].mean() - np.std(df['glucose'])
    mgn = df[(df['glucose'] <= up) | (df['glucose'] >= dw)]['glucose'].mean()
    return mgn
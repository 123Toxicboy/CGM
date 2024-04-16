import numpy as np

def compute_tor(df, sd=1, sr=5):
    """
    Compute the Time Outside Range (TOR).

    Parameters:
    df (DataFrame): DataFrame containing glucose data.
    sd (float): Standard deviation indicating glycemic excursions. Default is 1.
    sr (int): Sampling rate inverse in minutes of the CGM. Default is 5.

    Returns:
    float: Numeric value representing TOR.
    """
    up = df['glucose'].mean() + sd * np.std(df['glucose'])
    dw = df['glucose'].mean() - sd * np.std(df['glucose'])
    tor = df[(df['glucose'] >= up) | (df['glucose'] <= dw)].shape[0] * sr
    return tor
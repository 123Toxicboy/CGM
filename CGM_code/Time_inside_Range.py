import numpy as np

def compute_tir(df, sd=1, sr=5):
    """
    Compute the Time Inside Range (TIR).

    Parameters:
    df (DataFrame): DataFrame containing glucose data.
    sd (float): Standard deviation indicating glycemic excursions. Default is 1.
    sr (int): Sampling rate inverse in minutes of the CGM. Default is 5.

    Returns:
    float: Numeric value representing TIR.
    """
    up = df['glucose'].mean() + sd * np.std(df['glucose'])
    dw = df['glucose'].mean() - sd * np.std(df['glucose'])
    tir = df[(df['glucose'] <= up) & (df['glucose'] >= dw)].shape[0] * sr
    return tir
import numpy as np

def compute_interday_cv(df):
    """
    Compute the Interday Coefficient of Variation (CV).

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    float: Numeric value representing interday CV.
    """
    cvx = (np.std(df['glucose']) / np.mean(df['glucose'])) * 100
    return cvx


def compute_interday_sd(df):
    """
    Compute the Interday Standard Deviation (SD).

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    float: Numeric value representing interday SD.
    """
    interdaysd = np.std(df['glucose'])
    return interdaysd
import numpy as np

def compute_j_index(df):
    """
    Compute the J-index, a glycemic variability metric.

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    float: Numeric value representing J-index.
    """
    j_index = 0.001 * ((df['glucose'].mean() + np.std(df['glucose'])) ** 2)
    return j_index
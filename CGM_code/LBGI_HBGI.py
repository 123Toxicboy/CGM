import pandas as pd
import numpy as np

def compute_lbgi_hbgi(df):
    """
    Compute the Low Blood Glucose Index (LBGI) and High Blood Glucose Index (HBGI).

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    DataFrame: A DataFrame containing both LBGI and HBGI values.
    """
    log_glucose = np.log(df['glucose'] ** 1.084) - 5.381
    f = pd.DataFrame({'log_glucose': log_glucose})
    f['rl'] = np.where(f['log_glucose'] <= 0, 22.77 * (f['log_glucose'] ** 2), 0)
    f['rh'] = np.where(f['log_glucose'] > 0, 22.77 * (f['log_glucose'] ** 2), 0)

    LBGI = f['rl'].mean()
    HBGI = f['rh'].mean()

    return pd.DataFrame({'LBGI': [LBGI], 'HBGI': [HBGI]})


def compute_lbgi(df):
    """
    Compute the Low Blood Glucose Index (LBGI).

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    float: Numeric value representing LBGI.
    """
    log_glucose = (np.log(df['glucose']) ** 1.084) - 5.381
    f = pd.DataFrame({'log_glucose': log_glucose})
    f['rl'] = np.where(f['log_glucose'] <= 0, 22.77 * (f['log_glucose'] ** 2), 0)

    return f['rl'].mean()


def compute_hbgi(df):
    """
    Compute the High Blood Glucose Index (HBGI).

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    float: Numeric value representing HBGI.
    """
    log_glucose = (np.log(df['glucose']) ** 1.084) - 5.381
    f = pd.DataFrame({'log_glucose': log_glucose})
    f['rh'] = np.where(f['log_glucose'] > 0, 22.77 * (f['log_glucose'] ** 2), 0)

    return f['rh'].mean()

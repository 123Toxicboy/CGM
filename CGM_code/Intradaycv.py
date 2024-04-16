import numpy as np
import pandas as pd

from Interday import compute_interday_cv

def compute_intraday_cv(df):
    """
    Compute the Intraday Coefficient of Variation (CV) summary statistics:
    mean, median, standard deviation of all days in data.

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    DataFrame: A DataFrame containing the mean, median, and standard deviation
    of the intraday coefficients of variation.
    """
    intraday_cv = []
    for date in df['Date'].unique():
        intraday_cv.append(compute_interday_cv(df[df['Date'] == date]))

    intraday_cv_mean = np.mean(intraday_cv)
    intraday_cv_median = np.median(intraday_cv)
    intraday_cv_sd = np.std(intraday_cv)

    return pd.DataFrame({'intradaycv_mean': [intraday_cv_mean],
                         'intradaycv_median': [intraday_cv_median],
                         'intradaycv_sd': [intraday_cv_sd]})


def compute_intraday_sd(df):
    """
    Compute the Intraday Standard Deviation (SD) summary statistics:
    mean, median, standard deviation of all days in data.

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    DataFrame: A DataFrame containing the mean, median, and standard deviation
    of the intraday standard deviations.
    """
    intraday_sd = []
    for date in df['Date'].unique():
        intraday_sd.append(np.std(df[df['Date'] == date]['glucose']))

    intraday_sd_mean = np.mean(intraday_sd)
    intraday_sd_median = np.median(intraday_sd)
    intraday_sd_sd = np.std(intraday_sd)

    return pd.DataFrame({'intradaysd_mean': [intraday_sd_mean],
                         'intradaysd_median': [intraday_sd_median],
                         'intradaysd_sd': [intraday_sd_sd]})
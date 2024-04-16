def compute_ea1c(df):
    """
    Compute the Estimated A1c (eA1c) according to the American Diabetes Association calculator.

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    float: Numeric value representing eA1c.
    """
    ea1c = (46.7 + df['glucose'].mean()) / 28.7
    return ea1c
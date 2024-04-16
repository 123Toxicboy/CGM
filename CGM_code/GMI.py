def compute_gmi(df):
    """
    Compute the Glycemic Management Indicator (GMI).

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    float: Numeric value representing GMI.
    """
    gmi = 3.31 + (0.02392 * df['glucose'].mean())
    return gmi
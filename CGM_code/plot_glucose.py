import matplotlib.pyplot as plt

def plot_glucose(df):
    """
    Plot glycemic excursions over the time period in which data was collected.

    Parameters:
    df (DataFrame): DataFrame containing glucose data.

    Returns:
    None
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    for date in df['Date'].unique():
        df_date = df[df['Date'] == date]
        ax.plot(df_date['time_of_day'], df_date['glucose'], marker='o', linestyle='-', color='orange', markersize=3)

    ax.set_xlabel('Time of Day')
    ax.set_ylabel('Glucose Level')
    ax.set_title('CGM data for Participant #1')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
import pandas as pd
import matplotlib.pyplot as plt

def plot_cat_freq(column, title='Freq', ax=None):
    value_counts = column.value_counts()
    if ax is None:
        fig, ax = plt.subplots()

    # Plot the bar chart
    ax.bar(value_counts.index, value_counts.values)

    # Add labels and title
    ax.set_ylabel('Frequency')
    ax.set_title(title)

def plot_all_cat_freq(df, figsize = (15, 15)):
    num_cols = df.select_dtypes(include='object').shape[1]
    num_rows = (num_cols - 1) // 3 + 1  # Calculate the number of rows based on 3 columns per row
    fig, axes = plt.subplots(nrows=num_rows, ncols=3, figsize=figsize)

    for i, column in enumerate(df.select_dtypes(include='object')):
        row_idx = i // 3
        col_idx = i % 3
        plot_cat_freq(df[column], title=column, ax=axes[row_idx, col_idx])

    plt.tight_layout()
    plt.show()

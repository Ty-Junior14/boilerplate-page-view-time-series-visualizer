import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

lower_percentile = df['value'].quantile(0.025)
upper_percentile = df['value'].quantile(0.975)

# Clean data
df = df[(df['value'] >= lower_percentile) & (df['value'] <= upper_percentile)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['value'], color='blue', lw=1)

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=16)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Page Views', fontsize=12)

    plt.xticks(rotation=45)







    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Draw bar plot

    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    df_grouped = df_grouped[sorted(df_grouped.columns)]

    month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                   7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    df_grouped.columns = [month_names[m] for m in df_grouped.columns]

    fig, ax = plt.subplots(figsize=(10, 6))
    df_grouped.plot(kind='bar', ax=ax, width=0.8)

    ax.set_title('Average Daily Page Views for Each Month Grouped by Year', fontsize=16)
    ax.set_xlabel('Years', fontsize=12)
    ax.set_ylabel('Average Page Views', fontsize=12)

    ax.legend(title='Months', fontsize=10)

    plt.xticks(rotation=45)







    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(x='year', y='value', data=df_box, ax=ax1, hue='year', palette="coolwarm", legend=False)
    ax1.set_title('Year-wise Box Plot (Trend)', fontsize=16)
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Page Views', fontsize=12)

    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, hue='month', palette="coolwarm",
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                legend=False)
    ax2.set_title('Month-wise Box Plot (Seasonality)', fontsize=16)
    ax2.set_xlabel('Month', fontsize=12)
    ax2.set_ylabel('Page Views', fontsize=12)


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

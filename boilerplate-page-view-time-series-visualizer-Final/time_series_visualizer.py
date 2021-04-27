import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col= 'date', parse_dates= ['date'])

# Clean data
df = df.loc[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, axes= plt.subplots(figsize = (12,8))
    plt.plot(df,color = 'red')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig.set
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # Draw bar plot
    groupby_year = df_bar.groupby([df_bar.index.year,df_bar.index.month,])['value'].mean().unstack()
    fig = groupby_year.plot(kind = 'bar', figsize = (12,8)).figure
    plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December'],title = 'Months')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,axes = plt.subplots(1,2,figsize = (14,10)) #one row of two plots
    sns.boxplot(x = 'Year', y = 'value', data = df_box, ax = axes[0])
    sns.boxplot(x = 'Month', y = 'value', data = df_box, ax = axes[1])
    axes[0].set_ylabel('Page Views')
    axes[1].set_ylabel('Page Views')
    axes[1].set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

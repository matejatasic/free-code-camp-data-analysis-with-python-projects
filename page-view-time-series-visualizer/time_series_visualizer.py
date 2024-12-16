import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to "date".)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)\

# Clean data
df = df[
    (df["value"] > df["value"].quantile(.025)) 
    & (df["value"] < df["value"].quantile(.975))
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.plot(df.index, df["value"], color="red")
    ax.set_xlabel(xlabel="Date")
    ax.set_ylabel(ylabel="Page Views")
    ax.set_title(label="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don"t change this part)
    fig.savefig("line_plot.png")
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)

    month_names = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    )

    df_bar["years"] = df_bar.index.year
    months = df_bar.index.month_name()
    df_bar["months"] = pd.Categorical(values=months, categories=month_names)

    df_bar_pivot = pd.pivot_table(
        data=df_bar,
        values="value",
        index="years",
        columns="months"
    )

    # Draw bar plot
    fig = df_bar_pivot.plot(kind="bar").get_figure()
    fig.set_figwidth(16)
    fig.set_figheight(8)

    plt.xlabel(xlabel="Years")
    plt.ylabel(ylabel="Average Page Views")
    plt.legend(title="Months")

    # Save image and return fig (don"t change this part)
    fig.savefig("bar_plot.png")

    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]
    
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    ylabel = "Page Views"

    # Plot 1
    plt.subplot(1, 2, 1)
    sns.boxplot(data=df_box, x="year", y="value").get_figure()
    plt.ylabel(ylabel=ylabel)
    plt.xlabel(xlabel="Year")
    plt.title(label="Year-wise Box Plot (Trend)")

    # Plot 2
    plt.subplot(1, 2, 2)
    months = (
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
    )
    sns.boxplot(data=df_box, x="month", y="value", order=months).get_figure()
    plt.ylabel(ylabel=ylabel)
    plt.xlabel(xlabel="Month")
    plt.title(label="Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don"t change this part)
    fig.savefig("box_plot.png")
    return fig

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["overweight"] = np.where(df["weight"] / ((df["height"] / 100) ** 2) > 25, 1, 0)

# 3
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1

df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])
    
    # 6
    # df_cat = None
    
    # 7
    catplot = sns.catplot(data=df_cat, x="variable", hue="value", col="cardio", kind="count").set(ylabel = "total")


    # 8
    fig = catplot.fig


    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[ 
        ( df['ap_lo'] <= df['ap_hi'] ) & 
        ( df['height'] >= df['height'].quantile(0.025) ) & 
        ( df['height'] <= df['height'].quantile(0.975) ) & 
        ( df['weight'] >= df['weight'].quantile(0.025) ) & 
        ( df['weight'] <= df['weight'].quantile(0.975) ) 
    ]
    
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots()

    # 15
    ax= sns.heatmap(data=corr, cmap="coolwarm", annot=True, fmt=".1f", mask=mask, ax=ax)

    # 16
    fig.savefig("heatmap.png")
    return fig

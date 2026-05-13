import pandas as pd

df = pd.read_csv("Social_Media_Advertising.csv")

# What platforms are in this dataset?
print("Channels available:")
print(df["Channel_Used"].unique())

# How many ads per platform?
print("\nAd count per channel:")
print(df["Channel_Used"].value_counts())

# What are the different campaign goals?
print("\nCampaign goals:")
print(df["Campaign_Goal"].unique())

# What target audiences exist?
print("\nTarget audiences:")
print(df["Target_Audience"].unique())

# What is the ROI range?
print("\nROI stats:")
print(df["ROI"].describe())
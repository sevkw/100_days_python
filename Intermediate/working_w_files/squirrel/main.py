import pandas as pd

data = pd.read_csv(r".\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_color = data["Primary Fur Color"]
squirrel_color_count = squirrel_color.value_counts().to_frame()
squirrel_color_count.to_csv(r".\squirrel_count.csv")

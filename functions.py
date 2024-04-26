import pandas as pd
import numpy as np

dataset = "Popular_Baby_Names.csv"
# function that returns all years from dataset
def getAllYears(db):
    try:
        dataframe = pd.read_csv(db)
    except TypeError as te:
        return te
    years = dataframe["Year of Birth"].unique()
    return sorted(years)


# function that returns all ethnicities from dataset
def getAllEthnicities(db):
    try:
        dataframe = pd.read_csv(db)
    except Exception as ex:
        return ex
    ethnicities = dataframe["Ethnicity"].unique()
    return sorted(ethnicities)


# function that returns top ten popular names as the list
def topFivePopularNamesThisYear(db):
    try:
        dataframe = pd.read_csv(db)
    except Exception as ex:
        return ex

    year = int(input(f"Choose the year among {all_years}: "))
    ethnicity = input(f"Choose ethnicity among {all_ethnicities}: ").lower()
    top_five = set()
    for index, row in dataframe.iterrows():
        if row["Rank"] <= 5 and row["Year of Birth"] == year and ethnicity == row["Ethnicity"].lower():
            top_five.add(row["Child's First Name"])

    return top_five, year, ethnicity




# function that returns average count of the names in dataset
def actionCount(db):
    action = input("choose the action among [max, avg, min] ")
    try:
        dataframe = pd.read_csv(db)
    except Exception as ex:
        return ex

    list_count = []
    for index, row in dataframe.iterrows():
        list_count.append(row["Count"])
    try:
        arr = np.array(list_count)
    except Exception as ex:
        return ex

    if action == "max":
        return f"the maximum count of unique names is {arr.max()}"
    if action == "min":
        return f"the minimum count of unique names is {arr.min()}"
    if action == "avg":
        return f"the average count of names is {arr.mean()}"

all_years = getAllYears(dataset)
all_ethnicities = getAllEthnicities(dataset)

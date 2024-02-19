# Data Analysis & Machine Learning
# Pandas
import pandas as pd
print("pandas series")
# 1 D Array - List
sales = pd.Series([100,200,250,150,300])
print(sales)
print("data type ",type(sales))
print("shape ",sales.shape)

# 2 D Array - Dictionary
countries={
    "Country":["India","USA","China","Germany","UK"],
    "Captital":["ABC","XYZ","CDE","MNP","OPV"],
    "GDP":[7,8,5,8,9],
    "GDPRank":[2,1,3,4,5]
}

topcountries = pd.DataFrame(countries)
print("data frame ",topcountries)
print("shape ",topcountries.shape)
print("rows",topcountries.shape[0]," columns",topcountries.shape[1])
print(topcountries["Country"])
print(topcountries["GDP"])
print(topcountries["Captital"])

topcountriessort = topcountries.sort_values("GDPRank",ascending=True)
print("The Sort is ",topcountriessort)
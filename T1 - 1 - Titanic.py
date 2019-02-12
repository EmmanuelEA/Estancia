import pandas as pd

data = pd.read_csv("~/Downloads/11009-CELAYA (SMN)-GTO-Hunit.csv",skiprows = 7)

data.head()

mainpath = "~/Documents/GitHub/python-ml-course/datasets"
filename = "titanic/titanic3.xls"
filename2 = "titanic/titanic3.xlsx"

titanic2 = pd.read_excel(mainpath + "/" + filename, "titanic3")
titanic3 = pd.read_excel(mainpath + "/" + filename, "titanic3")
titanic3.to_csv(mainpath + "/titanic/titanic_custom.csv")
titanic3.to_excel("/home/eea/Downloads/titanic3_custom.xls")
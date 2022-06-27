import pandas as pd

data = [[50, True], [40, False], [30, False]]
label_rows = ["Ioana", "Maria", "Ion"]
label_cols = ["varsta", "calificat"]

df = pd.DataFrame(data, label_rows, label_cols)
print(df.loc["Ioana", "varsta"])

data2 = [[50, True], [40, False], [30, False]]

df = pd.DataFrame(data2)

print(df.iloc[1, 0])
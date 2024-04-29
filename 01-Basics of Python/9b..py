import pandas as pd
df = pd.DataFrame(
{
"Gender": ['Male','Male','Female','Female','Female'],
"Team" : [1,2,3,3,1]
})
print("Displaying DataFrame\n")
print(df)
print("\nDisplaying the distribution of genders in each team\n")
print(pd.crosstab(df.Gender, df.Team))
print("\nDisplaying the distribution of teams for each gender\n")
print(pd.crosstab(df.Team, df.Gender))
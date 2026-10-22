#Chapter 1 SERIES :-----> A series is a one D. it has labels and values (index + values) = Series.
#Numpy stores the positions and Pandas stores position plus labels.
#Series are vectors (5,).
#for dictionary keys becomes the index and the values become the series values.
#for custom index we replace meaningless numbers with meaningful labels.
# Index VS Values:- the series stores one object as index and the one numpy array called values.
#pandas are fast cause it store internally as numpy values.
#Every series can have a name.


#import pandas as pd

#s = pd.Series([10,20,30,40])
#print(s)
#print(s.shape)
#print(s.size)

#marks = pd.Series(
#    [88,92,75],
#    index=["Aman","Rahul","John"]
#)
#print(marks)
#print(marks.shape)
#print(marks.size)
#print(marks.index)

#temperature = pd.Series(
#    [18,22,25,19,21],
#    index = ["Mon","Tue","Wed","Thu","Fri"]
#)
#print(temperature["Wed"])
#print(temperature.iloc[3])
#temperature["Wed"] = 28
#print(temperature)
#print(temperature * 2)

#Sales = pd.Series(
#    [10,200,300,400,500],
#    index = ["Mon","Tue","Wed","Thu","Fri"]
#)
#print(Sales.iloc[2:5])
#print(Sales.loc["Tue":"Thu"])
#print(Sales.iloc[::-1])

#Prices = pd.Series(
#    [100,200,300,400],
#    index = ["A","B","C","D"]
#)
#print((Prices/sum(Prices)*100)+Prices)

#sales = pd.Series(
#    [100, 200, 300],
#    index=["A", "B", "C"]
#)

#returns = pd.Series(
#    [10, 20, 30],
#    index=["A", "B", "C"]
#)
#net_result = sales - returns
#print(net_result)

#a = pd.Series(
#    [100, 200, 300],
#    index=["A", "B", "C"]
#)

#b = pd.Series(
#    [10, 20, 30],
#    index=["C", "A", "B"]
#)
#print(a + b)

#a = pd.Series(
#    [100, 200, 300],
#    index=["A", "B", "C"]
#)

#b = pd.Series(
#    [10, 20, 30],
#    index=["B", "C", "D"]
#)
#print(a + b)

#actual = pd.Series(
#    [1, 0, 1, 1, 0],
#    index=["img1", "img2", "img3", "img4", "img5"]
#)

#prediction = pd.Series(
#    [0.8, 0.2, 0.9, 0.7, 0.1],
#    index=["img3", "img1", "img5", "img2", "img4"]
#)
#error = actual - prediction
#print(error)
#print(max(error))

#prediction = pd.Series(
#    [0.91, 0.12, 0.88, 0.45, 0.97, 0.03],
#    index=["img1", "img2", "img3", "img4", "img5", "img6"]
#)
#result = prediction >=0.90
#boolean = prediction[result]
#print(boolean)


#model_A = pd.Series(
#    [0.90, 0.20, 0.80, 0.70],
#    index=["img1", "img2", "img3", "img4"]
#)

#model_B = pd.Series(
#    [0.60, 0.30, 0.95, 0.85],
#    index=["img3", "img1", "img4", "img2"]
#)
#difference = model_A - model_B
#print(difference)
#print(min(difference))

#actual = pd.Series(
#    [1, 0, 1, 1, 0, 1],
#    index=["A", "B", "C", "D", "E", "F"]
#)

#prediction = pd.Series(
#    [0.95, 0.20, 0.80, 0.60, 0.10, 0.99],
#    index=["D", "A", "F", "C", "B", "E"]
#)
#error = actual - prediction
#print(error)
#print(error.abs())
#print(max(abs(error)))

#DataFrames:--->It si a 2D. it has row,columns,index,values.
#import pandas as pd
#import numpy as np

#records = [
#    {"user_id": 101, "age": 25, "country": "UK", "purchase": 200},
#    {"user_id": 102, "age": 30, "country": "US", "purchase": 350},
#    {"user_id": 103, "age": 28, "country": "UK", "purchase": 150},
#    {"user_id": 104, "age": 35, "country": "IN", "purchase": 500}
#]
#result = pd.DataFrame(records)
#print(result)
#x = result[["age","country"]]
#y = result["purchase"]
#print(x)
#print(y) # user_id is not valid input to get the prediction. it is used as the label.

#records = [
#    {"id": 1, "name": "Alice", "score": 90},
#    {"id": 2, "name": "Bob"},
#    {"id": 3, "name": "Charlie", "score": 85},
#    {"id": 4, "name": "David", "score": 70}
#]
#o = pd.DataFrame(records)
#print(o)
#j = o["score"].mean()
#print(j)
#o["score"] = o["score"].fillna(j)
#o["passed"] = np.where(o["score"] >= 80,True,False)
#print(o)

#names = pd.Series(
#    ["Alice", "Bob", "Charlie"],
#    index=[101, 102, 103]
#)

#scores = pd.Series(
#    [95, 80, 90],
#    index=[103, 101, 102]
#)

#df = pd.DataFrame({
#    "name": ["Alice", "Bob", "Charlie"],
#    "score": [95, 80, 90]
#})
#print(df)


#import pandas as pd
#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#    "Age": [25, 30, 25, 40, 30],
#    "Department": ["AI", "ML", "AI", "Data", "ML"],
#    "Salary": [60000, 75000, 65000, 90000, 80000]
#})
#print(df.shape)
#print(df.memory_usage(deep=True))
#print(df.info())
#print(df.describe())
#print(df.nunique())
#print(df["Department"].value_counts())

#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie"],
#    "Age": [25, 30, 35]
#})


#import pandas as pd

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104, 105],
#    "age": [25, 32, 28, 41, 30],
#    "income": [50000, 80000, 65000, 120000, 70000],
#    "country": ["UK", "US", "UK", "India", "US"],
#    "churn": [0, 1, 0, 1, 0],
#    "satisfaction": [8, 5, 9, 4, 7]
#})
#X = df[["age","income","country","satisfaction"]]
#y = df["churn"]
##print(X)
#print(y)
#print(X.shape)
#print(y.shape)


#feature_columns = ["age", "income", "satisfaction"]
#metadata_columns = ["user_id", "country"]
#target_column = "churn"
#X = df[feature_columns]
#y = df[target_column]
#metadata = df[metadata_columns]
#print(X)
#print(metadata)

#required_columns = ["age", "income", "country", "satisfaction"]

#available_columns = df.columns.tolist()
#print(required_columns)
#x = df[required_columns]
#print(x)
#print(y)


#import pandas as pd
#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#    "Age": [25, 30, 28, 35, 22],
#    "Salary": [50000, 70000, 60000, 90000, 45000]
#})
#print(df.iloc[[1,2,4]])
#print(df.loc[[1,3]])
#print(df.iloc[[1,3]])

#df = pd.DataFrame({
#    "Name": ["A", "B", "C", "D", "E"],
#    "Score": [80, 90, 70, 95, 85]
#})
#print(df.loc[1:3])
#print(df.iloc[1:4])


#import pandas as pd

#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#    "Age": [25, 30, 28, 35, 22],
#    "Salary": [50000, 70000, 60000, 90000, 45000],
#    "Score": [85, 90, 75, 95, 80]
#}, index=["emp101", "emp102", "emp103", "emp104", "emp105"])

#f = df.loc["emp102":"emp104",["Name","Salary"]]
#print(f)

#o = df.iloc[1:4,1:3]
#print(o)

#df["Salary"] = df["Salary"].astype(float)
#df.loc[["emp102","emp104"],"Salary"] *= 1.10
#print(df)


#import pandas as pd

#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#    "Age": [25, 30, 28, 35, 22],
#    "Salary": [50000, 70000, 60000, 90000, 45000],
#    "Score": [85, 90, 75, 95, 80]
#}, index=["emp101", "emp102", "emp103", "emp104", "emp105"])

#df[["Salary","Score"]] = df[["Salary","Score"]].astype(float)
#df.loc[["emp102","emp103","emp104"],["Salary","Score"]] *= 1.10
#print(df)

#import pandas as pd

#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#    "Age": [25, 30, 28, 35, 22],
#    "Salary": [50000, 70000, 60000, 90000, 45000],
#    "Score": [85, 90, 75, 95, 80],
#    "Department": ["AI", "ML", "AI", "Data", "ML"]
#})
#f = df[
#    (df["Age"]>=28)&
#    (df["Salary"]>60000)
#]
#print(f)
#print(
#    df.loc[
#        df["Department"].isin(["AI","Data"]),
#        ["Name","Department","Score"]
#    ]
#)

#print(
#    df.loc[
#        (df["Score"]>=85) & (df["Department"].isin(["AI","ML"])),
#        ["Name","Salary","Score"]
#    ]
#)

#import pandas as pd
#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#    "Age": [25, 30, 28, 35, 22],
#    "Salary": [50000, 70000, 60000, 90000, 45000],
#    "Score": [85, 90, 75, 95, 80],
#    "Department": ["AI", "ML", "AI", "Data", "ML"]
#})

#print(
#    df.loc[
#        (df["Age"].between(25,30)) &
#        (df["Department"].isin(["AI","ML"])) &
#        (df["Salary"] >= 50000),
#        ["Name","Age","Salary","Department"]
#    ]
#)

#print(
#    df.loc[
#        (~df["Score"].between(80,90)) |
#        (df["Salary"] > 80000),
#        ["Name","Salary","Score"]
#    ]
#)

#import pandas as pd
#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
#    "Age": [25, 32, 28, 41, 22, 36],
#    "Salary": [50000, 80000, 60000, 120000, 45000, 95000],
#    "Score": [85, 92, 76, 95, 81, 68],
#    "Department": ["AI", "ML", "AI", "Data", "ML", "AI"]
#})
#print(
#    df.query("Age>=25 and Age<=40 and Salary >= 60000 "
#             "and Department in ['AI','ML']"
#             "and Score >= 80 ")[["Name","Age","Salary","Score"]]
#)

#adjust_score = df["Score"].where(df["Score"] >=80,0)
#print(adjust_score)
#print(df)

#result = df[["Name","Salary","Score"]].copy()
#result["Salary"] = result["Salary"].mask(result["Salary"]<60000)
#result["Score"] = result["Score"].mask(result["Score"]<80)
#print(result)

#import pandas as pd
#import numpy as np

#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
#    "Age": [25, 32, 28, 41, 22, 36],
#    "Salary": [50000, 80000, 60000, 120000, 45000, 95000],
#    "Score": [85, 92, 76, 95, 81, 68],
#    "Department": ["AI", "ML", "AI", "Data", "ML", "AI"]
#})

#print(
#    df.query("Age > 25 and Age <40"
#               "and Salary > 55000"
#               "and Department in ['AI','ML']"
#               "and Score > 80")[["Name","Salary","Department"]]
#      )
#print(
#    df["Score"].where(df["Score"]>= 80,0)
#)


#result = df[["Name","Salary","Score"]].copy()
#result["Salary"] = result["Salary"].mask(result["Salary"]<60000)
#result["Score"] = result ["Score"].mask(result["Score"]<80)
#print(result)

#import pandas as pd

#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David"],
#    "Age": [25, 30, 28, 35],
#    "Salary": [50000, 70000, 60000, 90000],
#    "Department": ["AI", "ML", "AI", "Data"]
#})
#df.loc[1,"Age"]=32
#print(df)
#df["Salary"] = df["Salary"].astype(float)
#df.loc[[0,2],"Salary"]=[55000,65000]
#print(df)


#df.loc[df["Department"]=="AI","Salary"]*=1.10
#print(df)

#v = df.iloc[3,1]=40
#print(df)

#df["Department"] = df["Department"].replace(
#    {"AI" : "Artificial Intelligence",
#     "ML" : "Machine Learning",}
#)
#print(df)


#high_salary = df[df["Salary"]>70000].copy()
#high_salary["Salary"] *= 1.10
#print(high_salary)

                                        #Modifying Frame :
#import pandas as pd
##df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
#    "Age": [25, 32, 28, 41, 22, 36],
#    "Salary": [50000, 80000, 60000, 120000, 45000, 95000],
#    "Score": [85, 92, 76, 95, 81, 68],
#    "Department": ["AI", "ML", "AI", "Data", "ML", "AI"]
#})

#df.loc[1,"Age"]=35
#print(df)

#df.loc[[0,2,4],"Salary"]+=5000
#print(df)

#df.loc[1,["Age","Score"]] = [33,95]
#print(df)

#df.iloc[3,3] = 100
#print(df)

#df["Salary"] = df["Salary"].astype(float)
##df.loc[df["Department"]=="AI","Salary"] *= 1.10
#print(df)

#df["Salary"] = df["Salary"].astype(float)
#condition = (
#(df["Department"]=="AI")&
##(df["Score"]>=80)
#)
#df.loc[condition,"Salary"]*=1.10
#print(df)

#df["Salary"] = df["Salary"].astype(float)
#df["Score"] = df["Score"].astype(float)
#condition = (
#(df["Salary"]>=80000)&
#(df["Score"]>=90)
#)
#df.loc[condition,["Salary","Score"]] *= [1.10,1.05]
#print(df)

#df["Department"] = df["Department"].replace(
#    {"Unknown" : "other"}
#)
#print(df)

#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
#    "Age": [25, 32, 28, 41, 22, 36],
#    "Salary": [50000, 80000, 60000, 120000, 45000, 95000],
#    "Score": [85, 92, 76, 95, 81, 68],
#    "Department": ["AI", "ML", "AI", "Data", "ML", "AI"]
#})

#high_salary = df[df["Salary"]>=70000].copy()
##high_salary["Score"] = 100
#print(high_salary)

#df.loc[df["Salary"]>=70000,"Score"] = 100
#print(df)

#high_salary = df.loc[df["Salary"]>=70000].copy()

#high_salary[["Salary","Score"]] *= [1.10,1.05]
#print(high_salary)


#df["Salary"] = df["Salary"].astype(float)
#df.loc[df["Score"]>=90,"Salary"] *= 1.20
#df.loc[
#    (df["Score"]>=80) &(df["Score"]< 90),"Salary"
#] *= 1.10
#print(df)

#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
#    "Age": [25, 32, 28, 41, 22, 36],
#    "Salary": [50000, 80000, 60000, 120000, 45000, 95000],
#    "Score": [85, 92, 76, 95, 81, 68],
#    "Department": ["AI", "ML", "AI", "Data", "ML", "AI"]
#})

#df.loc[df["Score"]<0,"Score"] = 0
#df.loc[df["Score"]>100,"Score"] = 100
#df.loc[df["Age"]<18,"Age"] = 18
#df["Department"] = df["Department"].replace(
#    {"AI":"Artificial Intelligence",
#     "ML":"Machine Learning"}
#)
#print(df)

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104, 105, 106],
#    "age": [25, 17, 35, 42, 16, 29],
#    "income": [50000, 40000, 90000, 120000, 30000, 70000],
#    "score": [85, 120, 75, 95, -10, 88],
##    "department": ["AI", "ML", "AI", "Data", "ML", "AI"]
#})

#df.loc[df["age"]<18,"age"] = 18
#df.loc[df["score"]<0 ,"score"] = 0
#df.loc[df["score"]>100,"score"] = 100
#df["income"] = df["income"].astype(float)
#df["department"] =df["department"].replace(
#    {"AI":"Artificial Intelligence",
#     "ML":"Machine Learning"}
#)
#condition = (
#        (df["income"]>=70000) &
#        (df["score"]>=80)
#)
#high_value = df[condition].copy()
#high_value["income"] *= 1.10
#print("new==============")
#print(high_value)
#print("New-------")
#print(df)

#import pandas as pd

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104, 105, 106, 107],
#    "age": [17, 25, 45, 16, 30, 52, 22],
#    "salary": [45000, 80000, 120000, 60000, 75000, 150000, 40000],
#    "score": [95, 88, 105, -10, 92, 78, 101],
#    "department": ["AI", "ML", "AI", "Unknown", "ML", "Data", "AI"]
#})
#df.loc[df["age"]<18,"age"] = 18
#df.loc[df["score"]<0,"score"] = 0
#df.loc[df["score"]>100,"score"] = 100
#df["department"] = df["department"].replace(
#    {"AI":"Artificial Intelligence",
#     "ML":"Machine Learning",
#     "Unknown": "others"}
#)
#condition = (
#   ( df["salary"]>=70000 )&
#    (df["score"] >=90)
#)
#high_value = df[condition].copy()
#high_value["salary"] *=1.10
#high_value["score"] *=1.05
##print("High---Value")
#print(high_value)
#print("\nORIGINAL")
#print(df)


#                                   CREATING COLUMNS:------------>
#import pandas as pd
#import numpy as np
#from pyexpat import features

#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry"],
#    "Age": [22, 31, 28, 45, 19, 36, 52, 27],
#    "Salary": [45000, 75000, 60000, 120000, 40000, 90000, 150000, 65000],
#    "Score": [78, 92, 85, 95, 65, 88, 97, 72],
#    "Department": ["AI", "ML", "AI", "Data", "ML", "AI", "Data", "ML"]
#})
#df["Country"] = ["UK","USA","INDIA","UK","INDIA","USA","UK","USA"]
#print(df)

#df["Status"] = "Active"
#print(df)

#df["Salary_K"] = df["Salary"] / 1000
#print(df)

#df["Age_next_year"] = df["Age"] + 1
#print(df)

#df["Salary_per_Age"] = (df["Salary"] / df["Age"]).round(2)
#print(df)


#df["Salary_Level"] = np.where((df["Salary"]>=80000),"High","Low" )
#print(df)

#df["performance"] = np.where(
#    df["Score"]>=90,
#    "Excellent",
#    np.where(
#        df["Score"]>=80,
#        "Good",
#        "Needs Improvement"
#        )
#    )
#print(df)

#df = df.assign(
#     Salary_k = df["Salary"]/1000,
#     Age_Next_year  = df["Age"] + 1
#)
#print(df)
#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry"],
#    "Age": [22, 31, 28, 45, 19, 36, 52, 27],
#    "Salary": [45000, 75000, 60000, 120000, 40000, 90000, 150000, 65000],
#    "Score": [78, 92, 85, 95, 65, 88, 97, 72],
#    "Department": ["AI", "ML", "AI", "Data", "ML", "AI", "Data", "ML"]
#})

#df.insert(1,
#          "Country",
#          ["UK", "USA", "India", "UK", "India", "USA", "UK", "USA"])
#print(df)

#df["Department_code"] = df["Department"].map(
#    {"AI": 0,
#     "ML" : 1,
#     "Data" : 2}
#)
#print(df)

#df["Salary_K"] = df["Salary"].map(lambda x : x/1000)
#print(df)

#df["Score_Double"] = df["Score"].apply(lambda x : x*2)
#print(df)

#df["Income_Score_Ratio"] = df.apply(
#    lambda x : x["Salary"] / x["Score"],
#    axis = 1
#).round(2)
#print(df)

#df["Adjust_Salary"] = df["Salary"] * 1.15
#print(df)

#df["Age_Group"] = pd.cut(
#    df["Age"],
#    bins = [0,29,39,49,50],
#    labels = ["Young","Adult","Middle_Age","Senior"]
#)
#print(df)

#df["Salary_Quartile"] = pd.qcut(
#    df["Salary"],
#    4
#)
#print(df)

#df["Salary_k"] = df["Salary"] / 1000
#df["Age_Squared"] = df["Age"]**2
#df["Salary_per_Age"] = df["Salary"] / df["Age"]
#print(df)

#df.assign(
#    salary_k = df["Salary"] / 1000,
#    Age_Squared = df["Age"]**2,
#    Salary_per_age = df["Salary"] / df["Age"]
#)
#print(df)

#df["Candidate_Level"] = np.where((df["Score"]>=90) & (df["Salary"]>= 80000),
#                                 "Top candidate",
#                                 np.where((df["Score"]>=80) & (df["Salary"]>=60000),
#                                          "Strong candidate",
#                                          "Regular Candidate")
#                                 )
#print(df)


#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104, 105, 106, 107, 108],
#    "age": [17, 25, 45, 16, 30, 52, 22, 39],
#    "salary": [45000, 80000, 120000, 60000, 75000, 150000, 40000, 95000],
#    "score": [95, 88, 105, -10, 92, 78, 101, 84],
#    "department": ["AI", "ML", "AI", "Unknown", "ML", "Data", "AI", "ML"]
#})

#df["age"] = df.loc[df["age"]<18,"age"] = 18
#df["score"] = df.loc[df["score"]<0,"score"] = 0
#df["score"] = df.loc[df["score"]>100,"score"] = 100
#df["department_code"] = df["department"].map(
#    {"AI": 0,
#     "ML":1,
#    "Data":2,
#     "Unknown": -1}
#)
#df["salary_k"] = df["salary"] / 1000
#df["age_squared"] = df["age"]**2
#df["score_normalised"] = df["score"]/df["salary_k"]
#df["age_group"] = pd.cut(
#    df["age"],
#    bins = [0,30,39,49,float("inf")],
#    labels =["young","Adult","Middle_Age","Senior"]
#)
#df["high_value_flag"] = np.where(((df["salary"]>=80000) & (df["score"]>=90)),1,0)
#df = features

#print("New---------->")
#import pandas as pd
#import numpy as np

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#    "name": [
#        "Alice", "Bob", "Charlie", "David", "Eva",
#        "Frank", "Grace", "Henry", "Ivy", "Jack"
#    ],
#    "age": [17, 25, 45, 16, 30, 52, 22, 39, 28, 61],
#    "salary": [
#        45000, 80000, 120000, 60000, 75000,
#        150000, 40000, 95000, 70000, 200000
#    ],
#    "score": [95, 88, 105, -10, 92, 78, 101, 84, 67, 99],
#    "department": [
#        "AI", "ML", "AI", "Unknown", "ML",
#        "Data", "AI", "ML", "Unknown", "Data"
#    ],
#    "experience": [0, 3, 10, 0, 5, 15, 2, 8, 4, 20]
#})

#features = df.copy()
#print(features.shape)
#print(features.columns)
#print(features.dtypes)
#print(features.head())
#print(features.describe())
#print(features.nunique())

#features.loc[features["age"]<18,"age"] =18
#features.loc[features["score"]<0,"score"] = 0
#features.loc[features["score"]>100,"score"] = 100
#features["department_code"] = features["department"].map(
#    {"AI":0,
#     "ML":1,
#     "Data":2,
#     "Unknown":-1
#    }
#)
#features["salary_k"] = features["salary"] / 1000
##features["age_squared"] = features["age"] ** 2
#features["experience_ratio"] = features["experience"]/ features['age']
#features["salary_per_experience"] = np.where(features["experience"] == 0,0,
#features["salary"]/ features['experience']
#)
#features["score_normalized"] = features["score"] / 100
#features["age_group"] = pd.cut(
#    features["age"],
#    bins = [0,30,40,50,float("inf")],
#    labels = ["Young","Adult","Middle_Age","Senior"]
#)
#features["salary_quartiles"] = pd.qcut(
#    features["salary"],
#    4
#)
#features["high_value_flag"] = np.where(
#    (features["salary"]>=80000) &
#    (features["score"]>=90)&
#    (features["experience"]>=5),1,0
#)
#features["performance_level"] = np.where(
#    (features["score"] >= 90),"Excellent",
#    np.where(features["score"]>= 80,"Good",
#             np.where(features["score"]>= 70,"Avarage","Need Improvement"))
#)

#features["seniority"] = pd.cut(
#    features["experience"],
#    bins = [0,3,7,14,float("inf")],
#    labels = ["junior","Mid","Senior","Expert"]
#)

#features["risk_flag"] = np.where(
#    (features["age"]<25) |
#    (features["score"]<70)|
#    (features["experience"]==0),1,0
#)

#features["ml_eligible"] = np.where(
#    (features["score"]>=70) &
#    (features["experience"]>=2) &
#    (features["age"] >=18),"yes","No"
#)
#features = features.assign(
#    salary_k = features["salary"] / 1000,
#    age_squared = features["age"] ** 2,
#    score_normalized = features["score"] / 100
#)
#X = features[
#    [
#        "age",
#        "salary",
#        "score",
#        "department",
#        "experience",
#        "department_code",
#        "salary_k",
#        "age_squared",
#        "experience_ratio",
#        "salary_per_experience",
#        "score_normalized",
#        "age_group",
#        "salary_quartiles",
#        "high_value_flag",
#        "performance_level",
#        "seniority",
#        "risk_flag",
#        "ml_eligible"
#    ]
#]
#print(X)

                                  #RENAME COLUMNS/INDEX:----->

#import pandas as pd
#import numpy as np

#df = pd.DataFrame({
#    "User ID": [101, 102, 103, 104, 105, 106, 107, 108],
#    "Employee Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry"],
#    "Age": [22, 31, 17, 45, 29, 52, 36, 27],
#    "Annual Salary": [45000, 80000, 120000, 60000, 75000, 150000, 90000, 65000],
#    "Score": [78, 92, 105, -10, 85, 97, 88, 72],
#    "Department Name": ["AI", "ML", "AI", "Unknown", "ML", "Data", "AI", "ML"]
#})

#df = df.rename(
#    columns= lambda x : x.lower().replace(" ","_")
#)
#print(df)

#features = df.copy()
#features = features.rename(
#    columns = {"Annual Salary": " salary",
#               "Department Name": "department",
#               "Score": "performance_score"
#               }
#)
#print(features)

#features = df.copy()
#features = features.rename(
#    columns = {
#        "annual_salary": "salary",
#        "department_name": "department"
#    }
#)
#features.loc[features["age"]<18,"age"] = 18
##features.loc[features["score"]<0,"score"] = 0
#features.loc[features["score"]>100,"score"] = 100

#features["salary_k"] = features["salary"] / 1000
#features["age_squared"] = features["age"] ** 2
#features["department_code"] = features["department"].map(
#    {"AI":0,
#     "ML":1,
#     "Data":2,
#     "unknown":-1
#    }
#)

#df = pd.DataFrame({
#    "Department": ["AI", "ML", "AI", "Data"],
#    "Salary": [50000, 70000, 90000, 60000]
#})
#df["Department"] = df["Department"].replace(
#    {"AI": "Artificial Intelligence",
#     "ML": "Machine Learning",
#     "Data": "Data Science"
#    }
#)
#df = df.rename(columns = {
#        "Department": "department",
#        "Salary":"salary"
#    }
#)
#print(df)

#df = pd.DataFrame({
#    "Salary": [50000, 80000, 120000],
#    "Score": [70, 95, 110]
#}, index=["emp_a", "emp_b", "emp_c"])

#df1 = df.copy()
#df1 = df1.rename(
#    columns = {
#        "emp_a": "employee_101",
#        "emp_b": "employee_102",
#        "emp_c": "employee_103"
#    }
#)
#df1.loc[df1["Score"]>100,"Score"]=100
#df1["salary_k"] = df1["Salary"]/1000
#print(df1)



#df = pd.DataFrame({
#    "USER_ID": [1, 2],
#    "FIRST_NAME": ["Alice", "Bob"],
#    "ANNUAL_SALARY": [50000, 70000],
#    "DEPARTMENT_NAME": ["AI", "ML"]
#})
#df = df.rename(
#    columns = lambda x : x.lower()
#)

#df = pd.DataFrame({
#    "User ID": [101, 102, 103, 104, 105, 106, 107, 108],
#    "Employee Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry"],
#    "Age": [22, 31, 17, 45, 29, 52, 36, 27],
#    "Annual Salary": [45000, 80000, 120000, 60000, 75000, 150000, 90000, 65000],
#    "Score": [78, 92, 105, -10, 85, 97, 88, 72],
#    "Department Name": ["AI", "ML", "AI", "Unknown", "ML", "Data", "AI", "ML"]
#})
#df["Experience Year"] = [3,4,5,6,7,8,9,2]
#features = df.copy()
#features = features.rename(
#    columns = lambda x : x.lower().replace(" ", "_")
#)
#print(features)

#features = features.rename(
#    columns = {
#        "annual_salary": "salary",
#        "department_name": "department",
#        "experience_year": "experience"
#    }
#)
#features.loc[features["age"]<18,"age"] = 18
#features.loc[features["score"]<0,"score"] = 0
#features.loc[features["score"]>100,"score"] = 100
#features["department"] = features["department"].map(
#    {
#        "AI":0,
#        "ML":1,
#        "Data":2,
#        "Unknown":-1
#    }
#)

#features["salary_k"] = features["salary"] / 1000
#features["age_squared"] = features["age"] ** 2

#features["high_value"] = ((features["salary"]>=80000) &
#                          (features["score"]>=90))



#x = features[
#    ["user_id",
#    "employee_name",
#    "age",
#    "salary",
#    "high_value",
#    "score",
#    "department"]
#]
#print(x)

#import pandas as pd
#df1 = pd.DataFrame({
#    "USER ID": [101, 102, 103, 104, 105, 106, 107, 108],
#    "EMPLOYEE NAME": [
#        "Alice", "Bob", "Charlie", "David",
#        "Eva", "Frank", "Grace", "Henry"
#    ],
#    "AGE YEARS": [17, 31, 45, 16, 29, 52, 36, 27],
#    "ANNUAL SALARY ($)": [
#        45000, 80000, 120000, 60000,
#        75000, 150000, 90000, 65000
#    ],
#    "PERFORMANCE SCORE": [78, 92, 105, -10, 85, 97, 88, 72],
#    "DEPARTMENT NAME": [
#        "AI", "ML", "AI", "Unknown",
#        "ML", "Data", "AI", "ML"
#    ],
#    "EXPERIENCE YEARS": [0, 3, 10, 0, 5, 15, 8, 2]
#})
#original_df = df1.copy()
#df = df1.copy()
#df = df.rename(
#    columns = lambda x : x.lower().replace(" ","_")
#)

#df = df.rename(
#    columns = {
#        "age_years":"age",
#        "annual_salary_($)":"salary",
#        "performance_score":"score",
#        "department_name":"department",
#        "experience_years":"experience"
#    }
#)
#df.loc[df["age"]<18,"age"] = 18
#df.loc[df["score"]<0,"score"] = 0
#df.loc[df["score"]>100,"score"] = 100

#df["department_code"] = df["department"].map(
#    {
#        "AI":0,
#        "ML":1,
#        "Data":2,
#        "Unknown":-1
#    }
#)
#df["salary_k"] = df["salary"]/1000
#df["age_squared"] = df["age"]**2
#df["experience_ratio"] = df["experience"]/df["age"]
#df["score_normalised"] = df["score"]/100

#df["high_value_flag"] = (df["salary"]>=80000) & (df["score"]>=90) & (df["experience"]>=5)

#df["performance_level"] = pd.cut(
#    df["score"],
#    bins = [float("-inf"),69,79,89,float("inf")],
#    labels = ["Needs Improvement","Average","Good","Excellent"]
#)

#df["age_group"] = pd.cut(
#    df["age"],
#    bins = [18,31,41,51,float("inf")],
#    labels = ["young","Mid","Senior","old"]
#)

#df["salary_quartile"] = pd.qcut(
#    df["salary"],
#    4,
#    labels = ["Q1","Q2","Q3","Q4"]
#)
#x = df[
#    [
#        "age",
#        "salary",
#        "experience",
#        "score",
#        "department",
#        "salary_k",
#        "experience_ratio",
#        "score_normalised",
#        "age_squared",
#        "high_value_flag",
#        "performance_level",
#        "age_group",
#        "salary_quartile"
#    ]
#]
#print(x)
#df.isna().sum()
#df["score"].between(0,100).all()
#df["user_id"].duplicated().any()
#df.shape
#x.shape


                           #DELETING COLUMNS :--------->
#import pandas as pd

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104],
#    "name": ["Alice", "Bob", "Charlie", "David"],
#    "age": [25, 31, 42, 29],
#    "salary": [60000, 85000, 120000, 70000],
#    "department": ["AI", "ML", "Data", "AI"],
#    "target": [0, 1, 1, 0],
#    "temp_score": [0.72, 0.91, 0.88, 0.65]
#})

#features = df.copy()
#features = features.drop(columns =["user_id","name","target"])
#print(features)
#features =  features[["age","department","salary","temp_score"]]
##target = df["target"]
#print(df)
#print(features.columns)
#print(target)
#print(df.columns)

#import pandas as pd

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104],
#    "name": ["Alice", "Bob", "Charlie", "David"],
#    "age": [25, 31, 42, 29],
#    "salary": [60000, 85000, 120000, 70000],
#    "department": ["AI", "ML", "Data", "AI"],
#    "target": [0, 1, 1, 0],
#    "temp_score": [0.72, 0.91, 0.88, 0.65]
#})

#original_df = df.copy()
#features = df.copy()
#target = df["target"]
#features = features.drop(columns = ["user_id","name","target"],errors="ignore")
#temp_score = features.pop("temp_score")
#features = features[["age","department","salary"]]
#print(features)
#print(df.columns)
#print(features.columns)
#print(target)
#print(df.equals(original_df))


#import pandas as pd

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104, 105],
#    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#    "age": [25, 31, 42, 29, 36],
#    "salary": [60000, 85000, 120000, 70000, 95000],
#    "department": ["AI", "ML", "Data", "AI", "ML"],
#    "target": [0, 1, 1, 0, 1],
#    "temp_score": [0.72, 0.91, 0.88, 0.65, 0.95],
#    "debug_flag": [True, False, True, False, True]
#})

#original_df = df.copy()
#features = df.copy()
#target = df["target"]
#features = features.drop(columns = ["user_id","name","target","debug_flag"],errors="ignore")
#temp_score = features.pop("temp_score")
#features = features[["age","department","salary"]]
#print(df.columns)
#print(features)
##print(target)
#print(temp_score)
#print(df.equals(original_df))

#                           PART 5 SHORTING AND INDEX FRAME.
#SORTING DATAFRAMES:--------->
#import pandas as pd

#df = pd.DataFrame({
#    "employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
#    "department": ["AI", "ML", "AI", "ML", "AI", "ML"],
#    "salary": [90000, 85000, 90000, 70000, 70000, 85000],
#    "performance": [92, 88, 95, 88, 91, 94]
#})


#ranked_df = df.sort_values(["department","performance","salary"],
#               ascending=[True,False,False]
#               )
#print(ranked_df)

#predictions = pd.DataFrame({
#    "prediction": ["cat", "dog", "cat", "bird", "dog", "cat"],
#    "confidence": [0.91, None, 0.87, 0.99, 0.72, None],
#    "model": ["A", "B", "A", "C", "B", "A"]
#})
#ranked_prediction = predictions.sort_values(["confidence","model"],
#                                   ascending = [False,True],
#                                   na_position="last").head(4)
#print(ranked_prediction)


#customers = pd.DataFrame({
#    "customer": ["alice", "Bob", "CHARLIE", "david", "EVA"],
#    "revenue": [5000, 9000, 7000, 9000, 6000],
#    "orders": [10, 15, 12, 15, 8]
#})
#ranked_customer = customers.sort_values("customer",
#                                        key= lambda x: x.str.lower(),
#                                        ascending =True)
#print(ranked_customer)

#predictions = pd.DataFrame({
#    "sample_id": [103, 101, 105, 102, 104],
#    "confidence": [0.80, 0.95, 0.80, 0.95, 0.70],
#    "prediction": ["cat", "dog", "bird", "cat", "dog"]
#})

#pre = predictions.sort_values(["confidence"],
#                              ascending = False,
#                              kind = "stable",).head(3)
#print(pre)

#df = pd.DataFrame({
#    "candidate": ["Alice", "Bob", "Charlie", "David", "Eva"],
#    "score": [91, 85, 91, 78, 85],
#    "experience": [5, 8, 3, 10, 6]
#}, index=[104, 101, 105, 102, 103])

#index_sorted = df.sort_index(ascending = True)
#print(index_sorted)

#ranked = df.sort_values(["score","experience","candidate"],
#                        ascending = [False,False,True])
#print(ranked)


#import pandas as pd
#models = pd.DataFrame({
#    "model": ["BERT", "GPT", "Llama", "Claude", "Gemma", "Mistral"],
#    "accuracy": [0.91, 0.95, 0.91, 0.95, None, 0.91],
#    "latency_ms": [120, 300, 100, 250, 80, 100],
#    "model_size": [110, 175, 70, 200, 27, 70]
#})
#top_models = models.sort_values(["accuracy","latency_ms","model_size"],
#                                 na_position = "last",
#                                ascending = [False,True,True]
#                                ).head(4)
#print(top_models)

#employees = pd.DataFrame({
#    "department": ["AI", "ML", "AI", "Data", "ML", "AI", "Data"],
#    "employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
#   "salary": [90000, 85000, 90000, 75000, 95000, 80000, 75000],
#    "performance": [92, 88, 95, 91, 88, 92, 91]
#})

#ranked = employees.sort_values(["department","performance","salary","employee"],
#                               ascending = [True,False,False,True])
#print(ranked)

#predictions = pd.DataFrame({
#    "sample_id": [107, 102, 109, 101, 105, 103, 110],
#    "confidence": [0.82, 0.95, 0.82, None, 0.95, 0.82, None],
#    "model": ["B", "A", "C", "D", "B", "A", "C"]
#})
#final_predictions = predictions.sort_values(["confidence"],
#                                            na_position = "last",
#                                            kind = "stable",
#                                            ascending = False).head(5)
#print(final_predictions)

#                             #nlargest-------------->

#models = pd.DataFrame({
#    "model": ["A", "B", "C", "D", "E", "F"],
#    "accuracy": [0.91, 0.95, 0.91, 0.97, 0.95, 0.89],
#    "latency_ms": [100, 250, 80, 300, 150, 70]
#})

#top_3_models = models.nlargest(3,["accuracy","latency_ms"])
#print(top_3_models)

#employees = pd.DataFrame({
#    "employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
#    "salary": [90000, 70000, 85000, 70000, 60000, 80000],
#    "experience": [5, 8, 3, 10, 4, 6]
#})
#lowest_paid = employees.nsmallest(3,
#                                  ["salary","experience"],
#                                  )
#print(lowest_paid)



#INDEX MANAGEMENT:------->

#import pandas as pd

#users = pd.DataFrame({
#    "user_id": [104, 101, 103, 102],
#    "name": ["David", "Alice", "Charlie", "Bob"],
#    "score": [82, 95, 88, 91]
#})
#users = users.set_index("user_id")
#users_102 = users.loc[102]
#users_2 = users.iloc[2]
#users = users.reset_index
#print(users)

#import pandas as pd
#df = pd.DataFrame({
#    "score": [90, 75, 95, 80],
#    "status": ["A", "B", "A", "C"]
#}, index=["D", "B", "A", "C"])

#sorted_df = df.sort_index()
#print(sorted_df)

#reindex_df = df.reindex(["D", "A", "C", "B"])
#print(reindex_df)
#in the sorted index sequenced alphabetically and the same alphabet one is at end but in reindexing we arrange it by ourself.

#products = pd.DataFrame({
#    "price": [100, 200, 300],
#    "stock": [10, 5, 8]
#}, index=["P101", "P102", "P103"])

#result = products.reindex(["P103", "P101", "P999","P102"])
#print(result)

#employees = pd.DataFrame({
#    "department": ["AI", "AI", "ML", "ML", "Data", "Data"],
#    "employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
#    "salary": [90000, 85000, 95000, 80000, 75000, 82000],
#    "score": [95, 88, 92, 85, 90, 87]
#})

#employees = employees.set_index(["department","employee"])
#emp = employees.loc["AI"]
#print(emp)
#empo = employees.loc[("AI","Alice")]
#print(empo)
#ml_emp = employees.loc["ML"]
#print(ml_emp)
#sorting = employees.sort_index()
#print(sorting)

#df = pd.DataFrame({
#    "name": ["Alice", "Bob", "Charlie"],
#    "score": [95, 85, 90]
#}, index=["emp_101", "emp_102", "emp_103"])

#df.index.name = "employee_id"
#df = df.rename(index = {
#    "emp_101":"E101",
#    "emp_102":"E102",
#    "emp_103":"E103"
#})
#print(df)
#df = df.sort_index()
#user = df.loc["E102"]
#print(user)

#import pandas as pd
#df = pd.DataFrame({
#    "department": ["ML", "AI", "AI", "Data", "ML", "AI", "Data"],
#    "employee_id": [105, 102, 101, 106, 103, 104, 107],
#    "employee": ["Eva", "Bob", "Alice", "Frank", "Charlie", "David", "Grace"],
#    "score": [88, 95, 91, 82, 90, 97, 85],
#    "salary": [85000, 90000, 95000, 75000, 88000, 100000, 78000]
#})

#df = df.set_index(["department", "employee_id"])
#df = df.sort_index()
#ai_employees = df.loc["AI"]
#print(ai_employees)
#emp_104 = df.loc["AI",104]
#print(emp_104)
#required = df.reindex([("AI",104),("AI",101),("AI",999),("ML",103),("ML",105)])
#final_df = required
#print(final_df)
#reset_df = df.reset_index()
#print(df)

#print(final_df)

#import pandas as pd

#df = pd.DataFrame({
#    "team": ["AI", "ML", "AI", "Data", "ML", "AI", "Data", "ML"],
#    "region": ["UK", "US", "US", "UK", "UK", "UK", "US", "US"],
#    "employee_id": [104, 201, 101, 301, 202, 103, 302, 203],
#    "employee": [
#        "David", "John", "Alice", "Eva",
#        "Mike", "Bob", "Frank", "Sarah"
#    ],
#    "score": [97, 88, 95, 82, 91, 90, 85, 94],
#    "salary": [100000, 85000, 95000, 72000, 90000, 88000, 76000, 93000]
#})
#original_df = df.copy()
#df = df.set_index(["team", "region", "employee_id"])
#df = df.sort_index()
#ai_employees = df.loc["AI"]
#ai_uk = df.loc[("AI","UK")]
#bob = df.loc[("AI","UK", 103)]
#print(bob)

#required = df.reindex([("ML", "US", 203),
#    ("AI", "UK", 104),
#    ("AI", "US", 999),
#    ("Data", "UK", 301),
#    ("ML", "US", 201)
#])
#final_df = required
#flat_df = df.reset_index()
#print(df.reset_index().equals(original_df))

#import pandas as pd

#df = pd.DataFrame({
#    "department": ["ML", "AI", "Data", "AI", "ML", "Data"],
#    "region": ["US", "UK", "UK", "US", "UK", "US"],
#    "employee_id": [202, 101, 301, 102, 201, 302],
#    "employee": ["Mike", "Alice", "Eva", "Bob", "John", "Frank"],
#    "score": [91, 95, 82, 88, 94, 85],
#    "salary": [90000, 95000, 72000, 88000, 93000, 76000]
#})
#original_df = df.copy()
#df = df.set_index(["department","region","employee_id"])
#df = df.sort_index()
#ai = df.loc["AI"]
#ai_uk = df.loc[("AI","UK")]
#bob = df.loc[("AI","US",102)]
#print(bob)
#required = df.reindex([
#("ML", "UK", 201),
#    ("AI", "US", 102),
#    ("AI", "UK", 999),
#    ("Data", "UK", 301),
 #   ("ML", "US", 202)
#])
#final_df = required
#flat_df = df.reset_index()
#print(flat_df)
#print(df.reset_index().equals(original_df))


#DATA CLEANING:------->

#import pandas as pd
#import numpy as np

#df = pd.DataFrame({
#    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#    "age": [25, np.nan, 32, 29, np.nan],
#    "salary": [60000, 75000, np.nan, 82000, np.nan],
#    "department": ["AI", "ML", np.nan, "AI", "ML"]
#})
#print(df)
#missing = df.isna().sum()
#print(missing)
#percentage = df.isna().mean()*100
#print(percentage)
#total_missing = df.isna().sum().sum()
#print(total_missing)

##Q2
#one_missing = df.isna().any(axis=1)
#print(one_missing)
#no_value = df.notna().all(axis=1)
#print(no_value)

#Q3
#df = pd.DataFrame({
#    "age": [25, 30, np.nan, 40, 35, np.nan],
#    "salary": [50000, np.nan, 70000, 80000, np.nan, 90000]
#})

#df["age"] = df["age"].fillna(df["age"].median())
#print(df)

#df["salary"] = df["salary"].fillna(df["salary"].mean())
#print(df)

#import pandas as pd
#import numpy as np

#df = pd.DataFrame({
#    "employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
#    "department": ["AI", "ML", np.nan, "AI", np.nan],
#    "city": ["London", np.nan, "London", "Paris", np.nan]
#})
#df["department_missing"] = df["department"].isna().astype(int)
#df["city_missing"] = df["city"].isna().astype(int)
#df["department"] = df["department"].fillna("unknown")
#df["city"] = df["city"].fillna("unknown")
#print(df)


#import pandas as pd
#import numpy as np
#df = pd.DataFrame({
#    "name": ["A", "B", "C", "D", "E"],
##    "age": [25, np.nan, 30, np.nan, 40],
#    "salary": [60000, np.nan, 70000, 80000, np.nan],
#    "score": [90, 85, np.nan, np.nan, 95]
#})

#any_value = df.dropna()
#print(any_value)
#drop_rows = df.dropna(subset=["salary","age"],
#                     how = "all")
#print(drop_rows)

#both = df.dropna(thresh=2)
#print(both)


#import pandas as pd
#import numpy as np
#df = pd.DataFrame({
#    "day": [1, 2, 3, 4, 5, 6],
#    "temperature": [20, np.nan, np.nan, 25, np.nan, 30]
#})
#df["forward"] = df["temperature"].ffill()
#df["backward"] = df["temperature"].bfill()
#df["interpolated"] = df["temperature"].interpolate().round(0)
#print(df)

#import pandas as pd
#import numpy as np

#train = pd.DataFrame({
#    "age": [20, 25, 30, np.nan, 40],
#    "salary": [40000, 50000, np.nan, 70000, 80000]
#})

#test = pd.DataFrame({
#    "age": [22, np.nan, 35],
#    "salary": [45000, 60000, np.nan]
#})

#train_mean = train["age"].mean()
#print(train_mean)
#train_median = train["salary"].median()
#print(train_median)
#train["age"] = train["age"].fillna(train_mean)
#train["salary"] = train["salary"].fillna(train_median)
#test["age"] = test["age"].fillna(train_mean)
#test["salary"] = test["salary"].fillna(train_median)
#print(train)
#print(test)

#import pandas as pd
#import numpy as np
#df = pd.DataFrame({
#    "age": [25, np.nan, 30, np.nan, np.nan],
#    "salary": [50000, 60000, np.nan, np.nan, np.nan],
#    "score": [90, 80, 70, 60, 50],
#    "city": ["London", np.nan, "Paris", np.nan, np.nan]
#})

#missing_report = pd.DataFrame({
#    "columns":df.columns,
#    "missing_count": df.isna().sum().values,
#    "missing_percentage": (df.isna().mean()*100).values
#})
#missing_report  = missing_report.sort_values("missing_percentage",
#                                             ascending = True)
#print(missing_report)

#result = missing_report[
#    missing_report["missing_percentage"]>40
#]
#print(result)

#import pandas as pd
#import numpy as np
#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104, 105, 106],
#    "age": [25, np.nan, 35, np.nan, 45, 50],
#    "salary": [50000, 60000, np.nan, 80000, np.nan, 100000],
#    "department": ["AI", "ML", np.nan, "AI", "ML", np.nan],
#    "score": [90, np.nan, 85, 70, np.nan, 95]
#})
#df["age_missing"] = df["age"].isna().astype(int)
#df["salary_missing"] = df["salary"].isna().astype(int)

#df["age"] = df["age"].fillna(df["age"].median())
#df["salary"] = df["salary"].fillna(df["salary"].median())
#df["department"] = df["department"].fillna("unknown")
#df["new_score"] = df["score"].mean()
#df["score"] = df["score"].fillna(df["new_score"])
#x = df[
#    [
#"age",
#"salary",
#"department",
#"score",
#"age_missing",
#"salary_missing"
#    ]
#]
#print(x)


#import pandas as pd
#import numpy as np

#import pandas as pd
#import numpy as np

#df1 = pd.DataFrame({
#    "user_id": [101, 102, 103, 104, 105, 106, 107, 108],
#    "age": [25, np.nan, 35, 40, np.nan, 50, 29, np.nan],
#    "income": [50000, 60000, np.nan, 90000, 75000, np.nan, 55000, 100000],
#    "experience": [2, np.nan, 8, 12, 6, 20, np.nan, 15],
#    "department": ["AI", "ML", np.nan, "Data", "AI", np.nan, "ML", "AI"],
#    "score": [90, 85, np.nan, 95, 70, np.nan, 88, 92],
#    "city": ["London", np.nan, "Paris", "London", np.nan, "Berlin", "London", np.nan],
#    "target": [1, 0, 1, 1, 0, 1, 0, 1]
#})

#original_df = df1.copy()
#df = df1.copy()
#df["age_missing"] = df["age"].isna().astype(int)
#df["income_missing"] = df["income"].isna().astype(int)
#df["experience_missing"] = df["experience"].isna().astype(int)
#df["department_missing"] = df["department"].isna().astype(int)
#df["city_missing"] = df["city"].isna().astype(int)
#df["score_missing"] = df["score"].isna().astype(int)

#df["age"] = df['age'].fillna(df["age"].median())
#df["income"] = df["income"].fillna(df["income"].median())
#df["experience"] = df["experience"].fillna(df["experience"].median())
#df["score"] = df["score"].fillna(df["score"].mean())

#df["department"] = df["department"].fillna("unknown")
#df["city"] = df["city"].fillna("unknown")
#print(df.isna().sum())

#y = df["target"]
#df = df.dropna(subset="user_id")
#x = df[[
#"age",
#    "income",
#    "experience",
#    "department",
#    "city",
#    "score",
#    "age_missing",
#    "income_missing",
#    "experience_missing",
#    "department_missing",
#    "city_missing",
#    "score_missing",
#]]
#print(x.isna().sum().sum()==0)
#print("target"not in x.columns)
#print("user_id"not in x.columns)
#print(x.shape[0]==y.shape[0])


#import pandas as pd
#import numpy as np

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104, 105, 106, 107, 108],
#    "age": [25, np.nan, 35, 40, np.nan, 50, 29, np.nan],
#    "income": [50000, 60000, np.nan, 90000, 75000, np.nan, 55000, 100000],
#    "experience": [2, np.nan, 8, 12, 6, 20, np.nan, 15],
#    "department": ["AI", "ML", np.nan, "Data", "AI", np.nan, "ML", "AI"],
#    "score": [90, 85, np.nan, 95, 70, np.nan, 88, 92],
#    "city": ["London", np.nan, "Paris", "London", np.nan, "Berlin", "London", np.nan],
#    "target": [1, 0, 1, 1, 0, 1, 0, 1]
#})

#original_df = df.copy()
#x = df.copy()

#x["age_missing"] = x["age"].isna().astype(int)
#x["income_missing"] = x["income"].isna().astype(int)
#x["experience_missing"] = x["experience"].isna().astype(int)
#x["department_missing"] = x["department"].isna().astype(int)
#x["city_missing"] = x["city"].isna().astype(int)
#x["score_missing"] = x["score"].isna().astype(int)

#x["age"] = x["age"].fillna(x["age"].median())
#x["income"] = x["income"].fillna(x["income"].median())
#x["experience"] = x["experience"].fillna(x["experience"].median())
#x["score"] = x["score"].fillna(x["score"].mean())

#x["department"] = x["department"].fillna("Unknown")
#x["city"] = x["city"].fillna("Unknown")

#print(x.isna().sum())

#y = x["target"]
#X = x[[
#"age",
#"income",
#"experience",
#"department",
#"score",
#"city",
#"age_missing",
#"income_missing",
#"experience_missing",
#"department_missing",
#"city_missing",
#"score_missing"
#]]

#print(X.isna().sum().sum()==0)
#print("target"not in X.columns)
#print("user_id"not in X.columns)
#print(X.shape[0]==y.shape[0])

#import pandas as pd
#import numpy as np

#df1 = pd.DataFrame({
#    "user_id": [1, 2, 3, 4, 5, 6, 7, 8],
#    "age": [22, np.nan, 35, np.nan, 42, 29, np.nan, 50],
##    "income": [30000, 45000, np.nan, 80000, np.nan, 60000, 70000, np.nan],
#    "experience": [1, 3, np.nan, 10, 15, np.nan, 7, 20],
#    "department": ["AI", "ML", np.nan, "AI", "Data", np.nan, "ML", "AI"],
#    "score": [75, 82, np.nan, 95, 88, np.nan, 91, 97],
#    "city": ["London", "Paris", np.nan, "London", "Berlin", np.nan, "Paris", "London"],
#    "target": [0, 1, 1, 1, 0, 0, 1, 1]
#})

#original_df = df1.copy()
#df = df1.copy()
#print(df)

#df["age_missing"] = df["age"].isna().astype(int)
#df["income_missing"] = df["income"].isna().astype(int)
#df["experience_missing"] = df["experience"].isna().astype(int)
#df["department_missing"] = df["department"].isna().astype(int)
#df["score_missing"] = df["score"].isna().astype(int)
#df["city_missing"] = df["city"].isna().astype(int)
#print(df)

#df["age"] = df["age"].fillna(df["age"].median())
#df["income"] = df["income"].fillna(df["income"].median())
#df["experience"] = df["experience"].fillna(df["experience"].median())
#df["score"] = df["score"].fillna(df["score"].mean())
##df["department"] = df['department'].fillna(df["department"].mode()[0])
#df["city"] = df["city"].fillna("unknown")

#Y = df["target"]
#print(df.isna().sum().sum())

#X = df[
#    [
#        "age",
#        "income",
#        "experience",
#        "department",
#        "score",
#        "city",
#        "age_missing",
#        "income_missing",
#        "experience_missing",
#        "department_missing",
#        "city_missing",
#        "score_missing",

#    ]
#]

#                               DUPLICATE DATA:------->

#import pandas as pd

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 103, 104],
#    "name": ["Alice", "Bob", "Charlie", "Charlie", "David"],
#    "age": [25, 30, 35, 35, 40]
#})

#print(df.duplicated())
#print(df["user_id"].duplicated(keep=False))
#print(df[df["user_id"].duplicated(keep=False)])


#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 103, 103, 104],
#    "name": ["Alice", "Bob", "Charlie", "Charlie", "Charlie", "David"],
#    "score": [90, 80, 95, 97, 99, 85]
#})

#print(df["user_id"].duplicated(keep=False))
#print(df[df["user_id"].duplicated(keep=False)])

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 103, 104, 105],
#    "name": ["Alice", "Bob", "Charlie", "Charlie", "David", "Eva"],
#    "email": [
#        "alice@gmail.com",
#        "bob@gmail.com",
#        "charlie@gmail.com",
#        "charlie@gmail.com",
#        "david@gmail.com",
#        "eva@gmail.com"
#    ],
#    "score": [90, 80, 95, 99, 85, 88]
#})

#print(df["user_id"].duplicated(keep=False))
#clean_df = df.drop_duplicates(keep="last",
#                              subset=["user_id"])
#print(clean_df)


#df = pd.DataFrame({
#    "user_id": [101, 101, 102, 103, 103, 103, 104],
#    "transaction_id": ["T1", "T2", "T3", "T4", "T4", "T5", "T6"],
#    "amount": [50, 80, 100, 200, 200, 300, 150]
#})

#print(df["user_id"].duplicated(keep=False))
#print(df["transaction_id"].duplicated(keep=False))
#print(df["amount"].duplicated(keep=False))

#import pandas as pd
#from pandas import Int64Dtype

#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 103, 104, 105, 105, 105, 106],
#    "email": [
#        "a@gmail.com",
#        "b@gmail.com",
#        "c@gmail.com",
#        "c@gmail.com",
#        "d@gmail.com",
#        "e@gmail.com",
#        "e@gmail.com",
#        "e@gmail.com",
#        "f@gmail.com"
#    ],
#    "name": [
#        "Alice",
#        "Bob",
#        "Charlie",
#        "Charlie",
#        "David",
#        "Eva",
#        "Eva",
#        "Eva",
#        "Frank"
#    ],
#    "score": [90, 80, 95, 97, 85, 88, 88, 92, 75],
#    "country": [
#        "UK",
#        "USA",
#        "France",
#        "France",
#        "UK",
#        "Germany",
#        "Germany",
#        "Germany",
#        "UK"
#    ]
#})
#original_df = df.copy()
#print(df["user_id"].duplicated(keep = False))
#print(df[df["user_id"].duplicated(keep = False)])

#clean_df= df.drop_duplicates(keep = "last",
#                              subset = "user_id"
#                        )
#print(clean_df)
#print(clean_df["user_id"].duplicated().any())
#print(df.equals(original_df))

#original_df = df.copy()
#df["user_id"].duplicated(keep=False)
#print(df[df["user_id"].duplicated(keep=False)])
#duplicate_report = (
#    df["user_id"]
#                    .value_counts()
#                    .loc[lambda x : x>1]
#.reset_index()
#)
#print(duplicate_report)
#clean_df = df.drop_duplicates(keep="last",
#                              subset = ["user_id"])
#print(clean_df)
#print(clean_df["user_id"].duplicated().any())
#print(df.equals(original_df))

#DATA TYPES:--------->

#import pandas as pd

#df = pd.DataFrame({
#    "age": [25, 30, 35],
#    "salary": [50000.0, 60000.5, 70000.0],
#    "name": ["Alice", "Bob", "Charlie"],
#    "active": [True, False, True]
#})

#print(df.dtypes)
#print(df.info())
#df["age"] = df["age"].astype("string")
#print(df["age"].dtype)

#Q2
#import pandas as pd
#df = pd.DataFrame({
#    "age": ["25", "30", "35"],
#    "score": ["85.5", "90.0", "72.5"]
#})

#df["age"] = (df["age"].astype(int))
#print(df["age"])
#df["score"] = df['score'].astype(float)
#print(df["score"])

#Q3
#df = pd.DataFrame({
#    "salary": ["50000", "60000", "unknown", "70000", "N/A"],
#    "experience": ["2", "5", "3", "unknown", "8"]
#})
#print(df)
#df["salary"] = pd.to_numeric(df["salary"],
#                             errors = "coerce"
#                             )
#df["experience"] = pd.to_numeric(df["experience"],
#                                 errors = "coerce")
#print(df)
#print(df.dtypes)
#print(df.isna().sum())

#Q4
#df = pd.DataFrame({
#    "start_date": [
#        "2025-01-01",
#        "2025-02-15",
#        "invalid",
#        "2025-04-10"
#    ],
#    "duration": [
#        "5 days",
#        "10 days",
#        "invalid",
#        "3 days"
#    ]
#})
#df["start_date"] = pd.to_datetime(df["start_date"],
#                                  errors = "coerce")
#print(df["start_date"])
#df["duration"] = pd.to_timedelta(df["duration"],
#                                 errors = "coerce")
#print(df["duration"])

#end_date = df["start_date"] + df["duration"]
#print(end_date)
#print(end_date.dtypes)

#Q5
#df = pd.DataFrame({
#    "age": [25, 30, None, 42],
#    "verified": [True, False, None, True]
#})
#df["age"] = df["age"].astype("Int64")
#df["verified"] = df["verified"].astype("boolean")
#print(df)

#Q6
#df = pd.DataFrame({
#    "user_id": range(1, 11),
#    "country": [
#        "UK", "USA", "UK", "India", "USA",
#        "UK", "India", "UK", "USA", "UK"
#    ],
#    "email": [
#        "a@test.com", "b@test.com", "c@test.com",
#        "d@test.com", "e@test.com", "f@test.com",
#        "g@test.com", "h@test.com", "i@test.com", "j@test.com"
#    ]
#})
#df["country"] = df["country"].astype("category")
#df["email"] = df["email"].astype("string")
#print(df.dtypes)

#Q7

#df = pd.DataFrame({
#    "age": [18, 25, 32, 45, 60],
#    "salary": [25000, 50000, 75000, 100000, 150000],
#    "score": [0.72, 0.81, 0.91, 0.88, 0.95],
#    "department": [
#        "AI", "ML", "AI", "Data", "ML"
#    ]
#})
#print(df.memory_usage(deep = True))
#df["age"] = pd.to_numeric(df["age"],downcast = "integer")
#df["salary"] = pd.to_numeric(df["salary"],downcast = "integer")
#df["score"] = pd.to_numeric(df["score"],downcast = "float")
##df["department"] = df["department"].astype("category")
#df.memory_usage(deep = True)
#print(df.memory_usage(deep = True))

#df = pd.DataFrame({
#    "user_id": ["101", "102", "103", "104", "105"],
#    "age": ["25", "31", "unknown", "42", "29"],
#    "salary": ["60000", "85000", "N/A", "120000", "invalid"],
#    "join_date": [
#        "2025-01-10",
#        "2025-02-15",
#        "bad-date",
#        "2025-04-20",
#        "2025-05-01"
#    ],
#    "active": [
#        "True",
#        "False",
#        None,
#        "True",
#        "False"
#    ],
#    "department": [
#        "AI",
#        "ML",
#        "Data",
#        "AI",
#        "ML"
#    ]
#})
##print("nw----------->")
#print(df.memory_usage(deep=True).sum())
#df["user_id"] = pd.to_numeric(
#                              df["user_id"],
#                              downcast = "integer")
#df["age"] = pd.to_numeric(
#                          df["age"],
#                          errors = "coerce",
#                          downcast="integer")

#df["salary"] = pd.to_numeric(
#    df["salary"],
#    errors = "coerce",
#    downcast ="integer"
#)

#df["join_date"] = pd.to_datetime(df["join_date"],
#                                 errors ="coerce",
#                                 )
#df["active"] = df['active'].map({
#    "True": True,
#    "False": False
#}).astype("boolean")


#df["department"] = df["department"].astype("category")

#print(df)
#print(df.dtypes)
#print(df.isna().sum())
#print(df.memory_usage(deep=True).sum())


#import pandas as pd

#df = pd.DataFrame({
#    "user_id": ["101", "102", "103", "104", "105", "106"],
#    "age": ["25", "31", "unknown", "42", None, "29"],
#    "salary": [
#        "60000",
#        "85000",
#        "120000",
#        "invalid",
#        "95000",
#        "70000"
#    ],
#    "score": [
#        "91.5",
#        "87",
#        "unknown",
#        "95.2",
#        "88.0",
#        "invalid"
#    ],
#    "join_date": [
#        "2025-01-10",
#        "2025-02-15",
#        "bad-date",
#        "2025-04-20",
#        "2025-05-01",
#        None
#    ],
#    "experience": [
#        "2 years",
#        "5 years",
#        "3 years",
#        "10 years",
#        "7 years",
#        "invalid"
#    ],
#    "active": [
#        "True",
#        "False",
#        None,
#        "True",
#        "False",
#        "True"
#    ],
#    "department": [
#        "AI",
#        "ML",
#        "AI",
#        "Data",
#        "ML",
#        "AI"
#    ]
#})
#memory_before = df.memory_usage(deep = True).sum()
#print(memory_before)
#original_df = df.copy()
#clean_df = df.copy()
#clean_df["user_id"] = pd.to_numeric(df["user_id"].astype("Int32"))

#clean_df["age"] = pd.to_numeric(df["age"],
#                  errors = "coerce"
#                  ).astype("Int32")

#clean_df["salary"] = pd.to_numeric(df["salary"],
#                  errors = "coerce",
#                  downcast = "integer")

#clean_df["score"] = pd.to_numeric(df["score"],
#                  errors = "coerce",
#                  downcast = "float")

#clean_df["join_date"] = pd.to_datetime(df["join_date"],
#                   errors = "coerce")
#clean_df["experience"] = pd.to_timedelta(df["experience"],
#                                         errors = "coerce")

#clean_df["active"] = df["active"].map({
#        "True": True,
#        "False":False,
#    }).astype("boolean")

#clean_df["department"] = df["department"].astype("category")

#memory_after = clean_df.memory_usage(deep = True).sum()
#print(memory_after)
#print(df)
#print(clean_df["age"].dtype)
#print(clean_df["salary"].dtype)
#print(clean_df["score"].dtype)
#print(clean_df["join_date"].dtype)
#print(clean_df["experience"].dtype)
#print(clean_df["active"].dtype)
#print(clean_df["department"].dtype)
#print(df.isna().astype(int))


#STRING AND TEXT PROCESSING:---------->

#import pandas as pd

#df = pd.DataFrame({
#    "name": [
#        "  Alice Smith  ",
#        "BOB JONES",
#        "  charlie brown",
#        "Diana",
#        None,
#        "   EVE   ADAMS   "
#    ],
#    "email": [
#        " ALICE@GMAIL.COM ",
#        "bob@yahoo.com",
#        "CHARLIE@GMAIL.COM",
#        "diana@outlook.com",
#        None,
#        "EVE@GMAIL.COM"
#    ],
#    "department": [
#        " AI ",
#        "ML",
#        " ai",
#        "Data",
#        "ML",
#        "AI "
#    ],
#    "filename": [
#        "model.pdf",
#        "training.csv",
#        "README.txt",
#        "model.PDF",
#        None,
#        "dataset.csv"
#    ],
#    "text": [
#        "  Machine    Learning is amazing!  ",
#        "Python is widely used in AI.",
#        "   RAG   combines retrieval and generation. ",
#        None,
#        "Deep Learning is powerful.",
#       "LLMs are useful for GenAI."
#    ]
#})

#df["email"] = df["email"].str.lower()
#print(df["email"])

#df["department"] = df["department"].str.upper()
#print(df["department"])

#df["name"] = df["name"].str.strip()
#print(df["name"])

#df["email"] = df["email"].str.strip().str.lower()
#print(df["email"])

#df["name"] = df["name"].str.title().str.strip()
#print(df["name"])

#df["department"] = df["department"].str.upper()
#print(df["department"])

#df["is_email"] = df["email"].str.contains("gmail",case = False)
#print(df[df["is_email"]])

#df['is_filename'] = df["filename"].str.contains(".pdf",case = False)
#print(df["is_filename"])

#df["text"] = df["text"].str.strip()
#print(df["text"])

#df["is_text"] = df["text"].str.contains("AI",case = False,na = False)
#print(df["is_text"])

#df["is_csv"] = df["filename"].str.contains(".csv",case = False)
#print(df["is_csv"])

#df["text_length"] = df["text"].str.len()
#result = df[df["text_length"] > 30]
#print(result)

#df["clean_text"] = df["text"].str.strip().str.lower().str.replace("  ","")
#print(df["clean_text"])

#df["clean_name"] = df["name"].str.strip().str.lower().str.title()
#print(df["clean_name"])

#df["text_length"] = df["text"].str.len()
#result = df[df["text_length"]>30]
#print(result)

#df = pd.DataFrame({
#    "text": [
#        "   MACHINE     LEARNING   ",
#        "Deep    Learning",
#        "  Natural Language   Processing  ",
#        None,
#        "GENERATIVE     AI!!!"
#    ]
#})

#df["clean_text"] = (
#    df["text"]
#    .str.strip()
#    .str.lower()
#    .str.replace(r"\s+", " ", regex=True)
#)

#print(df["clean_text"])

#df = pd.DataFrame({
#    "text": [
#        "AI",
#        "Machine Learning is powerful",
#        "",
#        "   ",
#        None,
#        "Retrieval Augmented Generation is useful"
#    ]
#})
#df["clean_text"] = (df["text"]
#              .str.replace(r"\s+", " ", regex=True)
#              )
#print(df["clean_text"])


#df = pd.DataFrame({
#    "document_id": ["D1", "D2", "D3", "D4", "D5", "D6"],
#    "text": [
#        "   Retrieval     Augmented Generation is powerful!!!   ",
#        "LLMs   are changing    AI.",
#        "   ",
#        None,
#        "Machine Learning is used in production systems.",
#        "  PYTHON is widely used for machine learning.  "
#    ]
#})

#df["clean_text"] = (
#    df["text"]
#    .str.strip()
#    .str.lower()
#    .str.replace(r"\s+"," ",regex = True)
#)

#df["text_length"] = df["clean_text"].str.len()
#print(df["text_length"])

#df["has_ai"] = df["clean_text"].str.contains("ai",na = False)
#print(df["has_ai"])

#df["final_document"] = df["text_length"]>=20
#print(df[df["final_document"]])

#import re

#text = "I have 3 apples and 25 oranges."
#result = re.findall(r"\d+",text)
#print(result)

#text = "Contact me at john.doe@gmail.com"
#result = re.search(r"([\w.-]+@[\w.-]+\.\w+\b)",text)
#print(result)

#text = "AI is transforming healthcare"
#result = re.search(r"^AI",text)
#print(result)

#text = "User ID: ABC-12345"
#result = re.search(r"ABC-\d+",text)
#print(result)

#text = "Hello     world    AI"
#result = re.sub(r"\s+"," ",text)
#print(result)

#text = "Order 123 contains 45 items."
#result = re.findall(r"\d+",text)
#print(result)

#text = "hello AI_engineer 2026"
#result = re.findall(r"\w+",text)
#print(result)

##text = "Hello    AI   Engineer"
#result = re.findall(r"\s+" ,text)
#print(result)

#text = "cat bat hat mat"
#result = re.findall(r"[cb]\w+",text)
#print(result)

#text = "abc123XYZ"
#result = re.findall(r"[^\d]",text)
#print(result)

#text = "12 123 1234 12345 123456"
#result = re.findall(r"\d{3,5}",text)
#print(result)

#text = "AI is useful"
#result1 = re.search(r"^AI",text)
#result2 = re.search(r"useful$",text)
#result3 = re.search(r"\bAI\b",text)
#print([result1],[result2],[result3])

#text = "I use Python, Java, and C++."
#result = re.findall(r"Python|Java",text)
#print(result)

#text = "Name: John"
#esult = re.search(r"Name:\s*(\w+)",text)
#print(result.group(1))

#text = "Start hello End and Start world End"
#result = re.search(r"Start.*?End",text)
#result1 = re.search(r"Start.*End",text)
#print(result.group())

#text = "Hello     AI     Engineer"
#result = re.sub(r"\s+"," ",text)
#print(result)

#text = """
#Contact john.doe@gmail.com or support@company.co.uk
#"""
#result = re.findall(r"\b [\w.-]+@[\w.-]+\.\w+\b",text)
#print(result)


#import pandas as pd

#df = pd.DataFrame({
#    "text": [
#        "AI is amazing",
#        "Machine Learning is powerful",
#        "AI engineer salary is 120000",
#        None,
#        "RAG uses documents"
#    ],
#    "email": [
#        "john@gmail.com",
#        "alice@yahoo.com",
#        "bob@gmail.com",
#        None,
#        "sam@company.com"
#    ]
#})

#has_ai = df["text"].str.contains(
#    "AI",
#    case = False,
#    na = False
#                             )
#print(has_ai)

#salary  = df["text"].str.extract(r"(\d+)",expand=False).astype("Int64")
#print(salary)

#df["clean_text"] = (df["text"]
#              .str.strip()
#              .str.lower()
#              .str.replace(r"\s+"," ",regex=True))
#df["text_length"] = df["clean_text"].str.len()
#df['number'] = df["text"].str.findall(r"\d+")
#print(df)

#CATEGORIES AND ENCODING:-------->

#import pandas as pd

#df = pd.DataFrame({
#    "age": [22, 31, 45, 29, 38],
#    "department": ["Engineering", "HR", "Engineering", "Marketing", "HR"],
#    "experience": [1, 7, 20, 5, 12],
#    "seniority": ["Junior", "Senior", "Senior", "Mid", "Senior"],
#    "salary": [45000, 72000, 120000, 65000, 95000]
#})
#print(df["department"].nunique())
#print(df["seniority"].nunique())
#print(df["department"].value_counts())
#print(df["department"].value_counts(normalize = True)*100)
#df["department"] = df["department"].astype("category")
#df["seniority"] = df["seniority"].astype("category")
#print(df.dtypes)
#print(df["department"].cat.categories)
#print(df["department"].cat.codes)

#df["seniority"] = pd.Categorical(
#    df["seniority"],
#    categories = ["Junior","Mid","Senior"],
#    ordered = True
#)
#print(df["seniority"].cat.categories)

#df = pd.DataFrame({
#    "employee": ["A", "B", "C", "D"],
#    "department": ["Engineering", "HR", "Engineering", "Marketing"]
#})
#df_encoded = pd.get_dummies(df,
#                            columns =["department"],
#                            dtype = int)
#print(df_encoded)

#import numpy as np
#df = pd.DataFrame({
#    "customer_id": range(1, 11),
#    "country": [
#        "UK", "UK", "UK", "USA", "USA",
#        "India", "India", "Germany", "Brazil", "Brazil"
#    ]
#})
#count = df["country"].value_counts()
#rare = count[count<100].index
#df["country"] = df["country"].where(~df["country"].isin(rare),"others")
#print(df["country"])

#counts = df["country"].value_counts()
#df["country"] = df["country"].map(
#    lambda x: x if counts[x] >=100 else "Others"
#)
#print(df["country"])


#df = pd.DataFrame({
#    "employee": ["A", "B", "C", "D", "E"],
#    "department": [
#        "Engineering",
#        "HR",
#        "Marketing",
#        "Engineering",
#        "HR"
#    ]
#})

#df["department"] = df["department"].astype("category")

#filtered = df[df["department"] == "Engineering"].copy()
#print(filtered["department"].cat.categories)
#filtered["department"] = filtered["department"].cat.remove_unused_categories()
#print(filtered["department"].cat.categories)

#df["department"] = df["department"].cat.rename_categories(
#    {
#        "Engineering":"ENG",
#        "HR":"HUMAN RESOURCES",
#        "Marketing": "MKT"
#    }
#)
#print(df["department"].cat.categories)

#mapping = {
#    "Engineering": 1,
#    "HR": 2,
#    "Marketing": 3
#}

#df["department_code"] = df["department"].map(mapping)

#these departments are not ordinal these are nominal we have to use the one hot encoding instead of this. use pd.get_dummy here.
#This type of mapping is appropriate when we have the categorical ordinal like high mid low.
#one hot encoding pd.get_dummies() is safer for this.

#import pandas as pd
#df = pd.DataFrame({
#    "user_id": [101, 102, 103, 104, 105, 106, 107],
#    "plan": [
#        "Free",
#        "Premium",
#        "premium",
#        "FREE ",
#        "Enterprise",
#        "Premium",
#        None
#    ],
#    "country": [
#        "UK",
#        "UK",
#        "USA",
#        "USA",
#        "India",
#        "UK",
#        "UK"
#    ],
#    "age": [22, 31, 45, 29, 38, 27, 41]
#})

#plan_value =  (df["plan"].value_counts(normalize = True)*100).round(2)
#df["plan"] = df["plan"].str.title()
#df["plan"] = df["plan"].str.replace(r"\s+","")
#df["plan"] = df["plan"].map({
#    "Free":1,
#    "Premium":2,
#    "Enterprise":3
#})
#df["plan"] = df["plan"].fillna(0)
#distribution  = df["plan"].value_counts(normalize = True)*100
#print(df)

#MAP(), APPLY(),VECTORIZE:---------->

#import pandas as pd
#df = pd.DataFrame({
#    "status": ["active", "inactive", "ACTIVE", "pending", "unknown"]
#})
#df["status"] = (df["status"]
#                .str.lower()
#                .replace({
#    "active": "A",
#    "inactive": "I",
#    "pending": "P"
#})
#)
#print(df)

#df = pd.DataFrame({
#    "salary": [45000, 62000, 85000, 120000, 200000]
#})
#df["Salary_k"] = df["salary"].map(lambda x: float(x/1000))
#print(df)

#df = pd.DataFrame({
#    "model_accuracy": [0.91, 0.87, 0.95],
#    "model_precision": [0.89, 0.91, 0.93],
#    "model_recall": [0.92, 0.84, 0.96]
#})
#df["average_score"] = df.apply(
#    lambda row : row.mean(), axis =1
#)
#print(df["average_score"])

#df = pd.DataFrame({
#    "A": [1, 2, 3],
#    "B": [4, 5, 6],
#    "C": [7, 8, 9]
#})
#df = df.map(lambda x : x*10)
#df = df.apply(lambda x : x*10)

#df = pd.DataFrame({
#    "price": [100, 200, 300, 400],
#    "quantity": [2, 3, 4, 5]
#})

#total = df['price'] * df['quantity']
#print(total)
#df["total"] = df.apply(lambda x : x["price"] * x["quantity"],axis = 1)
#print(df)

#import numpy as np
#df = pd.DataFrame({
#    "experience": [1, 3, 7, 10, 15],
#   "salary": [40000, 60000, 90000, 120000, 180000]
#})

#employee_type = np.where(
#  (df["experience"] >=5)&
#   (df["salary"] >=100000),"senior High Earner","Other"
#)

#employee_type2 = df.apply(lambda x : "senior High Earner" if x["experience"]>=5 & x["salary"]>100000 else"Other",axis=1)
#print(employee_type)

#import .

#df = pd.DataFrame({
#    "name": [" Alice ", "BOB", " Charlie "],
#    "salary": ["50000", "65000", "80000"],
#    "department": ["eng", "hr", "eng"]
#})

#def clean_df(df):
#    df["name"] = df["name"].str.title().str.strip()
#    return df
#def clean_salary(df):
#    df["salary"] = df["salary"].astype(int)
#    return df
#def clean_department(df):
#    df["department"].map(
#        {
#            "eng":"Engineering",
#            "hr": "HR"
#        }
#    )
#result = (
#    df
#    .pipe(clean_df)
#    .pipe(clean_salary)
#    .pipe(clean_department)
#    .pipe(clean_df)
#)
#print(result)


#COMBINING DATAFRAMES:---------->

import pandas as pd
from pandas.conftest import ascending

#users = pd.DataFrame({
#    "user_id": [101, 102, 103, 104],
#    "name": ["Alice", "Bob", "Charlie", "David"]
#})

#orders = pd.DataFrame({
#    "user_id": [101, 102, 105],
#    "amount": [500, 300, 700]
#})
#result = users.merge(
#    orders,
#    on = "user_id",
#    how = "inner"
#print(result)

#users = pd.DataFrame({
#    "user_id": [1, 2, 3, 4],
#    "name": ["A", "B", "C", "D"]
#})

#orders = pd.DataFrame({
#    "user_id": [1, 2, 2, 5],
#    "amount": [100, 200, 300, 500]
#})
#result0 = users.merge(orders, on="user_id",how = "inner")
#result1 = users.merge(orders, on="user_id",how = "left")
#result2 = users.merge(orders, on="user_id",how = "right")
#result3 = users.merge(orders, on="user_id",how = "outer")
#print(result0)
#print(result1)
#print(result2)
#print(result3)


#sales = pd.DataFrame({
#    "store": ["A", "A", "A", "B"],
#    "product": ["Laptop", "Phone", "Tablet", "Laptop"],
#    "units": [10, 20, 15, 8]
#})

#prices = pd.DataFrame({
#    "store": ["A", "A", "B"],
#    "product": ["Laptop", "Phone", "Laptop"],
#    "price": [1000, 500, 900]
#})

#df = sales.merge(prices, on=["store","product"],how="left")
#print(df)


#customer = pd.DataFrame({
#    "name": ["Alice", "Bob", "Charlie"],
#    "country": ["UK", "USA", "India"]
#}, index=[101, 102, 103])

#activity = pd.DataFrame({
#    "logins": [50, 20, 70],
#    "sessions": [100, 40, 150]
#}, index=[101, 103, 104])

#df = customer.merge(activity,
#                    left_index=True,
#                    right_index = True,
#                    how = "left"
#                    )
#print(df)


#customers = pd.DataFrame({
#    "customer_id": [101, 102, 103, 104],
#    "age": [25, 31, 42, 29]
#})

#subscriptions = pd.DataFrame({
#    "customer_id": [101, 102, 103],
#    "plan": ["Pro", "Free", "Pro"]
#})

#activity = pd.DataFrame({
#    "customer_id": [101, 101, 102, 103, 103],
##    "logins": [20, 30, 10, 50, 60]
#})

#result = customers.merge(subscriptions, on="customer_id",how="inner")
#result2 = result.merge(activity, on="customer_id",how="inner")
#print(result2)

#users = pd.DataFrame({
#    "user_id": [1, 2, 3, 4],
#    "name": ["Alice", "Bob", "Charlie", "David"],
#    "country": ["UK", "USA", "India", "UK"]
#})

#orders = pd.DataFrame({
#    "user_id": [1, 1, 2, 5],
#    "order_id": [101, 102, 103, 104],
#    "amount": [100, 200, 300, 400]
#})

#models = pd.DataFrame({
#    "user_id": [1, 2, 3],
#    "model_used": ["GPT", "Claude", "GPT"]
#})

#df1 = users.merge(orders, on="user_id",how = "left")
#df = df1.merge(models, on="user_id",how="inner")
#print(df)

#ADVANCE MERGE:------>

#import pandas as pd

#users = pd.DataFrame({
#    "user_id": [101, 102, 103],
#    "name": ["Alice", "Bob", "Charlie"],
#    "score": [80, 90, 75]
#})

#models = pd.DataFrame({
#    "user_id": [101, 102, 103],
#    "model": ["A", "B", "A"],
#    "score": [0.91, 0.87, 0.95]
#})

#df = users.merge(models, on = "user_id", suffixes = ("_users", "_models"))
#print(df)

#customers = pd.DataFrame({
#    "customer_id": [1, 2, 3, 4],
#    "name": ["A", "B", "C", "D"]
#})

#payments = pd.DataFrame({
#    "customer_id": [2, 3, 5],
#    "amount": [100, 200, 500]
#})

#df = customers.merge(payments, how = "outer",on = "customer_id", indicator = True)
#print(df)

#users = pd.DataFrame({
#    "user_id": [1, 2, 3],
#    "name": ["Alice", "Bob", "Charlie"]
#})

#orders = pd.DataFrame({
#    "user_id": [1, 1, 2, 2, 2, 3],
#    "amount": [100, 200, 50, 75, 125, 300]
#})

#df = users.merge(orders, how = "left",validate = "1:m")
#print(df)

#users = pd.DataFrame({
#    "user_id": [1, 2, 2, 3],
#    "name": ["Alice", "Bob", "Robert", "Charlie"]
#})

#orders = pd.DataFrame({
#    "user_id": [1, 1, 2, 2, 3],
#    "amount": [100, 200, 50, 75, 300]
#})
#df = users.merge(orders, how = "left",validate = "1:m")
#print(df)

#import pandas as pd
#users = pd.DataFrame({
#    "user_id": [1, 2, 3],
#    "name": ["Alice", "Bob", "Charlie"],
#    "score": [80, 90, 70]
#})

#profiles = pd.DataFrame({
#    "user_id": [1, 2, 3],
#    "score": [0.8, 0.9, 0.7],
#    "country": ["UK", "US", "CA"]
#})

#orders = pd.DataFrame({
#    "user_id": [1, 1, 2, 3, 3],
#    "amount": [100, 200, 50, 300, 400]
#})

#df = users.merge(profiles, suffixes = ("_users","_profiles"),validate = "1:1",on = "user_id")
#df1 = df.merge(orders,validate = "1:m", how = "left",indicator = True,on = "user_id")
#print(df1)

#customers = pd.DataFrame({
#    "customer_id": [1, 1, 2, 3],
#    "name": ["Alice", "Alice", "Bob", "Charlie"]
#})

#transactions = pd.DataFrame({
#    "customer_id": [1, 1, 1, 2, 3],
#    "amount": [100, 200, 300, 400, 500]
#})

#df = customers.merge(transactions, on = "customer_id",validate = "m:m")
#print(df)


#users = pd.DataFrame({
#    "user_id": [1, 2, 3, 4],
#    "name": ["Alice", "Bob", "Charlie", "David"],
#    "score": [80, 90, 70, 85]
#})

#profiles = pd.DataFrame({
#    "user_id": [1, 2, 3, 4],
#    "country": ["UK", "US", "CA", "UK"],
#    "score": [0.91, 0.87, 0.95, 0.82]
#})

#orders = pd.DataFrame({
#    "user_id": [1, 1, 2, 3, 3],
#    "amount": [100, 200, 50, 300, 400]
#})

#predictions = pd.DataFrame({
#    "user_id": [1, 2, 3, 4],
#    "prediction": [1, 0, 1, 0]
#})

#df1 = users.merge(profiles, on = "user_id", how = "left",suffixes = ("_users", "_profiles"), validate = "1:1",)
#df2 = df1.merge(orders, on = "user_id", validate = "1:m", how = "left",)
#df3 = df2.merge(predictions, on = "user_id",validate = "m:1", indicator = True,how = "left")
#print(df3)

#                                        JOIN--------->
#import pandas as pd

#employees = pd.DataFrame({
#    "employee_id": [101, 102, 103, 104],
#    "name": ["Alice", "Bob", "Charlie", "David"]
#})

#salary = pd.DataFrame({
#    "employee_id": [101, 102, 104],
#    "salary": [70000, 80000, 90000]
#})
#result = employees.join(
#    salary.set_index("employee_id"),
#     on = "employee_id")
#print(result)


#employees = pd.DataFrame({
#    "name": ["Alice", "Bob", "Charlie"]
#}, index=[101, 102, 103])

#performance = pd.DataFrame({
#    "score": [90,  95]
#}, index=[101,  103])

#result = employees.join(performance)
#print(result)

#users = pd.DataFrame({
#    "user_id": [1, 2, 3],
#    "name": ["Alice", "Bob", "Charlie"]
#})

#scores = pd.DataFrame({
#    "user_id": [1, 2, 3],
#    "score": [90, 80, 95]
#})

#result = users.join(scores.set_index("user_id"),
#                    on = "user_id")
#print(result)

#users = pd.DataFrame({
#    "name": ["Alice", "Bob", "Charlie"]
#}, index=[101, 102, 103])

#transactions = pd.DataFrame({
#    "amount": [100, 200, 300, 400],
#    "type": ["Buy", "Sell", "Buy", "Sell"]
#}, index=[101, 101, 102, 103])

#employees = pd.DataFrame({
#    "name": ["Alice", "Bob", "Charlie"]
#}, index=[101, 102, 103])

#salary = pd.DataFrame({
#    "salary": [70000, 90000]
#}, index=[101, 104])

#result1 = employees.join(salary,how ="left")
#result2 = employees.join(salary,how = "inner")
#result3 = employees.join(salary,how = "outer")
#print(result1)
#print(result2)
#print(result3)

#users = pd.DataFrame({
#    "user_id": [101, 102, 103, 104],
#    "name": ["Alice", "Bob", "Charlie", "David"]
#})

#predictions = pd.DataFrame({
#    "prediction": [0.91, 0.72, 0.88]
#}, index=[101, 103, 104])
#result = users.join(predictions,on="user_id")
#print(result)

#users = pd.DataFrame({
#    "user_id": [1, 2, 3, 4],
#    "age": [25, 31, 22, 40]
#})

#profiles = pd.DataFrame({
#    "country": ["UK", "US", "CA"],
#}, index=[1, 2, 4])

#scores = pd.DataFrame({
#    "score": [90, 85, 95, 88]
#}, index=[1, 2, 3, 4])


#result = profiles.join(scores)
#result2 = users.join(result,on = "user_id", how = "outer")
#print(result2)

#                              CONCATENATE:-------->

# jan = pd.DataFrame({
#     "product": ["A", "B"],
#     "sales": [100, 200]
# })
#
# feb = pd.DataFrame({
#     "product": ["C", "D"],
#     "sales": [150, 250]
# })
#
# mar = pd.DataFrame({
#     "product": ["E", "F"],
#     "sales": [300, 350]
# })
#
# result = pd.concat([jan,feb,mar],ignore_index = True)
# print(result)
#
# employees = pd.DataFrame({
#     "name": ["Alice", "Bob", "Charlie"]
# }, index=[101, 102, 103])
#
# scores = pd.DataFrame({
#     "score": [90, 85, 95]
# }, index=[101, 102, 103])
#
# result1 = pd.concat([employees,scores],axis=1)
# print(result1)
#
#
# train = pd.DataFrame({
#     "user_id": [1, 2],
#     "score": [90, 80]
# })
#
# test = pd.DataFrame({
#     "user_id": [3, 4],
#     "score": [95, 85]
# })
#
# result2 = pd.concat([train,test],keys=["train","test"],axis = 0)
# print(result2)
#
# system_a = pd.DataFrame({
#     "user_id": [1, 2],
#     "name": ["Alice", "Bob"],
#     "age": [25, 30]
# })
#
# system_b = pd.DataFrame({
#     "user_id": [3, 4],
#     "name": ["Charlie", "David"],
#     "salary": [70000, 80000]
# })
#
# result3 = pd.concat([system_a,system_b],axis=0)
# print(result3)


# batch_1 = pd.DataFrame({
#     "user_id": [1, 2],
#     "age": [25, 30],
#     "label": [1, 0]
# })
#
# batch_2 = pd.DataFrame({
#     "user_id": [3, 4],
#     "age": [22, 35],
#     "label": [1, 1]
# })
#
# batch_3 = pd.DataFrame({
#     "user_id": [5, 6],
#     "age": [28, 40],
#     "label": [0, 1]
# })
#
# result = pd.concat([batch_1,batch_2,batch_3],axis=0, ignore_index=True)
# print(result)
#
#
#
# users = pd.DataFrame({
#     "user_id": [1, 2, 3],
#     "name": ["Alice", "Bob", "Charlie"]
# })
#
# train_predictions = pd.DataFrame({
#     "user_id": [1, 2],
#     "prediction": [0.8, 0.3]
# })
#
# test_predictions = pd.DataFrame({
#     "user_id": [3, 4],
#     "prediction": [0.9, 0.6]
# })
#
# result = pd.concat([train_predictions, test_predictions],keys = ["train","test"])
# print(result)


#                                     AGGREGATION:------->
#
# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "user_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#     "age": [25, 30, np.nan, 40, 35, 30, np.nan, 45, 30, 50],
#     "salary": [50000, 70000, 60000, np.nan, 90000, 70000, 65000, 120000, 70000, np.nan],
#     "score": [80, 85, 90, 95, np.nan, 85, 80, 100, 85, 70],
#     "department": [
#         "Engineering", "Sales", "Engineering", "HR", "Sales",
#         "Engineering", "HR", "Engineering", "Sales", "HR"
#     ]
# })
# report = {
#     "total rows" : df.count(),
#     "non-null age" : df["age"].count(),
#     "non-null salary" : df["salary"].count(),
#     "non-null score" : df["score"].count(),
#     "No. unique users" : df["user_id"].nunique(),
#     "no.unique departments" : df["department"].nunique(),
#     "Mean Salary" : df["salary"].mean(),
#     "median salary" : df["salary"].median(),
#     "minimum salary": df["salary"].min(),
#     "maximum salary": df["salary"].max(),
#     "25th percentile" : df["salary"].quantile(0.25),
#     "75th percentile" : df["salary"].quantile(0.75),
#     "standard deviation": df["salary"].std(),
#     "variance": df["salary"].var(),
#     "mean score": df["score"].mean(),
#     "median score": df["score"].median(),
#     "minimum score" : df["score"].min(),
#     "maximum score" : df["score"].max(),
#     "90th percentile" : df["score"].quantile(0.90),
#     "mode of department" : df["department"].mode()
# }
# for key , value in report.items():
#     print(key, ":",value)


#                               GroupBy:------>

# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "customer_id": [101,101,101,102,102,103,103,103,104,104,105],
#     "region": ["UK","UK","UK","US","US","UK","UK","UK","US","US","UK"],
#     "amount": [100,250,50,500,200,100,300,50,1000,500,75],
#     "status": [
#         "completed","completed","refunded",
#         "completed","failed",
#         "completed","completed","completed",
#         "completed","refunded",
#         "completed"
#     ]
# })
#
# import pandas as pd
# import numpy as np
#
# total_transection = (
#     df.groupby("customer_id")
#       .size()
#       .rename("total_transection")
# )
#
# successful_transections = df[
#     df["status"] == "completed"
# ]
#
# completed_stats = (
#     successful_transections
#     .groupby("customer_id")["amount"]
#     .agg(
#         successful_transections="count",
#         total_spend="sum",
#         avg_completed_spend="mean",
#         max_completed_spend="max"
#     )
# )
#
# result = completed_stats.join(total_transection)
#
# result["success_rate"] = (
#     result["successful_transections"]
#     / result["total_transection"]
# )
#
# result["high_value_customer"] = np.where(
#     result["total_spend"] >= 500,
#     "Yes",
#     "No"
# )
#
# print(result)


# df = pd.DataFrame({
#     "employee_id": [1,2,3,4,5,6,7,8,9,10],
#     "department": [
#         "Engineering","Engineering","Engineering",
#         "Sales","Sales",
#         "HR","HR",
#         "Engineering","Sales","HR"
#     ],
#     "salary": [
#         90000,120000,100000,
#         60000,80000,
#         50000,70000,
#         150000,90000,60000
#     ],
#     "performance_score": [
#         80,95,90,
#         70,85,
#         60,75,
#         100,90,65
#     ]
# })
#
# df["department_avg_salary"] = df.groupby("department")["salary"].transform("mean")
# df["department_max_salary"] = df.groupby("department")["salary"].transform("max")
# df["salary_vs_department"] =  df["salary"] - df["department_avg_salary"]
# df["department_avg_performance"] = df.groupby("department")["performance_score"].transform("mean")
# df["performance_vs_department"] = df["performance_score"] - df["department_avg_performance"]
# df["department_employee_count"] = df.groupby("department")["employee_id"].transform("count")
# df["salary_percentile_within_department"] = df.groupby("department")["salary"].rank(pct=True)
# print(df.columns.tolist)

# import numpy as np
# import pandas as pd
# df = pd.DataFrame({
#     "department": [
#         "Engineering","Engineering","Engineering","Engineering",
#         "Sales","Sales","Sales",
#         "HR","HR",
#         "Marketing","Marketing","Marketing"
#     ],
#     "employee_id": range(1,13),
#     "salary": [
#         90000,120000,150000,80000,
#         60000,70000,65000,
#         50000,55000,
#         70000,80000,90000
#     ],
#     "performance": [
#         90,95,100,60,
#         70,75,80,
#         85,90,
#         60,65,95
#     ]
# })
# result = df.groupby("department").filter(
#     lambda group : (
#         len(group)>=3
#         and group["performance"].mean() >= 80
#     )
# )
# result["department_avg_salary"] = result.groupby("department")["salary"].transform("mean")
# result = result[result["salary"] > result["department_avg_salary"]]
#
# result = result[
#     [
#         "department",
#         "employee_id",
#         "salary",
#         "performance",
#         "department_avg_salary"
#     ]
# ]
#
# print(result)


# df = pd.DataFrame({
#     "customer_id": [
#         101,101,101,102,102,103,103,103,
#         104,104,105,106,106,106,107
#     ],
#     "region": [
#         "UK","UK","UK","US","US","UK","UK","UK",
#         "US","US","UK","US","US","US","UK"
#     ],
#     "product": [
#         "A","B","A","A","B","A","B","C",
#         "A","A","B","A","B","C","A"
#     ],
#     "amount": [
#         100,200,150,500,300,100,250,400,
#         1000,500,50,200,300,400,80
#     ],
#     "status": [
#         "completed","completed","refunded",
#         "completed","completed",
#         "completed","completed","completed",
#         "completed","refunded",
#         "completed",
#         "completed","completed","completed",
#         "completed"
#     ]
# })
#
# total_Transections = df.groupby("customer_id").size().rename("total_transections")
# completed_transections = df[df["status"]=="completed"].copy()
# total_completed_spend = df.groupby("status")["amount"].sum()
# avg_completed_spend = df["completed_transections"].mean()
# customer_region = df.groupby("customer_id")["region"].nunique()
# unique_product = df.groupby("customer_id")["product"].nunique()
# favorite_product = df.groupby("customer_id")["product"].max()
# customer_rank_in_region = df.groupby("customer_id")["total_completed_spend"].rank()
# region_customer_spend = df.groupby("region")["total_completed_spend"].mean()
# spend_vs_region_avg = total_completed_spend - region_customer_spend


#PIVOT :------->
# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "model": [
#         "Model_A", "Model_A", "Model_A",
#         "Model_B", "Model_B", "Model_B",
#         "Model_C", "Model_C", "Model_C"
#     ],
#     "dataset": [
#         "Train", "Validation", "Test",
#         "Train", "Validation", "Test",
#         "Train", "Validation", "Test"
#     ],
#     "accuracy": [
#         0.98, 0.92, 0.90,
#         0.96, 0.94, 0.93,
#         0.99, 0.95, 0.94
#     ]
# })
#
#
#
#
#
# result = df.pivot(
#     index = "model",
#     columns = "dataset",
#     values = "accuracy"
# )
# print(result)
# print(result["Test"].idxmax())


# import pandas as pd
#
# df = pd.DataFrame({
#     "region": [
#         "UK", "UK", "UK", "UK",
#         "US", "US", "US", "US",
#         "UK", "UK", "US", "US"
#     ],
#     "model": [
#         "Model_A", "Model_A", "Model_B", "Model_B",
#         "Model_A", "Model_A", "Model_B", "Model_B",
#         "Model_A", "Model_B", "Model_A", "Model_B"
#     ],
#     "dataset": [
#         "Train", "Test", "Train", "Test",
#         "Train", "Test", "Train", "Test",
#         "Validation", "Validation", "Validation", "Validation"
#     ],
#     "accuracy": [
#         0.98, 0.91, 0.96, 0.93,
#         0.97, 0.94, 0.95, 0.92,
#         0.90, 0.94, 0.95, 0.96
#     ]
# })
# result = df.pivot(
#     index = ["region","model"],
#     columns = "dataset",
#     values = "accuracy"
# )
# print(result)
# print("Highest Test accuracy:", result["Test"].max())
# print("Region-model combination:", result["Test"].idxmax())


#                           PIVOT TABLE:--------->
# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "model": [
#         "GPT_A", "GPT_A", "GPT_A",
#         "GPT_B", "GPT_B", "GPT_B",
#         "GPT_A", "GPT_B"
#     ],
#     "dataset": [
#         "Train", "Test", "Test",
#         "Train", "Test", "Test",
#         "Validation", "Validation"
#     ],
#     "accuracy": [
#         0.98, 0.90, 0.94,
#         0.97, 0.93, 0.95,
#         0.92, 0.94
#     ]
# })
#
# result = df.pivot_table(
#     index = "model",
#     columns = "dataset",
#     values = "accuracy",
#     aggfunc = ["mean", "min", "max"]
# )
# print(result)
# print(result["mean"]["Test"])
# print(result["max"]["Test"])
# print(result["max"]["Test"]["GPT_A"])


# import pandas as pd
#
# df = pd.DataFrame({
#     "region": [
#         "UK", "UK", "UK", "UK", "US", "US",
#         "US", "US", "UK", "UK", "US", "US"
#     ],
#     "model": [
#         "Alpha", "Alpha", "Beta", "Beta",
#         "Alpha", "Alpha", "Beta", "Beta",
#         "Alpha", "Beta", "Alpha", "Beta"
#     ],
#     "dataset": [
#         "Train", "Test", "Train", "Test",
#         "Train", "Test", "Train", "Test",
#         "Validation", "Validation", "Validation", "Validation"
#     ],
#     "run_id": [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2],
#     "accuracy": [
#         0.98, 0.91, 0.96, 0.93,
#         0.97, 0.94, 0.95, 0.92,
#         0.90, 0.94, 0.95, 0.96
#     ],
#     "latency_ms": [
#         30, 50, 35, 48, 32, 52,
#         38, 49, 47, 44, 51, 42
#     ]
# })
#
# result1 = df.pivot_table(
#     index = ["region","model"],
#     columns = "dataset",
#     values = "accuracy",
#     aggfunc = "mean"
# )
# result2 = df.pivot_table(
#     index = ["region","model"],
#     columns = "dataset",
#     values = ["accuracy","latency_ms"],
#     aggfunc = "mean"
# )
# print(result1)
# print(result2)
# print(result1["Test"])
# print(result2["latency_ms"]["Test"])
# print(result1["accuracy"]["Test"].idxmax())

# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "model": [
#         "Alpha", "Alpha", "Alpha",
#         "Beta", "Beta", "Beta",
#         "Gamma", "Gamma"
#     ],
#     "dataset": [
#         "Train", "Test", "Test",
#         "Train", "Test", "Validation",
#         "Train", "Validation"
#     ],
#     "accuracy": [
#         0.98, 0.90, 0.94,
#         0.96, np.nan, 0.93,
#         0.97, np.nan
#     ]
# })
#
# result = df.pivot_table(
#     index = "model",
#     columns = "dataset",
#     values = "accuracy"
# )
# print(result)
#
# result2 = df.pivot_table(
#     index = "model",
#     columns = "dataset",
#     values = "accuracy",
#     fill_value = 0
# )
# print(result2)
# print(result2["Test"].idxmax())

# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "model": [
#         "Model_A", "Model_A", "Model_A",
#         "Model_B", "Model_B",
#         "Model_C", "Model_C", "Model_C", "Model_C"
#     ],
#     "dataset": ["Test"] * 9,
#     "accuracy": [
#         0.80, 0.90, 1.00,
#         0.85, 0.95,
#         0.70, 0.75, 0.80, 0.85
#     ]
# })
#
# result = df.pivot_table(
#     index = "model",
#     columns = "dataset",
#     values = "accuracy",
#     margins = True
# )
# print(result)
# r = 0.80,0.90,1.00
# g = 0.85,0.95
# t = 0.70,0.75,0.80,0.85
# re = np.array(r).mean()
# nr = np.array(g).mean()
# mk = np.array(t).mean()
# print(re)
# print(nr.round(3))
# print(mk)


# import pandas as pd
#
# df = pd.DataFrame({
#     "model": [
#         "LLM_A", "LLM_A", "LLM_A", "LLM_A",
#         "LLM_B", "LLM_B", "LLM_B", "LLM_B",
#         "LLM_C", "LLM_C", "LLM_C"
#     ],
#     "metric": [
#         "Faithfulness", "Faithfulness",
#         "Relevance", "Relevance",
#         "Faithfulness", "Faithfulness",
#         "Relevance", "Relevance",
#         "Faithfulness", "Relevance", "Relevance"
#     ],
#     "score": [
#         0.90, 0.95, 0.85, 0.90,
#         0.92, 0.94, 0.80, 0.88,
#         0.96, 0.91, 0.89
#     ]
# })
#
# model1 = df.pivot_table(
#     index = "model",
#     columns = "metric",
#     values = "score",
#     aggfunc = "mean"
# )
#
# model2 = df.pivot_table(
#     index = "model",
#     columns = "metric",
#     values = "score",
#     aggfunc = ["mean","max","count"]
#
# )
# print(model1)
# print(model2)
# print(model1["Faithfulness"].idxmax())
#
# model3 = df.pivot_table(
#     index = "model",
#     columns = "metric",
#     values = "score",
#     aggfunc = lambda x : x.quantile(0.9)
# )
# print(model3)

#              MELT():----------->

# import pandas as pd
#
# df = pd.DataFrame({
#     "Model": ["GPT_A", "GPT_B", "GPT_C"],
#     "Train": [0.95, 0.92, 0.97],
#     "Test": [0.90, 0.88, 0.94],
#     "Validation": [0.93, 0.91, 0.96]
# })
#
# result = df.melt(
#     id_vars = "Model",
#     var_name = "Dataset",
#     value_name = "Accuracy"
# )
# print(result)

# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "model": ["GPT_A", "GPT_B", "GPT_C", "GPT_A"],
#     "team": ["Research", "Engineering", "Research", "Research"],
#     "accuracy_train": [0.98, 0.96, 0.97, 0.99],
#     "accuracy_test": [0.91, 0.89, np.nan, 0.93],
#     "latency_train": [120, 150, 110, 115],
#     "latency_test": [180, 210, 195, 175]
# })
#
# result = df.melt(
#     id_vars = ["model","team"],
#     var_name = "metric",
#     value_name = "value"
# )
# print(result)
#
# result2 = df.melt(
#     id_vars = ["model","team"],
#     value_vars= ["accuracy_train", "accuracy_test"],
#     var_name = "metric",
#     value_name = "value"
#
# )
# print(result2)
# print(result2.dropna(subset=["value"]))
#
# print(result.shape)
# print(result2.shape)



#                      Stack and Unstack :----->
# import pandas as pd
#
# df = pd.DataFrame({
#     "Train": [0.95, 0.92, 0.97],
#     "Test": [0.90, 0.88, 0.94]
# }, index=["GPT_A", "GPT_B", "GPT_C"])
#
# print(df)
#
# stacked = df.stack()
# print(stacked)
#
# import pandas as pd
#
# df = pd.DataFrame({
#     "Train": [0.95, 0.92, 0.97, 0.94],
#     "Test": [0.90, 0.88, 0.94, 0.91]
# })
#
# df.index = pd.MultiIndex.from_tuples(
#     [
#         ("GPT_A", "Accuracy"),
#         ("GPT_A", "F1"),
#         ("GPT_B", "Accuracy"),
#         ("GPT_B", "F1")
#     ],
#     names=["Model", "Metric"]
# )
#
# print(df)
# stacked = df.stack()
# print(stacked)

#                 READING FILES:----------->

# df = pd.read_csv("student_csv",
#                  usecols=["name","marks"])
#
# df = pd.read_csv("student_csv",
#                  na_values = "NA")
# df = pd.read_csv("events_csv",
#                  parse_dates = ["timestamp"])
#
# result = pd.read_csv("sales.csv",
#                      usecols = ["price","product","date"],
#                      na_values = "NA",
#                      parse_dates = ["date"],
#                      chunksize = 1000
#                      )
# for chunk in result:
#     print(chunk)
#
# df.dtypes
# df["price"].dtypes

# reader = pd.read_csv("llm_evaluations.csv",
#                      na_values = "NA"
#                      )
# grouped = reader.groupby("model").agg(
#     total_evaluation = ("model","count"),
#     valid_scores = ("score","count"),
#     average_scores = ("score","mean"),
#     average_latency = ("latency_ms","mean"),
#
# )
# filtered = grouped[
#     (grouped["total_evaluation"] >= 3) &
#     (grouped["average_scores"] >= 0.85)
# ]
# result = filtered.short_values(
#     by = ["average_score","average_latency"],
#     ascending = [False,True]
# )

# import pandas as pd
#
# df = pd.DataFrame({
#     "customer_id": [101, 102, 103, 101, 104, 102, 105],
#     "age": [25, None, 35, 25, None, 40, 30],
#     "city": ["London", "Paris", None, "London", "Paris", "Paris", "London"],
#     "purchase_amount": [100, 200, None, 100, 300, None, 150]
# })
#
# missing_value = df.isna().sum()
# df["age"] = df["age"].fillna(df["age"].mean())
# city_average = df.groupby("city")["purchase_amount"].transform("mean")
# df["purchase_amount"] = df["purchase_amount"].fillna(city_average)
# df = df.drop_duplicates(subset="customer_id", keep="first")
# print(df)


# df = pd.read_csv("model_predictions.csv",
#                  usecols=["evaluation_id","model_name","task","score","latency_ms","evaluation_dates","status"],
#                  na_values = "NA",
#                  parse_dates = ["evaluation_dates"]
#                  )
# print(df.head(5))
# print(df.shape)
# print(df.dtypes)
# print(df.count)
#
# df1 = df[
#     (df["status"]=="success")&
#     (df["score"].notna())&
#     (df["latency_ms"].notna())
# ].copy()
#
#
# grouped = df1.groupby("model").agg(
#     total_evaluations = ("evaluation_id", "count"),
#     average_score = ("score", "mean"),
#     average_latency = ("latency_ms", "mean"),
#     max_score = ("score", "max"),
#     min_score = ("score", "min")
# )
#
# filtered = grouped[
#     (grouped["average_score"]>=0.90)&
#     (grouped["average_latency"]<300)
# ]
# result = filtered.short_values(
#     by = "average_score",
#     ascending = False
# )

#               writing files:----->

# import pandas as pd
#
# df = pd.DataFrame({
#     "customer_id": [101, 102, 103, 104],
#     "age": [25, 35, 45, 30],
#     "income": [30000, 50000, 70000, 40000],
#     "purchased": [0, 1, 1, 0],
#     "notes": ["New", "Returning", "New", "Returning"]
# })
#
# df.to_parquet("customers.parquet",index = False)
#
# df.to_csv("training_data.csv",index = False,
#                 columns = ["age", "income", "purchased"])
#
# df[["customer_id", "age", "purchased"]].to_json(
#     "customer_records.jsonl",
#     orient = "records",
#     lines = True
# )


# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "customer_id": [101, 102, 103, 104, 105, 106],
#     "age": [25, np.nan, 45, 30, 35, np.nan],
#     "income": [30000, 50000, np.nan, 40000, 60000, 70000],
#     "purchased": [0, 1, 1, 0, 1, 0],
#     "country": ["UK", "US", "UK", "IN", "US", "UK"],
#     "notes": [
#         "New customer",
#         "Returning customer",
#         "VIP customer",
#         "New customer",
#         "Returning customer",
#         "VIP customer"
#     ]
# })
#
# df.dropna(subset = ["age","income"])[
#     ["age","income","purchased"]
# ].to_parquet("training_data.parquet",
#               index=False,
#               columns = ["age","income","purchased"]
#               )
# df.loc[
#     df["purchase"]==1,
#     ["customer_id","country","purchased"]
# ].to_csv("customer_report.csv",
#           index = False,
#           columns = ["customer_id","country","purchased"])
#
# df.loc[
#     ["country"]=="UK",
#     ["customer_id","country","notes"]
# ].to_json("customer_dataset.jsonl",
#                                             lines= True,
#                                             orient = "records"
#
# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "customer_id": [101, 102, 103, 104, 105, 106, 107],
#     "age": [25, 35, np.nan, 45, 28, 50, 32],
#     "salary": [30000, 60000, 45000, np.nan, 35000, 80000, 55000],
#     "country": ["UK", "US", "UK", "IN", "UK", "US", "UK"],
#     "purchased": [1, 0, 1, 1, 0, 1, 1],
#     "feedback": [
#         "Good",
#         "Bad",
#         "Excellent",
#         "Good",
#         "Average",
#         "Excellent",
#         "Good"
#     ]
# })
#
# df.loc[
#     (df["country"]=="UK")&
#     (df["purchased"]==1)&
#     (df["age"]>=30)
# ]["customer_id","age","salary"]
#
# clean_df = df.dropna(subset=["age","salary"])
# clean_df["age","salary","customer_id,purchased"].to_parquet("training_data.parquet",
#                     index = False)
# df.loc[
#     df["country"]=="UK",
# ["customer_id","country","feedback"]
# ].to_jason("uk_customers.jsonl",
#                                                lines = True,
#                                                orient = "records")

#
# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "customer_id": [101, 102, 103, 104, 105, 106, 102, 107, 108, 109],
#     "age": [25, 35, np.nan, 45, 29, 50, 35, 38, 17, 42],
#     "income": [30000, 65000, 72000, np.nan, 35000, 90000, 65000, 55000, 25000, 80000],
#     "country": ["UK", "US", "UK", "UK", "IN", "US", "US", "uk", "UK", "US"],
#     "purchased": [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
#     "feedback": [
#         "Excellent", "Good", "Average", "Good", "Poor",
#         "Excellent", "Good", "Great", "Poor", "Excellent"
#     ],
#     "signup_date": [
#         "2025-01-10", "2025-02-15", "2025-03-01", "2025-03-12",
#         "2025-04-20", "2025-05-05", "2025-02-15", "2025-06-18",
#         "2025-07-01", "2025-08-10"
#     ]
# })
#
# clean_df = df.loc[
#     (df["country"].str.upper())&
#     (df["customer_id"].drop_duplicated(keep="first"))&
#     (df["age","income"].dropna())&
#     (df["age"]>=18)
# ]
#
# clean_df["income_band"] = np.select(clean_df["income"]<40000,
#                                    clean_df["income"]>=40000,"high")
# clean_df["is_uk"] = np.where(clean_df["country"]=="UK",True,False)
#
# result = clean_df[[
#     "customer_id",
#     "age",
#     "income",
#     "purchased",
#     "income_band",
#     "is_uk"
# ]]
#
# result.to_parquet("training_dataset.parquet",
#                   index = False)
#
# df.loc[
#     (df["income"] >= 65000)&
#     (df["purchased"] == 1),
# ["customer_id","country","income","purchased"]].to_csv("high_value_customers.csv",
#                                                        index=False)
#
# df.loc[
#     (df["country"] == "UK")|
#     (df["feedback"] == "Excellent"),
# ["customer_id","country","feedback"]].to_json("customer_feedback.jsonl",
#                                                index = False,
#                                                orient = "records",
#                                                lines = True)
#


#                          DATE TIME:------->
#
# import pandas as pd
# from pandas.core.array_algos.transforms import shift
#
# df = pd.DataFrame({
#     "customer_id": [101, 102, 101, 103, 102, 101, 103, 104],
#     "purchase_date": [
#         "2025-01-03",
#         "2025-01-01",
#         "2025-01-05",
#         "invalid",
#         "2025-01-04",
#         "2025-01-08",
#         "2025-01-07",
#         "2025-01-06"
#     ],
#     "amount": [
#         "200",
#         "150",
#         "bad",
#         "300",
#         "250",
#         "400",
#         "350",
#         None
#     ]
# })
# df["purchase_date"] = pd.to_datetime(
#     df["purchase_date"],
#     errors = "coerce"
# )
# df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
# df.dropna(subset = ["purchase_date","amount"])
# df["year"]=df["purchase_date"].dt.year
# df["months"]=df["purchase_date"].dt.month
# df["weekdays"]=df["purchase_date"].dt.weekday
#
# df = df.loc[
#     (df["purchase_date"]>"2025-01-01")&
#     (df["purchase_date"]<"2025-01-07")
# ]
# df = df.sort_values(by=["customer_id","purchase_date"],ascending=True).copy()
# g = df.groupby("customer_id")
# df["previous_amount"] = g["amount"].shift(1)
# df["amount_change"] = df["amount"].diff()
# df["previous_purchase_days"] = g["purchase_date"].diff().dt.days
#
# df["rolling_avg_2"] = (df.groupby("customer_id")["amount"]
#                        .transform(lambda s : s.rolling(2,min_periods=1).mean()))
#
# print(df)


# import pandas as pd
#
# df = pd.DataFrame({
#     "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109],
#     "customer_id": ["A", "B", "A", "C", "B", "A", "C", "B", "A"],
#     "product": [
#         "Laptop", "Phone", "Mouse", "Laptop", "Tablet",
#         "Phone", "Mouse", "Laptop", "Keyboard"
#     ],
#     "amount": [1200, 800, 50, 1500, 400, 800, -20, 1200, 100],
#     "status": [
#         "completed", "completed", "completed", "completed",
#         "cancelled", "completed", "completed", "completed",
#         "cancelled"
#     ]
# })
#
# df = df.loc[
#     (df["status"] == "completed")&
#     (df["amount"]>0)
# ].copy()
# df = df.drop_duplicates(subset=["order_id"],keep="first")
#
# customer_summery = df.groupby("customer_id").agg(
#     total_spending = ("amount","sum"),
#     total_orders = ("order_id","count"),
#     average_order_value = ("order_id","mean")
# ).reset_index()
#
#
# high_value_customers = customer_summery.loc[
#     (customer_summery["total_spending"]>=1000)&
#     (customer_summery["total_orders"]>=2)
# ]
# df = high_value_customers.sort_values(by="total_spending",ascending=False)
# print(df)

#              ML Data preparation :----->

# import pandas as pd
#
# df = pd.DataFrame({
#     "customer_id": [101, 102, 103, 104, 105, 106, 107, 108],
#     "age": [25, 40, 35, 50, 29, 45, 38, 60],
#     "monthly_fee": [20, 45, 30, 60, 25, 50, 35, 70],
#     "contract_type": [
#         "monthly", "annual", "monthly", "annual",
#         "monthly", "annual", "monthly", "annual"
#     ],
#     "months_as_customer": [3, 24, 12, 36, 6, 30, 18, 48],
#     "churned": [1, 0, 1, 0, 1, 0, 0, 0],
#     "cancellation_date": [
#         "2026-01-10", None, "2026-02-15", None,
#         "2026-03-01", None, None, None
#     ]
# })
#
# x = df[["age","monthly_fee","contract_type","months_as_customer"]]
# y = df["churned"]
# X = df.drop(columns = ["customer_id","cancellation_date","churned"])
#
# x = pd.get_dummies(
#     x,columns=["contract_type"],
#     dtype=int
# )
#
# print(y.value_counts())
# print(y.value_counts(normalize=True))
#
# print(x.shape[0]==y.shape[0])
# print(x.isna().sum())
# print("churned"in x.columns)

# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     "customer_id": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
#     "age": [25, 40, np.nan, 35, 29, 50, 42, np.nan, 31, 45],
#     "salary": [30000, 60000, 45000, np.nan, 38000, 80000, 65000, 52000, np.nan, 70000],
#     "city": ["London", "Leeds", "London", "Bristol", "Leeds",
#              "London", "Bristol", "Leeds", "London", "Bristol"],
#     "membership": ["Gold", "Silver", "Bronze", "Gold", "Silver",
#                    "Gold", "Bronze", "Silver", "Gold", "Bronze"],
#     "website_visits": [5, 12, 8, 15, 7, 20, 11, 9, 6, 18],
#     "discount_used": [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
#     "purchase_completed": [1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
#     "purchase_date": [
#         "2026-01-10", "2026-01-12", None, "2026-01-15", None,
#         "2026-01-18", None, None, "2026-01-20", "2026-01-22"
#     ]
# })
#
# print(df.shape)
# print(df.isna().sum())
# print(df.dtypes)
#
# x = df.drop(columns=["customer_id","purchase_completed","purchase_date"])
# y = df["purchase_completed"]
# x["age"] = df["age"].fillna(df["age"].median())
# x["salary"] = df["salary"].fillna(df["salary"].median())
#
# x = pd.get_dummies(
#     x,
#     columns=["city","membership"],
#     dtype = int
# )
#
# print(y.value_counts())
# print(y.value_counts(normalize=True))
#
# print(x.shape[0]==y.shape[0])
# print("purchase_completed" in x.columns)
# print(x.isna().sum())
# print(x.select_dtypes(exclude="number").columns.tolist())



#                   SAMPLING AND DATASET SPLITTING:------>
# import pandas as pd
#
# df = pd.DataFrame({
#     "customer_id": range(1, 21),
#     "age": [22, 35, 45, 29, 40, 31, 26, 50, 38, 42,
#             23, 36, 48, 27, 33, 41, 30, 44, 25, 39],
#     "purchased": [0, 1, 0, 1, 1, 0, 0, 1, 1, 0,
#                   0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
# })
#
# sampled_df = df.sample(n=5,random_state=34)
# shuffled_reset_df = df.sample(frac=1).reset_index(drop=True)

# import pandas as pd
#
# df = pd.DataFrame({
#     "age": [22, 30, 25, 45, 35, 50, 28, 40, 32, 29],
#     "salary": [30000, 50000, 35000, 80000, 60000,
#                90000, 40000, 75000, 55000, 45000],
#     "purchased": [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
# })
#
# random_rows = df.sample(n=4,random_state=42)
# fraction_sampling = df.sample(frac=0.5,random_state=42)
# print(df["purchased"].value_counts())
# print(df["purchased"].value_counts(normalize=True))
# X = df[["age","salary"]]
# y = df["purchased"]
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42,
#     stratify = y
# )

# import pandas as pd
#
# df = pd.DataFrame({
#     "customer_id": range(1, 1001),
#     "age": [25 + (i % 40) for i in range(1000)],
#     "salary": [30000 + (i % 20) * 2500 for i in range(1000)],
#     "purchased": [1] * 100 + [0] * 900
# })
#
# sampled_df = df.sample(n = 100,random_state = 34)
# fraction_df = df.sample(frac=0.20,random_state = 35)
# print(df["purchased"].value_counts())
# print(df["purchased"].value_counts(normalize = True))
#
# X = df[["age","salary"]]
# y = df["purchased"]
#
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size = 0.2,
#     random_state = 42,
#     stratify = y
# )
# print(X_train.iloc[0])
# print(X_test.iloc[0])
# print(y_train.value_counts())
# print(y_test.value_counts())

# import pandas as pd
#
# df = pd.DataFrame({
#     "age": [22, 30, 25, 45, 35, 50, 28, 40, 32, 29,
#             26, 38, 42, 31, 27, 36, 44, 33, 24, 39],
#     "salary": [30000, 50000, 35000, 80000, 60000,
#                90000, 40000, 75000, 55000, 45000,
#                32000, 68000, 85000, 48000, 37000,
#                62000, 78000, 52000, 34000, 72000],
#     "purchased": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                   0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# })
#
#
# not_purchased = df[df["purchased"]==0]
# purchased = df[df["purchased"]==1]
#
# balanced_df = pd.concat([
#     purchased.sample(n = 6, random_state = 9),
#     not_purchased.sample(n = 6, random_state = 9)
# ]).reset_index(drop=True)
#
# print(balanced_df["purchase"].value_counts())
# print(balanced_df["purchase"].value_counts(normalize = True)*100)
#
# x = df[["age","salary"]]
# y = df["purchased"]
#
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(
#     x,
#     y,
#     test_size = 0.2,
#     random_state = 9,
#     stratify = y
# )


# import pandas as pd
#
# df = pd.DataFrame({
#     "customer_id": range(1, 1001),
#     "monthly_fee": [20 + (i % 10) * 5 for i in range(1000)],
#     "months_active": [1 + (i % 36) for i in range(1000)],
#     "cancelled": [0] * 950 + [1] * 50
# })
#
# print(df.head())
# print(df.shape)
# print(df["cancelled"].value_counts())
#
# sampled_df = df.sample(n= 200,random_state=42)
# print(sampled_df.iloc[0])
#
# print(df["cancelled"].value_counts())
# print(df["cancelled"].value_counts(normalize=True)*100)
#
# x = df[["months_active", "monthly_fee"]]
# y = df["cancelled"]
#
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x,
#                                                     y,
#                                                     test_size=0.2,
#                                                     random_state=42,
#                                                     stratify = y
#                                                     )
# print(x_train.iloc[0])
# print(x_test.iloc[0])
# print(x_train.value_counts())
# print(y_train.value_counts())

#                 PANDAS ML LIBRARIES:------->

# import pandas as pd
# import numpy as np
# import torch
#
# df = pd.DataFrame({
#     "age": [21, 30, 45, 35],
#     "city": ["London", "Paris", "London", "Berlin"],
#     "purchased": [0, 1, 1, 0]
# })
#
# x = df[["age","city"]]
# y = df["purchased"]
#
# encode = pd.get_dummies(
#     x,
#     columns=["city"],
#     dtype = int
# )
# numeric = encode.to_numpy()
#
# pytorch_x = torch.tensor(numeric,dtype=torch.float32)
#
# pytorch_y = torch.tensor(y.to_numpy(),dtype=torch.int64)
#
# print(pytorch_x.shape, pytorch_y.shape)
# print(pytorch_x.dtypes, pytorch_y.dtypes)


# import pandas as pd
# import numpy as np
# import torch
#
# df = pd.DataFrame({
#     "customer_id": [101, 102, 103, 104, 105, 106],
#     "age": [25, 35, np.nan, 45, 30, 40],
#     "city": ["London", "Paris", "London", "Berlin", "Paris", "London"],
#     "monthly_spend": [120.5, 250.0, 180.0, np.nan, 90.0, 310.0],
#     "purchased": [1, 0, 1, 0, 0, 1]
# })
#
# x = df.drop(columns = ["customer_id","purchased"])
# y = df["purchased"]
#
# x = x[["age","monthly_spend"]].median()
#
# encode = pd.get_dummies(
#     x,
#     columns = ["city"],
#     dtype = int
# )
#
# numpy_v = encode.to_numpy()
# print(numpy_v.shape)
# print(numpy_v.dtype)
#
# x_tensor = torch.tensor(numpy_v,dtype=torch.float32)
# y_tensor = torch.tensor(y.to_numpy,dtype=torch.float32)
# print(x_tensor.shape)
# print(y_tensor.shape)
# print(x_tensor.dtype)
# print(y_tensor.dtype)
#
# print(torch.isnan(x_tensor).sum())
# print(x_tensor.dtype)
# print(x_tensor[0],y_tensor[0])






















































































































































































































































































































































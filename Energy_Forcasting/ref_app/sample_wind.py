import csv

# opening the CSV file
i=0
Dates=[]
Category=[]
Descript=[]
DayOfWeek=[]
PdDistrict=[]
X=[]
Y=[]

uDates=[]
uCategory=[]
uDescript=[]
uDayOfWeek=[]
uPdDistrict=[]
uX=[]
uY=[]



x=[]
y=[]

with open(r'C:\Users\nihal\Downloads\energy_forecasting\energy_forecasting\ref_app\wind.csv', mode ='r')as file:
# reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for lines in csvFile:
        if i!=0:
            # print(lines)
            Dates.append(lines[0].split(' ')[0])
            if lines[0].split(' ')[0] not in uDates:
                uDates.append(lines[0].split(' ')[0])
            Category.append(lines[12])
            if lines[12] not in uCategory:
                uCategory.append(lines[12])

            x.append(uDates.index(lines[0].split(' ')[0]))
            y.append(uCategory.index(lines[12]))
        i=i+1
        if i==4001:
            break

# Dates
print("Dates")
# Dates_list_set = set(Dates)
# Dates_unique_list = (list(Dates_list_set))
print(Dates)
print(len(Dates))
print(uDates)
print(len(uDates))

dict={}
for i in uDates:
    dict[str(i)]={}

for i in range(0,len(Dates)):
    if Category[i] not in dict[str(Dates[i])].keys():
        dict[str(Dates[i])][Category[i]]=0
    dict[str(Dates[i])][Category[i]]+=1

for i in dict:
    print(i)
    print(dict[i])


#
# # Descript
# print("Descript")
# # Descript_list_set = set(Descript)
# # Descript_unique_list = (list(Descript_list_set))
# print(Descript)
# print(len(Descript))
# print(uDescript)
# print(len(uDescript ))
#
#
# # DayOfWeek
# print("DayOfWeek")
# # DayOfWeek_list_set = set(DayOfWeek)
# # DayOfWeek_unique_list = (list(DayOfWeek_list_set))
# print(DayOfWeek)
# print(len(DayOfWeek))
# print(uDayOfWeek)
# print(len(uDayOfWeek))
#
#
# # PdDistrict
# print("PdDistrict")
#
# print(PdDistrict)
# print(len(PdDistrict))
# print(uPdDistrict)
# print(len(uPdDistrict))
#
# # X
# print("X")
# # X_list_set = set(X)
# # X_unique_list = (list(X_list_set))
# print(X)
# print(len(X))
# print(uX)
# print(len(uX))
#
# # Y
# print("Y")
# # Y_list_set = set(Y)
# # Y_unique_list = (list(Y_list_set))
# print(Y)
# print(len(Y))
# print(uY)
# print(len(uY))
#
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from .fo_gru import predictfn
def wind(num_of_days):
    global x
    global  y
    for cat in uCategory:
        try:
            print("================================")
            print("================================")
            print("================================")
            print(cat)



            data = {
                'Time':x, #[1, 2, 3, 4, 5, 6],
                'Value':y # [10, 12, 14, 16, 18, 20]
            }

            # Create a DataFrame from the data
            df = pd.DataFrame(data)

            # Separate the independent variable (X) and dependent variable (y)
            X = df[['Time']]
            y = df['Value']


            # model = LinearRegression()
            # model.fit(X, y)
            #
            # # Make predictions for future time points (e.g., forecasting for time = 7)
            # resultlist=[]
            # for ii in range(1,int(num_of_days)):
            #     future_time = len(X)+ii
            #     predicted_value = model.predict(np.array([[future_time]]))
            #     resultlist.append(predicted_value)
            # print("res------------",resultlist)
            resultlist = predictfn(y, num_of_days)
            return resultlist
            # return resultlist

            # Print the forecasted value

            print(f"Forecast for time {resultlist}: {predicted_value[0]:.2f}")

            # Visualize the linear regression line
            # plt.scatter(X, y, color='blue', label='Data Points')
            # plt.plot(X, model.predict(X), color='red', label='Linear Regression Line')
            # plt.scatter(future_time, predicted_value, color='green', marker='x', label='Forecast')
            # plt.xlabel('Time')
            # plt.ylabel('Value')
            # plt.legend()
            # # plt.savefig("/static/solar.jpg",dpi=300)
            # plt.show()
        except Exception as e:
            print(e,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(e,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(e,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(e,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# wind(12)
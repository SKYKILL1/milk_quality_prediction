import pandas as pd

df = pd.read_csv(r'C:\Users\atifa\Desktop\milk_quality_prediction_project\Datasets\milknew.csv')

x = df.drop(['Grade'],axis=1)
y = df['Grade']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
model1 = KNeighborsClassifier()

model1.fit(x_train,y_train)

def model():
    model = KNeighborsClassifier()
    model.fit(x_train,y_train)
    return model
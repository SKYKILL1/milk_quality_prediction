import pandas as pd

df = pd.read_csv(r'C:\Users\atifa\Desktop\milk_quality_prediction_project\Datasets\WineQT.csv')

df = df.drop(['Id'],axis=1)


'''fixed acidity, volatile acidity, citric acid , chlorides , total sulphur dioxide , density , sulphates , alcohol'''


df1= df.copy()

x= df1.drop(['residual sugar','free sulfur dioxide','pH','quality'],axis=1)

y= df1['quality'].apply(lambda Y : 2 if Y>=7 else 1 if Y<7 and Y>3 else 0)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=10)

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

sc = StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.transform(x_test)

knc1 = KNeighborsClassifier()

knc1.fit(x_train_scaled,y_train)

y_pred1 = knc1.predict(x_test_scaled)

knc1.score(x_test_scaled,y_test)

def predict_quality(fixed_acidity,volatile_acidity,citric_acid,chlorides,
                    total_sulphur_dioxide,density,sulphates,alcohol):
    parameters = [[fixed_acidity,volatile_acidity,citric_acid,chlorides,
                    total_sulphur_dioxide,density,sulphates,alcohol]]
    quality = knc1.predict(sc.transform(parameters))
    return quality


'''fixed_acidity,volatile_acidity,citric_acid,chlorides,
total_sulphur_dioxide,density,sulphates,alcohol
'''
predict_quality(7.8,0.33,0.44,0.075,37.0,0.997,0.8,12.5)


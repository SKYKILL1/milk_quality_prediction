from flask import Flask,render_template,request
import wine_model


app=Flask(__name__)

@app.route('/')

def home():
    result = ''
    return render_template('wine_quality.html',**locals())

@app.route('/predict' , methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        fixed_acidity = float(request.form['fixed_acidity'])
        volatile_acidity = float(request.form['volatile_acidity'])
        citric_acid = float(request.form['citric_acid'])
        chlorides = float(request.form['chlorides'])
        total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
        density = float(request.form['density'])
        sulphates = float(request.form['sulphates'])
        alcohol = float(request.form['alcohol'])
        result = wine_model.predict_quality(fixed_acidity,volatile_acidity,citric_acid,chlorides,total_sulfur_dioxide,density,sulphates,alcohol)
        if result==0:
            return render_template('wine_quality.html', **locals())
        elif result==1:
            return render_template('wine_quality.html', **locals())
        else:
            return render_template('wine_quality.html', **locals())

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask,render_template,request
import milk_model


app=Flask(__name__)

@app.route('/')

def home():
    result = ''
    return render_template('info.html',**locals())

@app.route('/predict' , methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        pH = float(request.form['pH'])
        Temperature = float(request.form['Temperature'])
        Taste = bool(request.form['Taste'])
        Odor = bool(request.form['Odor'])
        Fat = bool(request.form['Fat'])
        Turbidity = bool(request.form['Turbidity'])
        Colour = int(request.form['Color'])
        y_pred = [[pH, Temperature, Taste, Odor, Fat, Turbidity , Colour]]
        model = milk_model.model()
        result = model.predict(y_pred)
        return render_template('info.html', **locals())

if __name__=="__main__":
    app.run(debug=True) 
#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install flask_cors')


# In[6]:


from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('flight_rf.pkl', 'rb'))

@app.route('/')
@cross_origin()
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method=='POST':
        
        # Date Of Journey
        date_dep = request.form['Dep_Time']
        Journey_day = int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').dt.day)
        Journey_month = int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').dt.month)
        
        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').dt.hour)
        Dep_min = int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').dt.min)
        
        # Arrival
        date_arr = request.form['Arrival_Time']
        Arrival_hour = int(pd.to_datetime(date_arr, format='%Y-%m-%dT%H:%M').dt.hour)
        Arrival_min = int(pd.to_datetime(date_arr, format='%Y-%m-%dT%H:%M').dt.min)
        
        # Duration
        dur_hour = abs(Arrival_hour-Dep_hour)
        dur_min = abs(Arrival_min-Dep_min)
        
        # Total Stops
        Total_Stops = int(request.form['stops'])
        
        # Airline
        airline = request.form['airline']
        if (airline=='Jet_Airways'):
            Jet_Airways = 1
            Indigo = 0
            Air_India = 0
            GoAir = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='Indigo'):
            Jet_Airways = 0
            Indigo = 1
            Air_India = 0
            GoAir = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='Air_India'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 1
            GoAir = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='GoAir'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            GoAir = 1 
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='Jet_Airways_Business'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            GoAir = 0
            Jet_Airways_Business = 1
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='Multiple_carriers'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            GoAir = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 1
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='Multiple_carriers_Premium_economy'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            GoAir = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 1
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='SpiceJet'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            GoAir = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 1
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='Trujet'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            GoAir = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 1
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='Vistara'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            GoAir = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 1
            Vistara_Premium_economy = 0
            
        elif (airline=='Vistara_Premium_economy'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            GoAir = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 1
            
        else:
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            GoAir = 0
            Jet_Airways_Business = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        # Source
        Source = request.form['Source']
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            
        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
            
        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
            
        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
            
        else: 
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            
        # Destination
        Destination = request.form['Destination']
        if (Destination == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_New_Delhi = 0
            
        elif (Destination == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0
            d_New_Delhi = 0
            
        elif (Destination == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0
            d_New_Delhi = 0
            
        elif (Destination == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1
            d_New_Delhi = 0
            
        elif (Destination == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_New_Delhi = 1
            
        else: 
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_New_Delhi = 0
            
        prediction = model.predict([['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour', 'Dep_min', 'Arrival_hour', 'Arrival_min', 'dur_hour', 'dur_min', 'Air_India', 'GoAir', 'IndiGo', 'Jet_Airways', 'Jet_Airways_Business', 'Multiple_carriers', 'Multiple_carriers_Premium_economy', 'SpiceJet', 'Vistara', 'Vistara_Premium_economy', 's_Chennai', 's_Delhi', 's_Kolkata', 's_Mumbai', 'd_Cochin', 'd_Delhi', 'd_Hyderabad', 'd_Kolkata', 'd_New Delhi']])
        output = round(prediction[0], 2)
        
        return render_template('home.html', prediction_text='Your flight price is {}'.format(output))
    
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# File: hello_world.py
import os
from flask import Flask
from flask import request
from temperature_CO2_plotter import plot_temperature
from temperature_CO2_plotter import plot_CO2
from temperature_CO2_plotter import plot_CO2_by_country
from flask import render_template
import random

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
	"""The flask  web app first runs the temperature and CO2 plot generators for specified 
	   parameters, generates an image, and then embeds that image the web page by using html."""
	plot_temperature('February',1820,2000,-10,10)
	plot_CO2(1820,2000,3,10000)
	plot_CO2_by_country(1.5,3.0,1960)
	return render_template('assign6.html',var=random.random())

@app.route('/handle_changes', methods=['GET','POST']) 
def handle_changes():
    '''This function incorporates the users requested changes into the plots, generates updated plots
    and then updates the web page.'''
    assert request.method == 'POST'   # Check that we are really in a POST request
    
    # Acces the form data:
    m = str(request.form["month"])
    ts = int(request.form["t_starting_year"])
    te = int(request.form["t_ending_year"])
    tys = float(request.form["t_y_min"])
    tye = float(request.form["t_y_max"])
    cs = int(request.form["c_starting_year"])
    ce = int(request.form["c_ending_year"])
    cys = float(request.form["c_y_min"])
    cye = float(request.form["c_y_max"])
    lt = float(request.form["lower_t"])
    ut = float(request.form["upper_t"])
    y = int(request.form["yr"])
    plot_temperature(m,ts,te,tys,tye)
    plot_CO2(cs,ce,cys,cye)
    plot_CO2_by_country(lt,ut,y)
    return render_template('assign6.html',var=random.random())

app.run()


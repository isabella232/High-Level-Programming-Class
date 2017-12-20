import pandas as pd
import matplotlib.pyplot as plot
import os

temperature = pd.read_csv('temperature.csv', sep=',')
co2 = pd.read_csv('co2.csv', sep=',')
co2_by_country = pd.read_csv('CO2_by_country.csv', sep=',')


def plot_temperature(month,time_begin,time_end,y_min,y_max):
	""" The argument month represents the month that you wish to plot the results for.

	    The arguments time_begin and time_end represent the beginning and ending years that
	    you wish to create the plot for. The minimum and maximum year values are 1816 and 2012
	    respectively.

	    The arguments y_min and y_max represent the minimum and maximum temperature values 
	    that you wish to create the plot for. The lowest recorded temperature is -5.147 °C and
	    the highest recorded temperature is 22.659 °C.
	"""
	temperature.plot(x='Year', y=month)
	plot.legend(bbox_to_anchor=(0.5, 1.11), loc='center', ncol=1)
	plot.ylabel('Temperature (°C)')
	plot.xlim(time_begin,time_end)
	plot.ylim(y_min,y_max)
	plot.title('Temperature (°C) vs. time')
	plot.savefig(os.getcwd()+'/static/mytempfig.png')
	#plot.show()

#plot_temperature('February',1900,1940,-20,20)

def plot_CO2(time_begin,time_end,y_min,y_max):
	""" The arguments time_begin and time_end represent the beginning and ending years that
	    you wish to create the plot for. The minimum and maximum year values are 1751 and 2012
	    respectively.

	    The arguments y_min and y_max represent the minimum and maximum CO2 values 
	    that you wish to create the plot for. The lowest recorded CO2 value is 3 
	    Million Metric Tons of Carbon and the highest recorded CO2 value is 9671 
	    Million Metric Tons of Carbon.
	"""
	co2.plot(x='Year', y='Carbon')
	plot.legend(bbox_to_anchor=(0.5, 1.11), loc='center', ncol=1)
	plot.ylabel('CO2 Emissions (Million Metric Tons of Carbon)')
	plot.xlim(time_begin,time_end)
	plot.ylim(y_min,y_max)
	plot.title('Global CO2 Emissions')
	plot.savefig(os.getcwd()+'/static/myCO2fig.png')
	#plot.show()

#plot_CO2(1900,1940,-10,4000)



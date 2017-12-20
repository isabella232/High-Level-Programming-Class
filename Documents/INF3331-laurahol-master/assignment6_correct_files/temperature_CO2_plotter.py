import pandas as pd
import matplotlib.pyplot as plot
import os

temperature = pd.read_csv('temperature.csv', sep=',')
co2 = pd.read_csv('co2.csv', sep=',')
co2_by_country = pd.read_csv('CO2_by_country.csv', sep=',')


def plot_temperature(month,time_begin,time_end,y_min,y_max):
	""" This function plots temperature for a user specified month vs. time. The argument month 		    represents the month that you wish to plot the results for.

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
	plot.close()

plot_temperature('February',1900,1940,-20,20)

def plot_CO2(time_begin,time_end,y_min,y_max):
	""" This function plots Gloabl CO2 emissions vs. time. The arguments time_begin and time_end 		    represent the beginning and ending years that
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
	plot.close()

plot_CO2(1900,1940,-10,4000)

def plot_CO2_by_country(lower_threshold,upper_threshold,year):
	""" This function will create a bar chart of CO2 emissions for all of the countries that are 		within the lower and upper thresholds specifified by the lower_threshold and upper_threshold
	variables respectively."""

	country_codes=[]
	emission_data=[]
	numbers=[]
	for i in range(0, len(co2_by_country["Country Code"])):

		if co2_by_country[str(year)][i]>=lower_threshold and co2_by_country[str(year)][i]<=upper_threshold:
			country_codes.append(co2_by_country["Country Code"][i])
			emission_data.append(co2_by_country[str(year)][i])
	for i in range(0, len(emission_data)):
			numbers.append(i+1)
	plot.figure(figsize=(8,8))
	plot.bar(numbers,emission_data, align='center', alpha=0.5)
	plot.xticks(numbers, country_codes, rotation='vertical',fontsize=10)
	plot.title('CO2 Emissions by Country')
	plot.ylabel('CO2 Emissions (metric tons per capita)')
	plot.xlabel('Country Code')
	plot.savefig(os.getcwd()+'/static/myCO2bycountryfig.png')
	print("lo")
	#plot.show()
	plot.close()

#plot_CO2_by_country(1.5,3.0,1960)




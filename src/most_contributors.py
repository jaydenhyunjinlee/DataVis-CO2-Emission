import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

def most_contributors(data):
	'''
	This function plots a pie chart that shows the amount of
	CO2 emission made by the most developed
	countries in each continent between year of 2010 and 2017

	It will also transform raw dataset into
	formal structure for plotting pie chart
	'''
	COL_NAME = 'CO2 Emission between 2010 and 2017'
	PIE_EXPLODE_CONF = [0,0.1,0.25,0,0.05,0.2]
	WEDGE_PROPS = {
		'edgecolor':'black','linewidth':0.5
	}

	df = data[data['Year'] >= 2010]
	df = df.drop(columns='Year')
	df = df.groupby('Entity', as_index=False).aggregate(np.sum)
	df = df.rename(columns={
			df.columns[-1]:COL_NAME
		})
	df = df.sort_values(COL_NAME, ascending=False) # Global emission would be on top in descending order wrt emission rate
	df = df.reset_index(drop=True) # Reset index in nominal order
	global_emission = df.loc[0, COL_NAME] # Retreive aggregated global emission rate

	# Drop `World` row, or the top row, since no longer needed
	df = df.iloc[1:,:]
	df = df.reset_index(drop=True) # Reset index order once more
	tops = df.iloc[:11] 

	# Some rows in dataframe represent emission rates on continent level,
	# but we only want emission rates on nation-level
	categories = tops.Entity.tolist()[:2] + tops.Entity.tolist()[-4:]
	categories.remove('Africa')
	topFiveNations = categories + ['Others']
	# categories.append('Others');

	# Retreive top CO2 emission rates from those nations
	temp = list(filter(lambda sublst: sublst[0] in categories, tops.to_numpy()))
	top_emission_rates = [x[-1] for x in temp]
	top_emission_rates.append(global_emission-sum(top_emission_rates)) # Aggregate CO2 emission made by other countries

	fig = plt.figure(figsize=(8,6))
	ax = fig.gca()

	# Plot pie chart
	pie = ax.pie(top_emission_rates, labels=topFiveNations, autopct='%.1f%%', shadow=True, 
		explode=PIE_EXPLODE_CONF, wedgeprops=WEDGE_PROPS)

	return pie







import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

def usa_and_china(data):
	'''
	This function tries to measure the impact two of the most developed countries
	have on global CO2 Emission Rate.

	Unlike `most_contributor()`, which compared CO2 Emission Rate made in top five nations among the world between year of 2010 and 2017,
	`usa_and_china()` compares CO2 Emission Rate made from USA and China, the two wealthiest countries in the world

	Function will return pie chart that displays the amount of CO2 Emission made from USA and China
	'''
	COL_NAME = 'CO2 Emission between 2010 and 2017'
	PIE_EXPLODE_CONF = [0,0.1,0]
	VIS_TITLE = 'CO2 Emission Distribution in 2017'

	# Need to do perform some transformation to meet the requirements
	data = (
		data[data['Year'] >= 2010]
		.drop(columns=['Year', 'Code'])
		.rename(columns={
			data.columns[-1]:COL_NAME
		})
		)

	data = data.groupby('Entity').aggregate(np.sum)
	# CO2 Emission made globally from 2010 to 2017
	global_emission = data[data.index == 'World'].squeeze()

	# First extract only the entries we need for this part of analysis
	usa = data[data.index == 'United States'].squeeze(axis=1)
	china = data[data.index == 'China'].squeeze(axis=1)

	usa_emission = usa.values[0]
	china_emission = china.values[0]

	categories = [
		'United States',
		'China',
		'Others'
	]

	co2_emissions = [usa_emission, china_emission, global_emission]

	# Plot pie chart
	fig = plt.figure(figsize=(8,6))
	ax = fig.gca()

	# Text Formatter function for wedges
	def func(pct, values):
		# Values in `ax.pie()` environment are represented as percentages
		# So convert into true value firsthand, then configure the text format
		total = np.sum(values)
		true_val = int((pct/100)*total)
		thousands_separated = f'{true_val:,}'
		return '{:.1f}%\n{} tons'.format(pct, thousands_separated)

	pie = ax.pie(co2_emissions, labels=categories, autopct=lambda data:func(data, co2_emissions),
		explode=PIE_EXPLODE_CONF)
	_ = ax.set_title(VIS_TITLE)
	_ = fig.subplots_adjust(right=0.8)

	return pie


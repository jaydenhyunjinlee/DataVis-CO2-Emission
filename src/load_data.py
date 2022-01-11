import pandas as pd
import numpy as np 

def load_data(fp, option=None):
	'''
	Load file at specified filepath into Pandas Dataframe
	along with couple modifications and transformations for bar graph

	Raw data in `co2_emission.csv` is in long-data format that is, 
	there are columns for all variables

	`load_data()` will load CO2 Emission dataset, or 
	convert the raw data from its long-data format
	to single-column dataframe with each year as index
	and average CO2 emission rate as value if it's being loaded
	for plotting bar charts
	'''
	# Load raw data using `read_csv()` from Pandas
	co2 = pd.read_csv(fp)

	if option is None:
		return co2

	# For bar chart, we will transform the format of data from long-data format
	# to wide-data format
	elif option == 'bargraph':
		df = co2[co2['Entity'] != 'World'] # Drop rows with no specific nation associated

		# Aggregate global CO2 emission rate at each year using average as metric
		df = df.groupby('Year').aggregate(np.average)

		# Rename the column
		df.columns = ['Average Annual CO2 Emission']

	elif option == 'linegraph':
		df = co2[
		    (co2['Entity'] == 'China') |
		    (co2['Entity'] == 'United States') |
		    (co2['Entity'] == 'United Kingdom') |
		    (co2['Entity'] == 'Australia') |
		    (co2['Entity'] == 'South Africa')
		]

		# Data transformation
		df = (df.drop(columns=['Code'])
			.groupby(['Year', 'Entity'])
			.aggregate(np.sum)
			.reset_index()
			.rename(columns={
				df.columns[-1]:'Annual CO2 Emission'
				})
			)

	return df	

import matplotlib.pyplot as plt 

def global_emission_trend(data, color=None, figsize=(10,6)):
	'''
	Plots horizontal bar graph that shows global emission rate over the course
	of years from around 1750s to 2000s.

	Parameters
		color: Color of the bars in bar chart; Bars will be colored skyblue by default
		figsize: Size of output bar chart in (width, height) form
	'''

	# Create plt.figure and plt.axes object to draw bar chart on
	fig = plt.figure(figsize=figsize)
	ax = plt.gca()

	# Horizontal axis of bar chart will be years
	# Vertical axis of bar chart will be CO2 emission rate in tons in each year
	x = data.index.tolist()
	y = data.values.ravel()

	# Define features for the bar chart
	lowest = min(y) # Lowest CO2 Emission Rate, which is one from 1751
	highest = max(y) # Highest CO2 Emission Rate, which is one from 2017
	xaxis = 'Year'
	yaxis = 'CO2 Emission (tons)'

	if color is None:
		bars = ax.bar(x=x, height=y, color='skyblue', label='CO2 Emission (tons)')
	else:
		bars = ax.bar(x=x, height=y, color=color, label='CO2 Emission (tons)')

	_ = ax.set_xlabel(xaxis)
	_ = ax.set_ylabel(yaxis)
	_ = ax.set_title('Average Annual Global CO2 Emission Rate')
	_ = ax.legend(loc=2, frameon=True)

	# Write some findings from dataset on whitespace
	low_msg = 'Emission rate in 1751: {:.2} tons'.format(lowest)
	high_msg = 'Emission rate in 2017: {:.2} tons'.format(highest)
	message = low_msg+'\n'+high_msg
	_ = ax.text(1760, 150000000, message);

	return ax


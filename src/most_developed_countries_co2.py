import altair as alt 
import numpy as np

def most_developed_countries_co2(data, width=600, height=350, interactive=False):
	'''
	This function plots line graph using year and 
	CO2 emission rate of top5 developed countries in the world
	at each year

	Graph will be plotted using `Altair` visual library
	that offers further interactivity to created plot
	'''
	top5_nations = data['Entity'].unique().tolist()
	dropdown = alt.binding_select(options=top5_nations)
	select = alt.selection_single(fields=['Entity'], bind=dropdown, name='Choose')
	color = alt.condition(select, if_true='Entity:N', if_false=alt.value('lightgrey'))
	x_range = np.arange(1751, 2017, 10)

	base = alt.Chart(data, width=width, height=height, 
		title='CO2 Emission Rate in the most developed nations in each continent').mark_line()

	chart = base.encode(
			x=alt.X('Year', type='ordinal', axis=alt.Axis(values=x_range, labelAngle=40)),
			y=alt.Y('Annual CO2 Emission', type='quantitative'),
			color=color
		).add_selection(select);

	if interactive:
		chart = chart.interactive();


	return chart
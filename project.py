#PART 1 DATA EXPLORATION
import pandas as pd
import numpy as np
import plotly.express as px
df = px.data.iris()
df
#TASK 1
df.head()
#TASK 2
df.tail()
#TASK 3
df.shape
#TASK 4
df.info()
#TASK 5
df.columns
#TASK 6
df.dtypes

##PART 2 DATA ANALYSIS
#TASK 1
print('Average Sepal Length:', np.mean(df['sepal_length']))
#TASK 2
print('Average petal length:',np.mean(df['petal_length']))
#TASK 3
print('Maximum sepal length:',np.max(df['sepal_length']))
#TASK 4
print('Minimum petal width:', np.min(df['petal_width']))
#TASK 5
print('Total number of flower species:',len(df['species']))
#TASK 6
print('Count of each species:', df['species'].value_counts())

##PART 3 Numpy Practice
sepal_length_array = np.array(df['sepal_length'])
sepal_length_array
#TASK 1
average = np.mean(sepal_length_array, axis=0)
print('Average sepal length:', average)
#TASK 2
median_sepal_length = np.median(sepal_length_array, axis=0)
print('Median of sepal length:', median_sepal_length)
#TASK 3
maximum_sepal_length = np.max(sepal_length_array,axis = 0)
print('Maximum value of Sepal length:', maximum_sepal_length)
#TASK 4
minimum_sepal_length = np.min(sepal_length_array,axis=0)
print('Minimum value of sepal length:', minimum_sepal_length )
#TASK 5
deviation_sepal_length = np.std(sepal_length_array,axis = 0)
print('Standard deviation of sepal length:', deviation_sepal_length)

### PETAL LENGTH
petal_length_array = np.array(df['petal_length'])
petal_length_array
#Task 1
average_petal_length = np.mean(petal_length_array, axis = 0)
print('Average of petal length:', average_petal_length)
#TASK 2
median_petal_length = np.median(petal_length_array)
print('Median of petal length:', median_petal_length)
#TASK 3
maximum_petal_length = np.max(petal_length_array)
print('Maximum petal length:', maximum_petal_length)
#TASK 4
minimum_petal_length = np.min(petal_length_array)
print('Minimum petal length:',minimum_petal_length)
#TASK 5
deviation_petal_length = np.std(petal_length_array)
print('Standard deviation of petal length:', deviation_petal_length )


##PART 4 Visualization using Matplotlib
from pathlib import Path

#CHART 1 LINE CHART
import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
plt.plot(df.index,df['sepal_length'], marker ='x')
plt.xlabel('Index')
plt.ylabel('Sepal length')
plt.title('Sepal Length Trend')
plt.grid(True)
line_chart_path = "sepal_length_line-chart.png"
plt.savefig(line_chart_path, bbox_inches='tight')
plt.show()
plt.close()

#CHART 2 BAR CHART
species_count = df['species'].value_counts()
plt.figure(figsize=(8,4))
plt.bar(species_count.index,species_count.values)
plt.title('Total species count')
plt.xlabel('species')
plt.ylabel('species count')
bar_chart_path = 'species_count_bar_plot.png'
plt.savefig(bar_chart_path, bbox_inches='tight')
plt.show()
plt.close()

#CHART 3 SCATTER PLOT
plt.figure(figsize=(8,4))
plt.scatter(df['sepal_length'], df['petal_length'])
plt.title('Lengths of sepal and petal')
plt.xlabel('length of sepal')
plt.ylabel('length of petal')
scatter_path = 'length_scatter.png'
plt.savefig(scatter_path, bbox_inches = 'tight')
plt.grid(True)
plt.show()
plt.close() 

#CHART 4 HISTOGRAM
plt.figure(figsize=(8,4))
plt.hist(df['sepal_width'],bins= 20)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width')
plt.ylabel('Frequency of sepal width')
histo_path ='histo_plot.png'
plt.savefig(histo_path, bbox_inches = 'tight')
plt.show()
plt.close()


###PART 5
import plotly.express as px

#CHART 1 INTERACTIVE SCATTER PLOT
fig = px.scatter(
    df,
    x='sepal_length',
    y='petal_length',
    color = 'species',
    title='Sepal length VS Petal length'
)
fig.show()


#CHART 2 BOX PLOT
fig = px.box(
    df,
    x='species',
    y = 'petal_length',
    color = 'species',
    title = ' Petal length of Different Species'    
)
fig.show()

#CHART 3 HISTOGRAM
fig = px.histogram(
    df,
    x = 'sepal_length',
    nbins = 20,
    title = 'Distribution of Sepal Length'
)
fig.show()

#CHART 4 Pie Chart
species_dist = df['species'].value_counts().reset_index()
species_dist
species_dist.columns = ['species', 'counts']
fig = px.pie(
    species_dist,
    names='species',
    values= 'counts',
    title = 'Species Distribution'    
)
fig.show()


###PART 6: Python Fundamentals
marks = [78,82,91,65,88]

#TASK 1
marks.append(100)
marks

#TASK 2
marks.remove(91)
marks

#TASK 3
marks.sort(reverse = False)
marks

#TASK 4
highest_marks = np.max(marks)
print('Highest marks:', highest_marks )

#TASK 5
lowest_marks = np.min(marks)
print('Lowest marks:', lowest_marks)
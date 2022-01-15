import pandas as pd
from matplotlib import pyplot as plt

# Read csv into pandas
data = pd.read_csv(r"cars.csv")
data.head()
df = pd.DataFrame(data)

name = df['car'].head(12)
price = df['price'].head(12)

# figure size
fig, ax = plt.subplots(figsize = (16, 9))

# Horizontal bar plot
ax.barh(name, price)

# remove axes splines
for s in ['top','bottom','left','right']:
    ax.spines[s].set_visible(False)
    
# remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# add padding between axes and labels
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

# add x, y gridlines
ax.grid(b = True, color='grey', linestyle ='-.', linewidth=0.5,alpha = 0.2)

# show top values
ax.invert_yaxis()

# add annotaiton to bars
for i in ax.patches:
    plt.text(i.get_width() + 0.2, i.get_y()+0.5,str(round((i.get_width()),2)),fontsize=10,fontweight='bold',color='grey')
    
# add plot title
ax.set_title('sports car and their price in crore', loc='left')

# add text watermark
fig.text(0.9,.15,'Jeeteshgavande30', fontsize=12,color='grey',ha='right',va='bottom',alpha=0.7)

# show plot
plt.show()


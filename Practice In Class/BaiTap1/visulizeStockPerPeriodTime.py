import pandas as pd
import matplotlib.pyplot as plt

data_raw = pd.read_csv('excel_vnm.csv')

#change and extract column YYYYDDMM by months and years
stocks_vnm = data_raw[['<DTYYYYMMDD>','<Volume>' ,'<CloseFixed>']].copy()
stocks_vnm = stocks_vnm.rename(columns = {'<DTYYYYMMDD>':'Date','<CloseFixed>':'CloseFixed','<Volume>':'Volume' })

# Visualize data by matpltotlib
ax = stocks_vnm.Volume.plot(kind = 'line', color = 'royalblue', label = 'Volume')
ax1 = ax.twinx()
ax1 = stocks_vnm.CloseFixed.plot(kind = 'line',color = 'orange',label='CloseFixed' )

ax.legend(['Volumne'],bbox_to_anchor=(1.1, 1.05))
ax1.legend(['Price'],bbox_to_anchor=(1.11, 1.09))
ax1.set(ylabel = 'Price')
ax.set(xlabel="Time",ylabel="Volume")
plt.title('VNM Stock Price And Volume Chart (01/2006 - 09/2021)', fontsize = 18)

plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data_raw = pd.read_csv('excel_vnm.csv')

#change and extract column YYYYDDMM by months and years
stocks_vnm = data_raw[['<DTYYYYMMDD>','<Volume>' ,'<CloseFixed>']].copy()
#Change type of DTYYYMMDD to string to convert
stocks_vnm['<DTYYYYMMDD>'] = stocks_vnm['<DTYYYYMMDD>'].apply(str)
stocks_vnm['date'] = pd.to_datetime(stocks_vnm['<DTYYYYMMDD>'], format ='%Y%m%d')
stocks_vnm['years'] = pd.DatetimeIndex(stocks_vnm['date']).year
stocks_vnm['months'] = pd.DatetimeIndex(stocks_vnm['date']).month
stocks_vnm.drop('<DTYYYYMMDD>', axis = 'columns', inplace=True)
#Calculate the sum of price and volumn per month
stocks_vnm = stocks_vnm.groupby(['months','years'], as_index=False)
stocks_vnm = stocks_vnm.agg({'years':'first','<CloseFixed>':'sum','<Volume>':'sum'})
stocks_vnm = stocks_vnm.sort_values(by = ['years', 'months']).reset_index()
stocks_vnm.drop('index', axis  ='columns', inplace = True)
#Rename of the columns
stocks_vnm = stocks_vnm.rename(columns = {'<CloseFixed>':'CloseFixed','<Volume>':'Volume' })

# Visualize data by matpltotlib
ax = stocks_vnm.Volume.plot(kind = 'bar', color = 'royalblue', label = 'Volume',linewidth = 0.5)
ax1 = ax.twinx()
ax1 = stocks_vnm.CloseFixed.plot(kind = 'line',color = 'orange',label='CloseFixed' )

ax.legend(['Volumne'],bbox_to_anchor=(1.1, 1.05))
ax1.legend(['CloseFixed'],bbox_to_anchor=(1.11, 1.09))

#Set time 
dates = pd.date_range('2006-01-01','2021-09-30', freq='MS').strftime("%Y-%b").tolist()
tid = np.arange(189)

#Set labels of xaxis and yaxis
plt.xticks(ticks = tid, labels= dates, size = 5, rotation = 45)
ax.set_xticks( ax.get_xticks()[::2])
ax1.set(ylabel = 'Price')
ax.set(xlabel="Time", ylabel="Volume",)
plt.title('VNM Stock Price And Volume Chart (01/2006 - 09/2021)', fontsize = 18)
plt.show()
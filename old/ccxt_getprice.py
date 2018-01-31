import urllib, json
import time,datetime
import pandas as pd
import ccxt
import numpy as np
import mysql.connector
 

def connection_sql():
    cnx = mysql.connector.connect(user='henriqu2_bianca', password='verao2018',
            host='77.104.156.92',database='henriqu2_storageCoin')
    return(cnx)

base = datetime.datetime.today()
data_inicial = (base - datetime.timedelta(days=380)).date()
time1 = time.mktime(data_inicial.timetuple())


##### Tudo isso aqui abaixo pode virar uma função ####


def ccxt_get_allcoin(time_frame = "1d"):
#### Pega dados allcoin ####
    allcoin = ccxt.allcoin()
    ohclv = allcoin.fetch_ohlcv(symbol="LTC/BTC",timeframe=time_frame,since=time1)
    ohclv = np.array(ohclv)
    mercado = 'ltc/btc'
    l_timestamp = list(ohclv[:,0]/1000)
    l_date = []
    l_open = list(ohclv[:,1])
    l_high  = list(ohclv[:,2])
    l_close  = list(ohclv[:,3])
    l_low  = list(ohclv[:,4])
    l_volume  = list(ohclv[:,5])
    
    
        
    for i in range(len(ohclv)):
        timestamp = l_timestamp[i]
        t = datetime.datetime.fromtimestamp(timestamp)
        #lista_date.append(str(t.year)+'-'+str(t.month)+'-'+str(t.day))
        l_date.append(t)
        #l_timestamp.append(ohclv[i][0]/1000)
        #l_close.append(ohclv[i][2])
    
    struct_df = {
                "datetime": l_date,
                 "timestamp":l_timestamp,
                 "close":l_close,
                 "high":l_high,
                 "low":l_low,
                 "open":l_open,
                 "volume":l_volume,
                 }
    allcoin_btc_ltc = pd.DataFrame(struct_df)
    return(allcoin_btc_ltc)


#### Pega dados bitmex ####

def ccxt_get_bitmex(time_frame = "1d"):
    bitmex = ccxt.bitmex()
    ohclv = bitmex.fetch_ohlcv(symbol="LTCH18",timeframe=time_frame,since=time1)
    ohclv = np.array(ohclv)
    
    l_timestamp = list(ohclv[:,0]/1000)
    l_date = []
    l_close = list(ohclv[:,2])
    for i in range(len(ohclv)):
        timestamp = l_timestamp[i]
        t = datetime.datetime.fromtimestamp(timestamp).date()
        #lista_date.append(str(t.year)+'-'+str(t.month)+'-'+str(t.day))
        l_date.append(t)
        #l_timestamp.append(ohclv[i][0]/1000)
        #l_close.append(ohclv[i][2])
    
    struct_df = {"date":l_date,
                 "timestamp":l_timestamp,
                 "preco_BTC":l_close}
    bitmex_btc_ltc = pd.DataFrame(struct_df)
    return(bitmex_btc_ltc)


data1 = ccxt_get_allcoin(time_frame="1d")
data2 = ccxt_get_bitmex(time_frame="1d")


conn = connection_sql()
cursor = conn.cursor()
 

for i in range(len(data1.datetime)):    
    cursor.execute('insert into Allcoin(date,timestamp,open,high,close,low,volume,mercado) values("'+str(data1.datetime[i]) +'",'+str(data1.timestamp[i]) + ','+str(data1.open[i]) + ',' +str(data1.high[i]) + ',' + str(data1.close[i]) + ',' + str(data1.low[i]) + ',' +str(data1.volume[i]) + ',"' + str(mercado) + '")')

conn.commit()

### visualizacao

data = cursor.execute("SELECT * from Allcoin")





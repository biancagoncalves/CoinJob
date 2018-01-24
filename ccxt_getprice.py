import urllib, json
import time,datetime
import pandas as pd
import ccxt
import numpy as np



base = datetime.datetime.today()
data_inicial = (base - datetime.timedelta(days=380)).date()
time1 = time.mktime(data_inicial.timetuple())


##### Tudo isso aqui abaixo pode virar uma função ####

#### Pega dados allcoin ####
allcoin = ccxt.allcoin()
ohclv = allcoin.fetch_ohlcv(symbol="LTC/BTC",timeframe="1d",since=time1)
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
allcoin_btc_ltc = pd.DataFrame(struct_df)


#### Pega dados bitmex ####
bitmex = ccxt.bitmex()
ohclv = bitmex.fetch_ohlcv(symbol="LTCH18",timeframe="1d",since=time1)
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

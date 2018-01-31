# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:58:57 2018

@author: jonatha.costa
"""
 
import urllib, json
import time,datetime
import pandas as pd
import ccxt
import numpy as np
import mysql.connector
 
def salva_banquinho(data1,symbol):
            conn = mysql.connector.connect(user='henriqu2_bianca', password='verao2018',
            host='77.104.156.92',database='henriqu2_storageCoin')
            cursor = conn.cursor()
            for i in range(len(data1.datetime)):    
                cursor.execute('insert into Allcoin(date,timestamp,open,high,close,low,volume,mercado) values("'+str(data1.datetime[i]) +'",'+str(data1.timestamp[i]) + ','+str(data1.open[i]) + ',' +str(data1.high[i]) + ',' + str(data1.close[i]) + ',' + str(data1.low[i]) + ',' +str(data1.volume[i]) + ',"' + str(symbol) + '")')
            conn.commit()
    


def mercados(exch = 'allcoin',moedas = ['ETH','LTC','BTG']):
    if not exch:
        exch = ccxt.allcoin()
    if exch == 'allcoin':    
        exch = ccxt.allcoin()   
    else:
        exch = ccxt.allcoin()   
    markets = exch.load_markets()
    market_pairs = list(markets.keys())
    aux = []
    for pair in market_pairs:
        if (str(moedas[0]) in pair or str(moedas[1]) in pair or str(moedas[2]) in pair) and 'BTC' in pair: 
            aux.append(pair)  
    return(aux)       

class capturador(object):
    

    def __init__(self,max_dias,symbol,time_frame):
        self.time_frame = time_frame
        base = datetime.datetime.today()
        data_inicial = (base - datetime.timedelta(days=max_dias)).date()
        time1 = time.mktime(data_inicial.timetuple())
        self.time1 = time1
        self.symbol = symbol
        
        
  
    def get_allcoin_captura(self):
            allcoin = ccxt.allcoin()
            ohclv = allcoin.fetch_ohlcv(symbol=self.symbol,timeframe=self.time_frame,since=self.time1)
            ohclv = np.array(ohclv)
            mercado = self.symbol
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
            allcoin = pd.DataFrame(struct_df)
            return(allcoin)
                  
  
def connecta():
        conn = mysql.connector.connect(user='henriqu2_bianca', password='verao2018',
            host='77.104.156.92',database='henriqu2_storageCoin')
        return(conn)          


def save(data1,symbol):
    conn = connecta()
    cursor = conn.cursor()
    for i in range(len(data1.datetime)):    
        cursor.execute('insert into Allcoin(date,timestamp,open,high,close,low,volume,mercado) values("'+str(data1.datetime[i]) +'",'+str(data1.timestamp[i]) + ','+str(data1.open[i]) + ',' +str(data1.high[i]) + ',' + str(data1.close[i]) + ',' + str(data1.low[i]) + ',' +str(data1.volume[i]) + ',"' + str(symbol) + '")')
        conn.commit()
    conn.close()



def get(symbol,datainicio = None ,datafim = None):
    if not symbol:
        return(print("Insira a moeda, para poder capturar os valores \n do banco!"))
    conn = connecta()
    if datainicio is None and datafim is None:    
        df =  pd.read_sql('Select * from Allcoin where mercado =' + '"' + str(symbol) + '"',conn)
    elif datainicio is None:
        df =  pd.read_sql('Select * from Allcoin where mercado =' + '"' + str(symbol) + '"' + 'and date <= ' + '"' + str(datafim) + '"',conn)
    elif datafim is None:
        df =  pd.read_sql('Select * from Allcoin where mercado =' + '"' + str(symbol) + '"' + 'and date >= ' + '"' + str(datainicio) + '"' ,conn)
    else:   
        df =  pd.read_sql('Select * from Allcoin where mercado =' + '"' + str(symbol) + '"' +  'and date BETWEEN ' + '"' + str(datainicio) + '"' + ' and ' + '"' + str(datafim) + '"',conn)
    conn.close()
    return df
            
            
#btg = capturador(360,'BTG/BTC','1d')
#eth = capturador(360,'ETH/BTC','1d')
#bcd = capturador(360,'BCD/BTC','1d')

#df1 = btg.get_allcoin_captura()
#df2 = eth.get_allcoin_captura()
#df3 = bcd.get_allcoin_captura()

#salva_banquinho(df1,'BTG/BTC')
#salva_banquinho(df2,'ETH/BTC')
#salva_banquinho(df3,'BCD/BTC')




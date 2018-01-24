# -*- coding: utf-8 -*-

import urllib, json
import time,datetime
import pandas as pd

## A ideia do codigo é ficar pedindo o valor de determinada criptomoeda para determinada
# casa de câmbio para cada dia em uma lista de datas. 


# Cria lista de datas 
base = datetime.datetime.today()
total_dias = 380
date_list = [base - datetime.timedelta(days=x) for x in range(0, total_dias)]

def getCryptoPrice(crypto="XMR",exchanger="Bitfinex",lista_datas=date_list[0:9]):
    date = []
    preco_BTC = []
    preco_USD= []
    # Para cada data verifica o preço da criptomoeda
    for i in range(len(lista_datas)):
        time1 = time.mktime(lista_datas[i].timetuple())
        # Caso a casa de cambio seja Cryptopia
        if exchanger == "Cryptopia":
            url = "https://min-api.cryptocompare.com/data/pricehistorical?ts="+str(time1)+"&tryConversion=true&fsym="+crypto+"&tsyms=BTC&e="+exchanger
            response = urllib.request.urlopen(url)
            dados = json.loads(response.read())
            url = "https://min-api.cryptocompare.com/data/pricehistorical?ts="+str(time1)+"&tryConversion=true&fsym=BTC&tsyms=USDT&e="+exchanger
            response = urllib.request.urlopen(url)
            dados_btc = json.loads(response.read())
            dados[crypto]["USD"]=dados_btc["BTC"]["USDT"]*dados[crypto]["BTC"]
        else:
            url = "https://min-api.cryptocompare.com/data/pricehistorical?ts="+str(time1)+"&tryConversion=true&fsym="+crypto+"&tsyms=BTC,USD&e="+exchanger
            response = urllib.request.urlopen(url)
            dados = json.loads(response.read())
            
        date.append(date_list[i].date())
        preco_BTC.append(float(dados[crypto]["BTC"]))
        preco_USD.append(float(dados[crypto]["USD"]))
        print("Pego "+str(i+1)+" de "+str(len(lista_datas)))
    # Faz dataframe e devolve
    d = {"date":date,
         "preco_BTC":preco_BTC,
         "preco_USD":preco_USD}
    df = pd.DataFrame(d)
    return(df)



## Algoritmo ##
sumo_price_cryptopia = getCryptoPrice(crypto="SUMO",exchanger="Cryptopia")
etc_price_yobit = getCryptoPrice(crypto="ETC",exchanger="Yobit")
            

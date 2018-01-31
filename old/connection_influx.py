#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:31:38 2018

@author: bianca
"""




from influxdb import client as influxdb
import pandas as pd
db = influxdb.InfluxDBClient(host = 'localhost',port = '8083',username='root',
                             password='root',database='teste_coin')


teste  = pd.DataFrame.to_json(data1)

db.write_points(teste, database='teste_coin')
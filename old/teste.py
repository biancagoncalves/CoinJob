#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:57:57 2018

@author: john
"""

import argparse
 
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import random
import time
 
 
USER = 'bianca'
PASSWORD = 'verao2018'
DBNAME = 'teste_coin'
 
 
def main():
    host='localhost'
    port=8086
 
    nb_day = 15  # number of day to generate time series
    timeinterval_min = 5  # create an event every x minutes
    total_minutes = 1440 * nb_day
    total_records = int(total_minutes / timeinterval_min)
    now = datetime.datetime.today()
    metric = "server_data.cpu_idle"
    series = []
 
    for i in range(0, total_records):
        past_date = now - datetime.timedelta(minutes=i * timeinterval_min)
        value = random.randint(0, 200)
        hostName = "server-%d" % random.randint(1, 5)
        # pointValues = [int(past_date.strftime('%s')), value, hostName]
        pointValues = {
                "time": past_date.strftime ("%Y-%m-%d %H:%M:%S"),
                # "time": int(past_date.strftime('%s')),
                "measurement": metric,
                'fields':  {
                    'value': value,
                },
                'tags': {
                    "hostName": hostName,
                },
            }
        series.append(pointValues)
    print(series)
 
    client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)
 
    print("Create a retention policy")
    retention_policy = 'awesome_policy'
    client.create_retention_policy(retention_policy, '3d', 3, default=True)
 
    print("Write points #: {0}".format(total_records))
    client.write_points(series, retention_policy=retention_policy)
 
    time.sleep(2)
 
    query = 'SELECT MEAN(value) FROM "%s" WHERE time &amp;amp;gt; now() - 10d GROUP BY time(500m);' % (metric)
    result = client.query(query, database=DBNAME)
    print (result)
    print("Result: {0}".format(result))
 
if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:57:51 2018

@author: Bianca
"""

import argparse
from influxdb import InfluxDBClient
import pandas as p

def main(host='localhost', port=8083):
    """Instantiate the connection to the InfluxDB client."""
    user = 'root'
    password = 'root'
    dbname = 'teste_coin'
    # Temporarily avoid line protocol time conversion issues #412, #426, #431.
    protocol = 'json'

    client = DataFrameClient(host, port, user, password, dbname)

    print("Create pandas DataFrame")
    df = pd.DataFrame(data=list(range(30)),
                      index=pd.date_range(start='2014-11-16',
                                          periods=30, freq='H'))

    print("Create database: " + dbname)
    client.create_database(dbname)

    print("Write DataFrame")
    client.write_points(df, 'demo', protocol=protocol)

    print("Write DataFrame with Tags")
    client.write_points(df, 'demo',
                        {'k1': 'v1', 'k2': 'v2'}, protocol=protocol)

    print("Read DataFrame")
    client.query("select * from demo")

    print("Delete database: " + dbname)
    client.drop_database(dbname)


def parse_args():
    """Parse the args from main."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
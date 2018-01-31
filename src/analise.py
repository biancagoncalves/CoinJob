# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:34:19 2018

@author: jonatha.costa
"""

import urllib, json
import time,datetime
import pandas as pd
import ccxt
import numpy as np
import mysql.connector


class analise(object):
    
    def __init__(self,exch,symbol,datainicio,datafim,time_frame):
        self.time_frame = time_frame
        self.symbol = symbol
        self.datainicio
        self.datafim
        self.exch
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:48:35 2023


@author: Shahabedin Chatraee Azizabadi
RKZ run file 14 m0nth back
"""
import argparse
import pyodbc
import datetime
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import sqlalchemy
import rkz_main_python_version 


delta1=timedelta(days=2*365/12)
now = datetime.now()-delta1
month=now.month
# subtract 16 months from the current date
months_to_subtract = 16# 14+2
delta = timedelta(days=months_to_subtract*365/12)
new_date = now - delta
new_month=new_date.month
new_year=new_date.year

if month not in (3,4):
#if (month!=3):

    for i in range(new_month+1,12+1):#[target_m]:    
        test_brutto = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = False)
        test = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = True)
        print('for year', new_year)
        print('Done! for month', i)
        print('-------------')  
          
    for i in range(1,new_month+3):#[target_m]:    
        test_brutto = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year+1, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = False)
        test = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year+1, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = True)
        print('for year', new_year+1)
        print('Done! for month', i)
        print('-------------')   
        
else:
    for i in range(new_month+1,12+1):#[target_m]:
        if(i!=0):
            test_brutto = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = False)
            test = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = True)
            print('for year', new_year)
            print('Done! for month', i)
            print('-------------')
            
        else:
            print('April')
    if (month==3):
        for i in range(1,new_month+2):#[target_m]:    
            test_brutto = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year+1, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = False)
            test = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year+1, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = True)
            print('for year', new_year+1)
            print('Done! for month', i)
            print('-------------')
    else:
        for i in range(1,new_month+1):#[target_m]:    
            test_brutto = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year+1, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = False)
            test = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year+1, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = True)
            print('for year', new_year+1)
            print('Done! for month', i)
            print('-------------')
    
    for i in range(1,month-1):#[target_m]:    
        test_brutto = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year+2, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = False)
        test = rkz_main_python_version .run_RKZ(data_selection_for_year = new_year+2, month_number = i, ogr_key = 7, calculate_vgk_flag = True, current_overall_overstock_rate = 31.5,shop_exception = True)
        print('for year', new_year+2)
        print('Done! for month', i)
        print('-------------')  
    

   
          


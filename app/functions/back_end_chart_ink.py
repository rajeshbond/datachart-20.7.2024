import time
import requests
from fastapi import Response, status, HTTPException, Depends, APIRouter
from bs4 import BeautifulSoup as bs
import pandas as pd
import pytz,os, datetime
import asyncio
from pprint import pprint
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from sqlalchemy import text, column
from sqlalchemy.sql import select
from .sorted_data import frequency

# from fetch_data import nse_data

# from google_sheet import clean_up, update_google_sheet,update_cell
# t.me/CompoundingFunda_bot
URL = 'https://chartink.com/screener/process'

def scandata(condition, conditionName):
    try:
        db = next(get_db())
        symbol_df = pd.read_sql(db.query(models.Symbol).statement, db.bind)
        
        with requests.session() as s:
            rawData = s.get(URL)
            soup = bs(rawData.content, "lxml")
            meta = soup.find('meta', {"name": "csrf-token"})['content']
            header = {"X-Csrf-Token": meta}
            responseData_scan1 = s.post(url=URL, headers=header, data=condition, timeout=10000)
            if responseData_scan1.content:
                data = responseData_scan1.json()
                stock = data['data']
                stock_list = pd.DataFrame(stock)
                # print(f"-------------------{conditionName}----------------------------")
                # print(stock_list)
                if stock_list.empty:
                    time.sleep(10)
                    print("no data")
                    return
                today = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).date())
                stock_list['date'] = today
                now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))  
                current_time = now.strftime('%H:%M:%S')
                stock_list['time'] = str(current_time)
                stock_list['nsecode'] = stock_list['nsecode'].fillna('NA')
                stock_list['bsecode'] = stock_list['bsecode'].fillna(0)
                datafile = pd.merge(stock_list,  symbol_df[["nsecode", 'igroup_name']], on="nsecode", how='left')
                datafile['igroup_name'] = datafile['igroup_name'].fillna('Others')
                # print(datafile)
              
                new_data = datafile.drop(['sr','name','bsecode','volume','time'],axis=1)
                print(new_data)
                print(f"saving data to mid/{conditionName}.csv")
                new_data.to_csv(f'mid/{conditionName}.csv', index=False)
                dayStockSelector(datafile)
    
                # nse_data()
                return datafile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def chartinkLogicBankend(condition, conditionName,db_name):
    try:
        # today = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).date())
        scandata(condition, conditionName)
        # Fetch a database session
        db = next(get_db())
        
        # For Indraday Condition --- start
        if (db_name == "IntradayData" and conditionName == "Champions Intraday"):
            intra_data = pd.read_sql(db.query(models.IntradayData).statement, db.bind)
            if intra_data.empty:
                print(f"{db_name} {conditionName}data not found in scan")
                return
            frequency(intra_data,conditionName)
            
                
        # For OverBroughtData Condition --- start
        elif (db_name == "OverBroughtData" and conditionName == "Champions Over Brought"):
         
       
            over_brought_data = pd.read_sql(db.query(models.OverBroughtData).statement, db.bind)
            if over_brought_data.empty:
                print(f"{db_name} {conditionName}data not found in scan")
                return
            frequency(over_brought_data,conditionName)
           
        # For PositionalData Condition --- start  
        elif (db_name == "PositionalData" and conditionName == "Champions Positional"):
            positonal_data = pd.read_sql(db.query(models.PositionalData).statement, db.bind)
            if positonal_data.empty:
                print(f"{db_name} {conditionName}data not found in scan")
                return
            frequency(positonal_data,conditionName)
            
        elif (db_name == "ReversalData" and conditionName == "Champions Reversal Stocks"):  
            reversal_data = pd.read_sql(db.query(models.ReversalData).statement, db.bind)
            if reversal_data.empty:
                print(f"{db_name} {conditionName}data not found in scan")
                return
            frequency(reversal_data,conditionName)
            
        elif (db_name == "SwingData" and conditionName == "Champions Swing"):
            swing_data = pd.read_sql(db.query(models.SwingData).statement, db.bind)
            if swing_data.empty:
                print(f"{db_name} {conditionName}data not found in scan")
                return
            frequency(swing_data,conditionName)
                
                
        else:
            return

    except Exception as e:
        print(f"chartinkLogicBankend error: {e}")


    
def dayStockSelector(scanData):
    # print("-----------dayStockSelector------------")
    # print(scanData['nsecode'])
    db = next(get_db())
    day_symbol = pd.read_sql(db.query(models.DaySymbol).statement, db.bind)

    if not day_symbol.empty:
        new_symbol_entry = scanData[~scanData['nsecode'].isin(day_symbol['nsecode'])]

        if new_symbol_entry.empty:
            print("No new data found")
            return
        print("New data found")
        print(new_symbol_entry)
        new_symbol_entry = new_symbol_entry.to_dict(orient='records')
        print("---------------New data found-------------\n")
        try:
            db.bulk_insert_mappings(models.DaySymbol, new_symbol_entry)
            db.commit()
            pass
        except Exception as e:
            print(f"dayStockSelector error in dataBase (e)")
            raise HTTPException(status_code=500, detail=str(e))
    else:
        try:
            new_symbol_entry = scanData
            print("---------------First Entry -------------\n")
            print(new_symbol_entry)
            new_symbol_entry = scanData.to_dict(orient='records')
            
            db.bulk_insert_mappings(models.DaySymbol, new_symbol_entry)
            db.commit()
        except Exception as e:
            print(f"dayStockSelector error in dataBase (e)")
            raise HTTPException(status_code=500, detail=str(e))
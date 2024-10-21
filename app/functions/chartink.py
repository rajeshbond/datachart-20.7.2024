import time

from fastapi import HTTPException,status
from .back_end_chart_ink import chartinkLogicBankend
from .nse_function import market_status_1
from .nse_data import market_status




def trasferDataToGoogleSheet():

    # URL = 'https://chartink.com/screener/process'
    # URL = 'https://chartink.com/widget/process'

    # Initialize prev_data as None before the loop
    # print("started")
    count = 0
    test = 1
    flag = True
    while flag:
        test = 0
        market = market_status_1()
        print(f"Maket status <--------> {market}")
    
            
        try:
            title = "Champions Screener"
            sub_title = "powered by SnT Solution - 8080105062"
            # update_cell(cell='A3',data=title,sheetname='Champions DashBoard')
            # update_cell(cell='A200',data=sub_title,sheetname='DashBoard')
            # Condtion 1
            conditionName = "Champions Intraday" # change name Here
            db_name = "IntradayData"
            # Put condition here
            CONDITION1 = {"scan_clause": "( {cash} ( ( {57960} ( ( {cash} ( latest cci( 20 ) >= -100 and weekly cci( 20 ) >= -150 and latest rsi( 14 ) > 30 and weekly rsi( 14 ) >= 45 and monthly rsi( 14 ) >= 50 and market cap > 250 and latest obv >= [0] 4 hour obv and latest macd line( 13 , 8 , 5 ) >= [0] 15 minute macd line( 13 , 8 , 5 ) and weekly obv >= 1 week ago obv and latest avg true range( 14 ) >= 1 day ago avg true range( 14 ) and weekly avg true range( 14 ) >= 1 week ago avg true range( 14 ) and latest rsi( 14 ) >= 1 day ago rsi( 14 ) ) ) ) ) ) )"}
            # CONDITION1 = {"scan_clause": "( {cash} ( ( {57960} ( ( {cash} ( latest cci( 20 ) >= -100 and weekly cci( 20 ) >= -150 and latest rsi( 14 ) > 30 and weekly rsi( 14 ) >= 45 and monthly rsi( 14 ) >= 50 and market cap > 250 and latest obv >= [0] 4 hour obv and latest macd line( 13 , 8 , 5 ) >= [0] 5 minute macd line( 13 , 8 , 5 ) and weekly obv >= 1 week ago obv and latest avg true range( 14 ) >= 1 day ago avg true range( 14 ) and weekly avg true range( 14 ) >= 1 week ago avg true range( 14 ) and latest rsi( 14 ) >= 1 day ago rsi( 14 ) ) ) ) ) ) )"}
            # 
            chartinkLogicBankend(condition=CONDITION1 ,conditionName=conditionName,db_name=db_name)

        except Exception as e:
            print(e)
        # Condtion 2
        try:
            # Condtion 2
            db_name = "SwingData"
            conditionName = "Champions Swing" # change name Here
            CONDITION2 = {"scan_clause": "( {cash} ( ( {cash} ( ( {57960} ( ( {cash} ( latest cci( 20 ) >= 0 and weekly cci( 20 ) >= -150 and latest rsi( 14 ) > 30 and weekly rsi( 14 ) >= 45 and monthly rsi( 14 ) >= 50 and market cap > 250 and latest obv >= [0] 4 hour obv and latest macd line( 13 , 8 , 5 ) >= [0] 4 hour macd line( 13 , 8 , 5 ) and weekly obv >= 1 week ago obv and latest avg true range( 14 ) >= [0] 4 hour avg true range( 14 ) and weekly avg true range( 14 ) >= 1 week ago avg true range( 14 ) and earning per share[eps] > prev year eps ) ) ) ) ) ) ) )"}
            # chartinkLogicBankend(condition=CONDITION2,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            
            chartinkLogicBankend(condition=CONDITION2,conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e)
        # Condtion 3        
        try:
            # condition 3
            db_name = "PositionalData"
            conditionName = "Champions Positional"
            CONDITION3 = {"scan_clause": "( {cash} ( ( {cash} ( ( {cash} ( ( {cash} ( ( {cash} ( weekly cci( 20 ) >= -100 and monthly cci( 20 ) >= 0 and weekly rsi( 14 ) >= 40 and monthly rsi( 14 ) >= 50 and market cap > 250 and weekly obv >= 1 week ago obv and weekly avg true range( 14 ) >= 1 week ago avg true range( 14 ) and weekly rsi( 14 ) >= 1 week ago rsi( 14 ) and monthly obv >= 1 week ago obv and monthly avg true range( 14 ) >= 1 week ago avg true range( 14 ) and ttm eps > prev year eps and yearly return on capital employed percentage >= 20 and yearly debt equity ratio <= 1 and yearly operating profit margin percentage >= 15 ) ) ) ) ) ) ) ) ) )"}
            # chartinkLogicBankend(condition=CONDITION3,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            chartinkLogicBankend(condition=CONDITION3, conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e)
        # Condtion 4    
        try:
            # condition 4
            db_name = "ReversalData"
            conditionName = "Champions Reversal Stocks"
            CONDITION4 ={"scan_clause": "( {cash} ( 1 day ago cci( 20 ) <= -100 and latest cci( 20 ) >= 1 day ago cci( 20 ) and market cap >= 250 and latest close >= 1 day ago close and latest macd line( 26 , 12 , 9 ) >= [0] 4 hour macd line( 26 , 12 , 9 ) and latest obv >= 1 day ago obv and latest rsi( 14 ) >= 1 day ago rsi( 14 ) and latest adx di negative( 14 ) <= 1 day ago adx di negative( 14 ) and latest accdist  >= 1 day ago accdist  ) )"}
            # {"scan_clause":"( {cash} ( 1 day ago cci( 20 ) <= -100 and latest cci( 20 ) >= 1 day ago cci( 20 ) and market cap >= 250 and latest close >= 1 day ago close and latest macd line( 26 , 12 , 9 ) >= [0] 4 hour macd line( 26 , 12 , 9 ) and latest obv >= 1 day ago obv ) )"}
            # CONDITION4 = {"scan_clause": "( {cash} ( 1 day ago cci( 20 ) <= -100 and latest cci( 20 ) >= 1 day ago cci( 20 ) and market cap >= 250 ) )"}
            # chartinkLogicBankend(condition=CONDITION4,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            # print(conditionName)
            chartinkLogicBankend(condition=CONDITION4, conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e) 
        # Condtion 5   
        try:
            # condition 5
            
            db_name = "OverBroughtData"
            conditionName = "Champions Over Brought"
            CONDITION5 = {"scan_clause": "( {33489} ( latest cci( 20 ) <= 1 day ago cci( 20 ) and latest obv < 1 day ago obv and latest macd line( 26 , 12 , 9 ) < 1 day ago macd line( 26 , 12 , 9 ) and weekly obv < 1 week ago obv and monthly obv < 1 month ago obv and weekly cci( 20 ) < 1 week ago cci( 20 ) and monthly cci( 20 ) < 1 month ago cci( 20 ) and [0] 15 minute close < 1 day ago close ) )"}
            # {"scan_clause": "( {33489} ( latest cci( 20 ) <= 1 day ago cci( 20 ) and latest obv < 1 day ago obv and latest macd line( 26 , 12 , 9 ) < 1 day ago macd line( 26 , 12 , 9 ) and weekly obv < 1 week ago obv and monthly obv < 1 month ago obv and weekly cci( 20 ) < 1 week ago cci( 20 ) and monthly cci( 20 ) < 1 month ago cci( 20 ) and [0] 30 minute close < 1 day ago close ) )"}
            # chartinkLogicBankend(condition=CONDITION5,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            chartinkLogicBankend(condition=CONDITION5, conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e)
        # Condtion 6  
        try:
            # condition 6
            # conditionName = "MOMENTUM BUY"  - to be change on 20.3.2024
            db_name = "Condition6"
            conditionName = "Champions Condition 6"
            CONDITION6 = {"scan_clause": "( {cash} ( ( {cash} ( ( {57960} ( ( {cash} ( latest cci( 20 ) >= 0 and weekly cci( 20 ) >= -150 and latest rsi( 14 ) > 30 and weekly rsi( 14 ) >= 45 and monthly rsi( 14 ) >= 50 and market cap > 250 and latest obv >= [0] 4 hour obv and latest macd line( 13 , 8 , 5 ) >= [0] 4 hour macd line( 13 , 8 , 5 ) and weekly obv >= 1 week ago obv and latest avg true range( 14 ) >= [0] 4 hour avg true range( 14 ) and weekly avg true range( 14 ) >= 1 week ago avg true range( 14 ) and monthly obv >= 1 month ago obv and monthly cci( 20 ) >= 1 month ago cci( 20 ) ) ) ) ) ) ) ) )"}
            chartinkLogicBankend(condition=CONDITION6, conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e)
        # Condtion 7   
        try:
            # condition 
            db_name = "Stage_2"
            conditionName = "Stage_2"
            # CONDITION7 = {"scan_clause": "( {cash} ( 1 month ago ema( monthly close , 9 ) < 1 month ago ema( monthly close , 20 ) and monthly ema( monthly close , 9 ) >= monthly ema( monthly close , 20 ) and market cap >= 250 and monthly macd line( 26 , 12 , 9 ) >= 1 month ago macd line( 26 , 12 , 9 ) ) )"}
            CONDITION7 = {"scan_clause": "( {cash} ( ( {cash} ( ttm sales > 1 year ago net sales and monthly obv > 1 month ago obv and weekly obv > 1 week ago obv and monthly macd line( 26 , 12 , 9 ) > 1 month ago macd line( 26 , 12 , 9 ) and ttm eps > prev year eps and yearly return on capital employed percentage > 15 and market cap >= 1000 and yearly debt equity ratio <= 1 and monthly macd line( 26 , 12 , 9 ) > monthly macd signal( 26 , 12 , 9 ) and weekly macd line( 26 , 12 , 9 ) > weekly macd signal( 26 , 12 , 9 ) ) ) ) )"}
            chartinkLogicBankend(condition=CONDITION7, conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e)
        # Achivers conditions Starts here ----------->
        # Condtion 8   
        try:
            # condition 
            db_name = "AdvanceData"
            conditionName = "Advance"
            CONDITION8 = {"scan_clause": "( {cash} ( latest close > latest sma( close,30 ) and latest close > latest sma( close,50 ) and latest close > latest sma( close,100 ) and latest close > latest sma( close,200 ) and latest volume > 1 week ago volume and latest obv > 1 day ago obv and latest cci( 20 ) > 1 day ago cci( 20 ) and weekly obv > 1 week ago obv and monthly obv >= 1 week ago obv and latest macd line( 26 , 12 , 9 ) > 1 day ago macd line( 26 , 12 , 9 ) and latest adx di positive( 14 ) > 1 day ago adx di positive( 14 ) ) )"}
            chartinkLogicBankend(condition=CONDITION8, conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e)
        # Condtion 9   
        try:
            # condition 
            db_name = "BullishCrossOverData"
            conditionName = "Bullish CrossOver"
            CONDITION9 = {"scan_clause": "( {cash} ( ( {cash} ( latest macd line( 13 , 8 , 5 ) > latest macd signal( 13 , 8 , 5 ) and 1 day ago  macd line( 13 , 8 , 5 ) <= 1 day ago  macd signal( 13 , 8 , 5 ) and 1 day ago macd line( 13 , 8 , 5 ) < 1 day ago macd signal( 13 , 8 , 5 ) and latest rsi( 14 ) >= 40 and latest volume >= latest sma( latest volume , 20 ) and market cap >= 500 ) ) ) ) "}
            chartinkLogicBankend(condition=CONDITION9, conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e)
        # Condtion 10   
        try:
            # condition 
            db_name = "ReversalStockData"
            conditionName = "Reversal Stock"
            CONDITION10 = {"scan_clause": "( {cash} ( ( {cash} ( weekly rsi( 14 ) >= 60 and monthly rsi( 14 ) >= 60 and latest rsi( 14 ) >= 40 and latest rsi( 14 ) < 60 and latest rsi( 14 ) > 1 day ago rsi( 14 ) and 1 day ago rsi( 14 ) < 2 days ago rsi( 14 ) and 2 days ago rsi( 14 ) < 3 days ago rsi( 14 ) and latest volume >= 1 day ago volume and market cap >= 500 ) ) ) )"}
            chartinkLogicBankend(condition=CONDITION10, conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e)
        # Condtion 11   
        try:
            # condition 
            db_name = "ActiveByVolumeData"
            conditionName = "ActiveBy Volume"
            CONDITION11 = {"scan_clause": "( {cash} ( ( {cash} ( latest volume > 1 day ago max( 255 , latest volume ) ) ) ) )"}
            chartinkLogicBankend(condition=CONDITION11, conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e)
        # Condtion 12   
        try:
            # condition 
            db_name = "RangeBreakoutData"
            conditionName = "Range Breakout"
            CONDITION12 = {"scan_clause": "( {cash} ( ( {cash} ( ( {cash} ( abs( latest high - latest low ) > abs( 1 day ago high - 1 day ago low ) and abs( latest high - latest low ) > abs( 2 days ago high - 2 days ago low ) and abs( latest high - latest low ) > abs( 3 days ago high - 3 days ago low ) and abs( latest high - latest low ) > abs( 4 days ago high - 4 days ago low ) and latest close > latest open and latest close > weekly open and latest close > monthly open and latest low > 1 day ago close - abs( 1 day ago close / 222 ) and latest adx( 14 ) >= 15 and latest adx di positive( 14 ) > latest adx di negative( 14 ) and 1 day ago  adx di positive( 14 ) <= 1 day ago  adx di negative( 14 ) ) ) ) ) ) )"}
            chartinkLogicBankend(condition=CONDITION12, conditionName=conditionName,db_name=db_name)
        except Exception as e:
            print(e)
        # # print(market)    
        if(market == 'Closed' or market == "Close"):
            # print(f"Market is {count}<--->{market}")
            flag = False
            print(f"---{flag}----------{market}------------")
            break
        else:
            count +=1
            print(f"Market is {count}")
        time.sleep(10) # 300 seconds = 5 minutes
    # Sleep for 5 minutes``
        
    # time.sleep(120) # 300 seconds = 5 minutes

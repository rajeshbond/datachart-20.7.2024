from fastapi import HTTPException
import pandas as pd
import datetime, os
import pytz
from ..database import get_db
from sqlalchemy import text
from .comp import compare_csv_files
from .addfunda import piotista


def get_last_n_working_days(n, start_date):
    """
    Returns a list of the last `n` working days (Mon–Fri) before `start_date`.
    """
    start_date = pd.to_datetime(start_date)
    working_days = []

    current_day = start_date - pd.Timedelta(days=1)  # Start from yesterday
    while len(working_days) < n:
        if current_day.weekday() < 5:  # 0–4 are Mon–Fri
            working_days.append(current_day)
        current_day -= pd.Timedelta(days=1)
    return working_days


def frequency(data, conditionName):
    db = next(get_db())

    # Convert 'date' column to datetime
    data['date'] = pd.to_datetime(data['date'], format="%Y-%m-%d")

    today = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).date()
    print(f"=================={today} - {conditionName}=================")
    # ✔ Decide working day range based on condition
    if conditionName == 'Champions Over Brought':
        frequency_days = 4
    else:
        frequency_days = 70

    # Get last N working days (excluding today), and include today separately
    last_n_working_days = get_last_n_working_days(frequency_days, today)
    # if conditionName == 'OverBroughtData':
    #     print(f"============={last_n_working_days}  - {conditionName}================")
    last_n_working_days_str = [day.strftime('%d-%m-%Y') for day in last_n_working_days]
    last_n_working_days_str.append(today.strftime('%d-%m-%Y'))  # Include today

    # Filter relevant rows
    filtered_data = data[data['date'].dt.strftime('%d-%m-%Y').isin(last_n_working_days_str)]

    # Frequency by nsecode
    frequency_df = filtered_data['nsecode'].value_counts().reset_index()
    frequency_df.columns = ['nsecode', 'count']

    # Load condition-specific CSV
    chart_can_path = f'mid/{conditionName}.csv'
    if not os.path.exists(chart_can_path):
        raise HTTPException(status_code=404, detail=f"Data file {chart_can_path} not found")

    chart_can = pd.read_csv(chart_can_path)
    filtered_chart_can = chart_can[chart_can['nsecode'].isin(frequency_df['nsecode'])]

    # Merge with frequency
    result = filtered_chart_can.merge(frequency_df, on='nsecode')

    # Sector frequency
    igroup_name_count = result['igroup_name'].value_counts().reset_index()
    igroup_name_count.columns = ['igroup_name', 'igroup_name_count']
    result = result.merge(igroup_name_count, on='igroup_name')

    # Confirm latest count
    nsecode_count = result['nsecode'].value_counts().reset_index()
    nsecode_count.columns = ['nsecode', 'count']
    result = result.merge(nsecode_count, on='nsecode')

    # Cleanup and renaming
    result = result.drop(columns=['count_y'])
    result = result.rename(columns={'count_x': 'count', 'igroup_name_count': 'frequency', 'igroup_name': 'sector'})

    selected_columns = ['nsecode', 'per_chg', 'close', 'date', 'sector', 'count', 'frequency']
    result_list = result[selected_columns]

    # Load old result for comparison
    file_name = f'result/result_{conditionName}.csv'
    if os.path.exists(file_name):
        old_data = pd.read_csv(file_name)
    else:
        old_data = pd.DataFrame(columns=selected_columns)

    old_data = old_data.drop(columns=['date'], errors='ignore')
    new_data_with_date = result_list.drop(columns=['date'])

    # Compare new vs old
    comp_result = compare_csv_files(old_data, new_data_with_date)

    # Save if changed
    if comp_result != True:
        os.makedirs('result', exist_ok=True)
        result.to_csv(file_name, index=False)
        piotista(conditionName)

    return

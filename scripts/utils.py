
from datetime import date, timedelta , datetime
import time
import pandas  as pd


# dt = date(str_date)
# print(dt, "date transformed")

def date_window(str_date = None , ):

    # date window 

    end_dt = date.today() 

    if str_date is not None:
        yr = int(str_date.split('-')[0])
        mon = int(str_date.split('-')[1])
        day = int(str_date.split('-')[2])
        start_dt = date(yr, mon, day)
    else :
        start_dt = end_dt

    

    # difference between current and previous date
    delta = timedelta(days=1)

    # store the dates between two dates in a list
    dates = []

    while start_dt <= end_dt:
        # Check if the current date is not a Saturday (5) or Sunday (6)
        if start_dt.weekday() not in [5, 6]:
            # add current date to list by converting it to iso format
            dates.append(start_dt.strftime('%d%m%Y'))
        # increment start date by timedelta
        start_dt += delta

    print('Dates between', str_date, 'and', end_dt)
    print(dates)
    print('Number of working days:', len(dates))

    return dates


def is_data_available():
     date_str = date.today().strftime('%d%m%Y')
     print(date_str)
     df = pd.read_csv(f'https://archives.nseindia.com/products/content/sec_bhavdata_full_{date_str}.csv')
     df = df.rename(columns=lambda x: x.strip().replace(' ',"_").lower())
     df = df[df['series'] == ' EQ']
     print(df.shape)

     if df.shape[0] > 1:
         return "Data is available"
     else:
         return "oops!! Data is not available"

print(is_data_available())





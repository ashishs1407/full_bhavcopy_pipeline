from sqlalchemy  import create_engine
import pandas as pd
import time
from utils import date_window
import logging


# connection to postgress
engine = create_engine('postgresql+psycopg2://postgres:1407@localhost/DataWarehousex')
print(engine)
start_date = '2024-02-21'

# pd.read_sql_query('Truncate table public.nse_data', engine)


dates = date_window(start_date  )
# date_str = datetime.today().strftime('%d%m%Y')


for date in dates:
    try:
        time.sleep(5)
        df = pd.read_csv(f'https://archives.nseindia.com/products/content/sec_bhavdata_full_{date}.csv')
        df = df.rename(columns=lambda x: x.strip().replace(' ',"_").lower())

        # preprocessing
        df = df[df['series'] == ' EQ']
        
        time.sleep(5)

        df.to_sql('nse_data', engine, if_exists='append', index=False)
        print(f'loaded the data to postgress for {date}')


        time.sleep(5)
    except Exception as e:
        print(e)



# sql to df
# crypto_data_df = pd.read_sql_query('select * from dannys_diner.members', engine)
# print(crypto_data_df)


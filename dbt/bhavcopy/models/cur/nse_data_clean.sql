select 
 avg_price
 , volume
 , turnover_cr
 , open_price
 , high_price
 , low_price
 , prev_close
 , close_price
 , deliv_per
 , series
 , created_date
 , last_price
 , deliv_qty
 , symbol 

 from {{ref('bhavcopy_data')}}
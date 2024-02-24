select
 avg_price :: decimal(13,2) as avg_price
 , ttl_trd_qnty :: decimal(13,0) as volume
 , (turnover_lacs :: decimal(13,2) )/100.00 as  turnover_cr
 , open_price :: decimal(13,2) as open_price
 , high_price :: decimal (13,2) as high_price
 , low_price :: decimal (13,2) as low_price
 , prev_close :: decimal (13,2) as prev_close
 , close_price :: decimal (13,2) as close_price
 , deliv_per :: decimal (13,2) as deliv_per
 , series :: text as series
 , date1 :: date as created_date
 , last_price :: decimal (13,2) as last_price
 , deliv_qty :: decimal (13,0) as deliv_qty
 , symbol :: text as symbol
 from public.nse_data 
--  where date(date1) >= (select max(date(date1)) from datawarehousex.public.nse_data  )
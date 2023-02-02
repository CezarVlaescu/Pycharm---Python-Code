def mayanDate(date_str, seperation=','):
     days_in_kin     = 1
     kin_in_uinal    = 20
     uinal_in_tun    = 18
     tun_in_katun    = 20
     katun_in_baktun = 20

     days_in_uinal   = days_in_kin * kin_in_uinal
     days_in_tun     = days_in_uinal * uinal_in_tun
     days_in_katun   = days_in_tun * tun_in_katun
     days_in_baktun  = days_in_katun * katun_in_baktun

     days_1970 = 12 * days_in_baktun \
     + 17 * days_in_katun\
     + 16 * days_in_tun\
     + 7 * days_in_uinal\
     + 5 * days_in_kin

     total_days = daysPassed(date_str) + days_1970

     baktun = total_days // days_in_baktun
     total_days -= baktun * days_in_baktun
     katun = total_days // days_in_katun
     total_days -= katun * days_in_katun
     tun = total_days // days_in_tun
     total_days -= tun * days_in_tun
     uinal = total_days // days_in_uinal
     total_days -= uinal * days_in_uinal
     kin = total_days // days_in_kin

     print(seperation.join(map(str, (baktun, katun, tun, uinal, kin))))

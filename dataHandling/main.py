from data_fetching import data_fetching

'''Login to the server'''
username = "andreasmaakes"
password = "Terrengmodell69!"


'''
Defining spatial filter
Max_lat: float, min_lat: float, max_lon: float, min_lon: float, inc_angle: float
'''

#Iran spatial filter
'''
max_lat = 36
min_lat = 28
max_lon = 65
min_lon = 54
inc_angle = 65
'''

'''
Dates format: "yyyymmdd"
'''
start_date = "20230312"
end_date = "20230313" 




#Region name that is to be used for naming data folders
name = "Chad"
#Chad spatial filter
min_lat = 10
max_lat = 15
min_lon = 16
max_lon = 21
min_ddm_snr = 1
min_sp_rx_gain = 0
max_sp_rx_gain = 15
#Maximum inclination angle
inc_angle = 65


#Cygnss longitudes have to be corrected 
#Entire africa spatial filter
'''
name = "North-Africa"
min_lat = 2
max_lat = 20
min_lon = -19
max_lon = 38

min_ddm_snr = 1
min_sp_rx_gain = 0
max_sp_rx_gain = 15
inc_angle = 65
'''


data_fetching(start_date, end_date, username, password, max_lat, min_lat, max_lon, min_lon, inc_angle, name, min_ddm_snr, min_sp_rx_gain, max_sp_rx_gain)


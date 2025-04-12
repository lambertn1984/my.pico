#import modules
import wifi_station

# execute the wifi_station script
ip = wifi_station.connect()
connection = wifi_station.open_socket(ip)
wifi_station.serve(connection)


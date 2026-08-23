data_list = [{"id": 1, "temp": 22.5 }, {"id": 2, "temp":"error"}, {"id": 3, "temp": 31.0}]

def read_sensor_data(data_list):
    for data in data_list:
        yield data
        

def get_high_temperatures(data_list):
    temp_grt_30 =[data for data in data_list if isinstance(data["temp"], (int, float)) and data["temp"] > 30]
    return temp_grt_30
#print(get_high_temperatures(data_list))
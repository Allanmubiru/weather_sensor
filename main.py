from models import Sensor,TemperatureSensor

from processor import read_sensor_data, get_high_temperatures, data_list 



def main():
    temperatureSensor_a = TemperatureSensor("S1", "Kampala")
    temperatureSensor_b = TemperatureSensor("S2", "Nwoya")

    valid_records = []
    sensor_number = 0
    sensor_list =[temperatureSensor_a,temperatureSensor_b]

    for record in read_sensor_data(data_list):
        sensor = sensor_list[sensor_number]
        temperature = record["temp"]
        temperature = sensor.record_temperature(temperature)
        if temperature is not None:
            valid_record = {
                "id": record["id"],
                "temp": temperature
            }
            valid_records.append(valid_record)
        sensor_number = sensor_number +1 
        if sensor_number == len(sensor_list):
            sensor_number = 0
    high_temperatures = get_high_temperatures(valid_records)
    print("\nHigh temperatures:")
    print(high_temperatures)
main()
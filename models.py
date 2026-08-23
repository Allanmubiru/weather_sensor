class Sensor:
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location

class TemperatureSensor(Sensor):
    def __init__(self, sensor_id, location):
        super().__init__(sensor_id, location)

    def record_temperature(self, value):
        try:
            value =int(value)
            return value
        except ValueError:
            print(f"Warning: invalid temperature value {value!r} "
                f"for sensor {self.sensor_id}.")



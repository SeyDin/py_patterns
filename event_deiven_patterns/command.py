class Sensor:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def generate_data(self, data):
        self.command.execute(data)


class AlertCommand:
    def execute(self, data):
        if data > 100:
            print("Alert! Temperature is too high")


class RecordCommand:
    def execute(self, data):
        print("Recording data: {}".format(data))


sensor = Sensor()
alert_command = AlertCommand()
record_command = RecordCommand()

sensor.set_command(alert_command)
sensor.generate_data(80)
sensor.generate_data(110)

sensor.set_command(record_command)
sensor.generate_data(80)
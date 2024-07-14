class Sensor:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)


class AlertSystem:
    def update(self, data):
        if data > 100:
            print("Alert! Temperature is too high")


class DataRecorder:
    def update(self, data):
        print("Recording data: {}".format(data))


sensor = Sensor()
alert_system = AlertSystem()
data_recorder = DataRecorder()

sensor.register_observer(alert_system)
sensor.register_observer(data_recorder)

sensor.notify_observers(80)
sensor.notify_observers(110)

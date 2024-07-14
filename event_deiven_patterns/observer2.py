import random
from abc import ABC


class EventManager:
    def __init__(self):
        self.listeners: dict = {}

    def subscribe(self, event_type: str, listener):
        self.listeners.setdefault(event_type, []).append(listener)

    def unsubscribe(self, event_type: str, listener):
        self.listeners[event_type].remove(listener)

    def notify(self, event_type: str, data):
        for listener in self.listeners.get(event_type, []):
            listener.update(data)


class Editor:
    def __init__(self, event_manager: EventManager, file_name: str):
        self.events = event_manager
        self.file_name = file_name

    def write_something(self):
        rand_int = random.randint(0, 100)
        print(f'write number {rand_int} in {self.file_name}')
        self.events.notify('write', {'file_name': self.file_name, 'number': rand_int})

    def save(self):
        print(f'save {self.file_name}')
        self.events.notify('save', {'file_name': self.file_name})


class EventListener(ABC):
    def update(self, data):
        pass


class WriteEventListener(EventListener):
    def update(self, data):
        print(f'{self.__class__.__name__} - I feel something wrote into {data["file_name"]} number {data["number"]}')


class SaveEventListener(EventListener):
    def update(self, data):
        print(f'{self.__class__.__name__} - I feel something saved {data["file_name"]}')


if __name__ == '__main__':

    write_listener = WriteEventListener()
    save_listener = SaveEventListener()

    event_manager = EventManager()
    event_manager.subscribe('write', write_listener)
    event_manager.subscribe('save', save_listener)

    editor = Editor(event_manager, file_name='test.txt')
    editor.write_something()
    editor.save()

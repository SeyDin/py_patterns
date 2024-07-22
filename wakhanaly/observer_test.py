from wakhanaly.observer2_ import WriteEventListener, SaveEventListener, EventManager, Editor

if __name__ == '__main__':

    write_listener = WriteEventListener()
    save_listener = SaveEventListener()

    event_manager = EventManager()
    event_manager.subscribe('write', write_listener)
    event_manager.subscribe('save', save_listener)

    editor = Editor(event_manager, file_name='test.txt')
    editor.write_something()
    editor.save()

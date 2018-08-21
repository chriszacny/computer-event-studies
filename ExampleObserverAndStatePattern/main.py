from abc import ABC, abstractmethod


class EventfulObject(ABC):
    """
    The Subject in the Observer pattern.
    """
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.handle_event(self)


class EventHandler(ABC):
    """
    The Observer in the Observer pattern
    """
    @abstractmethod
    def handle_event(self, eventful_object):
        pass


class TestRun(EventfulObject):
    """
    The ConcreteSubject in the Observer pattern. Notifies observers on state changes.
    """
    def __init__(self):
        super().__init__()
        self._test_state = TestRunPreStartState(self)

    def change_state(self, new_state):
        self.notify()
        self._test_state = new_state
        self.execute()

    def execute(self):
        self._test_state.execute()


class TestRunPreStartState(object):
    """
    States in the State pattern
    """
    def __init__(self, test_run):
        super().__init__()
        self._test_run = test_run

    def execute(self):
        print('Simulating executing run pre-start code.')
        print('.')
        print('.')
        print('.')
        print('Pre-start complete.')
        self._test_run.change_state(TestRunStartState(self._test_run))


class TestRunStartState(object):
    """
    States in the State pattern
    """
    def __init__(self, test_run):
        super().__init__()
        self._test_run = test_run

    def execute(self):
        print('Simulating executing run start code.')
        print('.')
        print('.')
        print('.')
        print('Test run complete.')
        self._test_run.change_state(TestPostRunState(self._test_run))


class TestPostRunState(object):
    """
    States in the State pattern
    """
    def __init__(self, test_run):
        super().__init__()
        self._test_run = test_run

    def execute(self):
        print('Simulating executing post test run code.')
        print('.')
        print('.')
        print('.')
        print('Done.')


class UIStateChangeNotifier(EventHandler):
    def handle_event(self, test_run):
        print('Simulating sending state change websocket data to UI.')


class MSTeamsStateChangeNotifier(EventHandler):
    def handle_event(self, test_run):
        print('Simulating sending state change data to MS Teams.')


def main():
    test_run = TestRun()
    test_run.register_observer(UIStateChangeNotifier())
    test_run.register_observer(MSTeamsStateChangeNotifier())
    test_run.execute()


if __name__ == '__main__':
    main()

class Subject(object):
    def __init__(self):
        self._observers = []
        self._message_prefix = 'SUBJECT: '

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        print('{}Notifying my observers'.format(self._message_prefix))
        for observer in self._observers:
            observer.update()


class Observer(object):
    def __init__(self):
        self._message_prefix = 'OBSERVER: '

    def update(self):
        print('{}Observer method called.'.format(self._message_prefix))


def main():
    my_subject = Subject()
    my_subject.attach(Observer())
    my_subject.notify()


if __name__ == '__main__':
    main()

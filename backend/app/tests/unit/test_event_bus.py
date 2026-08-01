from app.events import EventBus


def test_subscribe_and_publish():

    bus = EventBus()

    received = []

    def listener(data):
        received.append(data)

    bus.subscribe("greeting", listener)

    bus.publish("greeting", "Hello JARVIS")

    assert received == ["Hello JARVIS"]


def test_unsubscribe():

    bus = EventBus()

    received = []

    def listener(data):
        received.append(data)

    bus.subscribe("event", listener)

    bus.unsubscribe("event", listener)

    bus.publish("event", "Should not arrive")

    assert received == []


def test_has_subscribers():

    bus = EventBus()

    def listener(data):
        pass

    bus.subscribe("boot", listener)

    assert bus.has_subscribers("boot") is True


def test_clear():

    bus = EventBus()

    def listener(data):
        pass

    bus.subscribe("boot", listener)

    bus.clear()

    assert bus.has_subscribers("boot") is False
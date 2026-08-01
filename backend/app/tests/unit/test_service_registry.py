from app.registry import ServiceRegistry


def test_register_and_get():

    registry = ServiceRegistry()

    service = object()

    registry.register("logger", service)

    assert registry.get("logger") is service


def test_exists():

    registry = ServiceRegistry()

    registry.register("database", object())

    assert registry.exists("database")


def test_unregister():

    registry = ServiceRegistry()

    registry.register("cache", object())

    registry.unregister("cache")

    assert registry.exists("cache") is False


def test_count():

    registry = ServiceRegistry()

    registry.register("one", object())

    registry.register("two", object())

    assert registry.count() == 2


def test_clear():

    registry = ServiceRegistry()

    registry.register("one", object())

    registry.register("two", object())

    registry.clear()

    assert registry.count() == 0


def test_duplicate_registration():

    registry = ServiceRegistry()

    registry.register("logger", object())

    try:
        registry.register("logger", object())
        assert False
    except ValueError:
        assert True
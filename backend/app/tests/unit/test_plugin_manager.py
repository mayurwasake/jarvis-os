from app.plugins import PluginManager


def test_register_plugin():

    manager = PluginManager()

    plugin = object()

    manager.register("voice", plugin)

    assert manager.get("voice") is plugin


def test_unregister_plugin():

    manager = PluginManager()

    manager.register("voice", object())

    manager.unregister("voice")

    assert manager.exists("voice") is False


def test_list_plugins():

    manager = PluginManager()

    manager.register("voice", object())

    manager.register("browser", object())

    plugins = manager.list_plugins()

    assert plugins == ["browser", "voice"]


def test_duplicate_plugin():

    manager = PluginManager()

    manager.register("voice", object())

    try:
        manager.register("voice", object())
        assert False
    except ValueError:
        assert True


def test_clear():

    manager = PluginManager()

    manager.register("one", object())

    manager.register("two", object())

    manager.clear()

    assert manager.count() == 0
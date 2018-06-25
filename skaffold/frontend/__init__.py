from skaffold import factory


def create_app(settings_override=None):
    app = factory.create_app(__name__, settings_override)
    return app

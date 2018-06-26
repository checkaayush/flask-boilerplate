from flask import Flask, Blueprint
from werkzeug.utils import find_modules, import_string


def _register_blueprints(app, package_name):
    rv = []
    for name in find_modules(package_name, include_packages=True, recursive=True):
        m = import_string(name)
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv


def create_app(package_name, settings_override=None):
    app = Flask(package_name, instance_relative_config=True)
    app.config.from_object('skaffold.config')
    app.config.from_object(settings_override)
    _register_blueprints(app, package_name)
    return app

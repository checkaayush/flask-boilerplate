from werkzeug.wsgi import DispatcherMiddleware

from skaffold import api, frontend


app = DispatcherMiddleware(frontend.create_app(), {
    '/api': api.create_app()
})

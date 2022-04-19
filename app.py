import logging
import connexion


app = connexion.AioHttpApp(__name__, only_one_api=True)
app.add_api('openapi.yaml')

if __name__ == '__main__':
    app.run(port=8081, use_reloader=False, threaded=False,debug=True)
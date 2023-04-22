import sys
sys.dont_write_bytecode = True
import os

from waitress import serve

from app import App


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))

    app = App()

    serve(app, host='0.0.0.0', port=port)

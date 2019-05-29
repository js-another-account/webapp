import os
import webapp.main

debug = os.environ.get('DEBUG', 'false') == 'true'

if __name__ == '__main__':
    webapp.main.app.run(debug=debug, host='0.0.0.0', port=8000)

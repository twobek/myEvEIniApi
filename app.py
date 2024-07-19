import os
from src import create_app

env = os.getenv('EVE_APP_ENV', 'dev')
print(env)

config_name = os.getenv('FLASK_ENV', 'development')
print(config_name)
app = create_app(config_name)

if __name__ == '__main__':
    if env == 'dev':
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0', port=5000)
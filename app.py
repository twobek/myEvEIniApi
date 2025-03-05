import os
from src import create_app

env = os.getenv('EVE_APP_ENV', 'dev')
print(env)

config_name = env
print(config_name)
app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)
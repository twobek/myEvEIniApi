#from controller.main_page import app
#from services.populatetypes import call_eve_type_ids_api,store_ids_in_eve_types_table,manage_eve_types
#from config.dbconfig import db_con
from flask import Flask

app = Flask(__name__, template_folder='../templates')

"""
data = call_eve_type_ids_api(1)
store_ids_in_eve_types_table(db_con, data)
"""

#manage_eve_types(db_con)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000)
import ORM
from flask_login import LoginManager, UserMixin
from flask import Flask, Blueprint, jsonify, request
from add_questions import bp as add_questions_bp
from Administrator_function import bp as administrator_function_bp
from create_polls import bp as create_polls_bp
from delete_polls import bp as delete_polls_bp
from poll_results import bp as poll_results_bp
from Profile_and_settings import bp as profile_and_settings_bp
from User_registration_and_login import bp as user_registration_and_login_bp
import configparser
import datetime
from databes import db
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
#db conncet
db_config = configparser.ConfigParser()
db_config.read('db_connect.ini')
def get_db_uri(cfg):
    res = "mysql+pymysql://" + cfg.get("user") + ":" + cfg.get("password") + "@" + cfg.get("host") + ":" + cfg.get("port") + "/" + cfg.get("database")    
    return res
conn = get_db_uri(db_config['DB_CONNECT'])
app.config['SQLALCHEMY_DATABASE_URI'] = conn
# 是否追蹤資料庫修改，一般不開啟，會影響效能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 是否顯示底層執行的 SQL 語句
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = '111DBMSfinal'


#blue print
app.register_blueprint(add_questions_bp)
app.register_blueprint(administrator_function_bp)
app.register_blueprint(create_polls_bp)
app.register_blueprint(delete_polls_bp)
app.register_blueprint(poll_results_bp)
app.register_blueprint(profile_and_settings_bp)
app.register_blueprint(user_registration_and_login_bp)


# app.secret_key = '111DBMSfinal'
if __name__ == "__main__":
    app.run(debug=True, port=3000)

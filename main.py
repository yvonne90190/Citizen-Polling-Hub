from ORM import app
from flask_login import LoginManager, UserMixin
from flask import Flask, Blueprint, jsonify, request
from add_questions import bp as add_questions_bp
from Administrator_function import bp as administrator_function_bp
from create_polls import bp as create_polls_bp
from delete_polls import bp as delete_polls_bp
from poll_results import bp as poll_results_bp
from Profile_and_settings import bp as profile_and_settings_bp
from User_registration_and_login import bp as user_registration_and_login_bp
from vote_polls import bp as vote_polls_bp
from view_polls import bp as view_polls_bp
from comment_and_reply import bp as comment_and_reply_bp


# blue print
app.register_blueprint(add_questions_bp)
app.register_blueprint(administrator_function_bp)
app.register_blueprint(create_polls_bp)
app.register_blueprint(delete_polls_bp)
app.register_blueprint(poll_results_bp)
app.register_blueprint(profile_and_settings_bp)
app.register_blueprint(user_registration_and_login_bp)
app.register_blueprint(vote_polls_bp)
app.register_blueprint(view_polls_bp)
app.register_blueprint(comment_and_reply_bp)


if __name__ == "__main__":
    app.run(debug=True, port=3000)

from ORM import app, db, User
from flask import request, jsonify, Blueprint
from flask_login import login_required, current_user


bp = Blueprint('profile_and_settings', __name__)
# 用戶可以查看自己的個人資料，如用戶名、電子郵件等。
@bp.route('/user/get_information', methods=['GET'])
@login_required
def get_user_information():
    user_id = current_user.user_id
    user = User.query.get(user_id)
    
    # 如果找到使用者，返回相關資訊
    if user:
        return jsonify({"message": "User information returned.", "username": user.username, "email": user.email}), 200
    
    # 如果找不到使用者，返回相應的錯誤訊息
    return jsonify({'error': 'User doesn\'t exist.'}), 400

# 用戶可以修改帳戶設置，如密碼等。
@bp.route('/user/reset_password', methods=['POST'])
@login_required
def reset_password():
    data = request.get_json()
    user_id = current_user.user_id
    user = User.query.get(user_id)
    if not data['old_password'] or not data['new_password']:
        return jsonify({'error': 'Missing required information. Please provide old_password and new_password.'}), 400
    
    if data['old_password'] != user.password:
        return jsonify({'error': 'Invalid password.'}), 401
    
    # 更新密碼
    user.password = data['new_password']
    
    # 執行資料庫更新操作
    db.session.commit()
    
    return jsonify({'message': 'Password is updated.'}), 200

if __name__ == '__main__':
    app.run(debug=True)

from ORM import app, Poll, db
from flask_login import login_required, current_user
from flask import jsonify, Blueprint


bp = Blueprint('delete_polls', __name__)


@bp.route('/admin/delete_poll/<path:poll_id>', methods=['DELETE'])
@login_required
def delete_poll(poll_id):
    poll = Poll.query.get(poll_id)
    if not poll:
        return jsonify({"error": "Poll not found."}), 404

    if current_user.email != 'admin@nccu.edu.tw' or poll.is_approved:
        return jsonify({"error": "Unauthorized operation."}), 403

    db.session.delete(poll)
    db.session.commit()

    return jsonify({"message": "Poll deleted successfully."}), 200


if __name__ == "__main__":
    app.run(debug=True)

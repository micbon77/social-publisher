from flask import Blueprint, request, jsonify
from models.db import get_db

api = Blueprint('api', __name__)

@api.route('/save-credentials', methods=['POST'])
def save_credentials():
    data = request.json
    platform = data.get("platform")
    access_token = data.get("access_token")
    db = get_db()
    db.execute("INSERT INTO credentials (platform, access_token) VALUES (?, ?)", (platform, access_token))
    db.commit()
    return jsonify({"message": "Credentials saved"}), 200

@api.route('/publish', methods=['POST'])
def publish():
    data = request.json
    content = data.get("content")
    platforms = data.get("platforms", [])

    for platform in platforms:
        print(f"Publishing on {platform}: {content}")
    return jsonify({"message": "Post sent to: " + ", ".join(platforms)}), 200

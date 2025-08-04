from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('id')
    return jsonify({
        "id": user_id,
        "name": "Maria Garcia",
        "plan": "Pro",
        "lang": "es",
        "email": "maria.garcia@example.com"
    })

@app.route('/invoice/last', methods=['GET'])
def get_invoice():
    user_id = request.args.get('user')
    return jsonify({
        "user": user_id,
        "amount": "$12.99",
        "date": "2025-07-15",
        "invoice_id": "INV-98765"
    })

@app.route('/ticket/create', methods=['POST'])
def create_ticket():
    data = request.get_json()
    return jsonify({
        "status": "success",
        "ticket_id": "ZEND12345",
        "issue": data.get("issue", "General Inquiry")
    })

@app.route('/feedback/route', methods=['POST'])
def route_feedback():
    data = request.get_json()
    return jsonify({
        "status": "sent to product",
        "category": data.get("category", "UX"),
        "message": data.get("message", "No message provided.")
    })

@app.route('/help/article', methods=['GET'])
def get_article():
    article_id = request.args.get('id')
    return jsonify({
        "article_id": article_id,
        "title": "How to Apply a Brand Kit in Canva",
        "steps": [
            "Go to your brand kit settings",
            "Select the brand kit you want to use",
            "Apply it to your design from the toolbar"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

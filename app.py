from flask import Flask, render_template, jsonify, request
from models import db, AccessLog
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logs')
def logs():
    ip = request.args.get('ip')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    query = AccessLog.query
    if ip:
        query = query.filter(AccessLog.ip == ip)
    if start_date:
        query = query.filter(AccessLog.date >= start_date)
    if end_date:
        query = query.filter(AccessLog.date <= end_date)
    logs = query.all()
    return render_template('logs.html', logs=logs)


@app.route('/api/logs')
def api_logs():
    ip = request.args.get('ip')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    query = AccessLog.query
    if ip:
        query = query.filter(AccessLog.ip == ip)
    if start_date:
        query = query.filter(AccessLog.date >= start_date)
    if end_date:
        query = query.filter(AccessLog.date <= end_date)
    logs = query.all()
    return jsonify([log.to_dict() for log in logs])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
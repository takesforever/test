from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.tvmg70z.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    price_receive = int(size_receive.strip('평'))*500

    doc = {
        'name':name_receive,
        'address':address_receive,
        'size':size_receive,
        'price':price_receive
    }
    db.remars.insert_one(doc)

    return jsonify({'msg': 'successfully ordered!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    order_list = list(db.remars.find({}, {'_id': False}))
    return jsonify({'orders': order_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.demoDb


@app.route('/')
def home():
        
        _items = db.demoDb.find()
        items = [item for item in _items]

        return render_template('home.html', items=items)


@app.route('/api/items', methods=['POST'])
def createItem():

        item = {
                'description': request.form['description']
        }
        db.demoDb.insert_one(item)

        return redirect(url_for('home'))

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)        
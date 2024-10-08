from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Replace this with your actual MongoDB Atlas connection string
client = MongoClient("mongodb+srv://avantiikaa11:Avt111203@exercismcluster.fkwqk.mongodb.net/")
db = client['exercism_db']
exercises_collection = db['exercises']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exercises')
def exercises():
    # Fetch exercises from MongoDB
    exercises = exercises_collection.find()
    return render_template('exercises.html', exercises=exercises)

@app.route('/exercise/<id>')
def exercise_detail(id):
    exercise = exercises_collection.find_one({"_id": ObjectId(id)})
    return render_template('exercise_detail.html', exercise=exercise)

if __name__ == '__main__':
    app.run(debug=True)

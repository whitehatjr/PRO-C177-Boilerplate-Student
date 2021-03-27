from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

answer_dict={
                "1": ["Black", "Gorilla", "Dancing", "Madagascar", "Nice", "White", "Tigers", "Move"],
                "2": ["Sunday", "Aunt", "Dog", "Burgers", "Soft Drinks", "Nice", "Cards"],
                "3": ["Smelly", "Cat", "California", "Cat", "Blue", "3", "Fishes", "Dance", "Songs", "Sad", "Childishly", "Happy"]
            }




#ADD stories data here!





@app.route("/")
def index():
    return render_template("index.html")
    

#ADD "/get-story" API here!!


    


@app.route("/post-answers", methods=["POST"])
def post_answers():
    story_id = request.json.get("story_id")
    values = request.json.get("values")
    answers = answer_dict.get(story_id)
    index, score = 0, 0
    while index < len(values):
        if values[index].lower() == answers[index].lower():
            score += 1
        index += 1
    return jsonify({
        "status": "success",
        "result": f"{score} / {len(values)}"
    })

if __name__ == "__main__":
    app.run(debug=True)
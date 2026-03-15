from flask import Flask, render_template, request

app = Flask(__name__)

# Define your mood keywords
mood_dataset = {
    "Happy": ["happy", "joy", "amazing", "smile", "wonderful"],
    "Sad": ["sad", "lonely", "bad", "heartbroken", "down"],
    "Angry": ["angry", "frustrated", "annoyed", "mad", "irritated"],
    "Excited": ["excited", "thrilled", "pumped", "can't wait", "super excited"],
    "Romantic": ["love","want him","want her", "romantic", "crush", "heart", "together"],
    "Motivated": ["motivated", "inspired", "determined", "goal", "dream"]
}

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    bg_image = "bg.jpg"

    if request.method == "POST":
        user_text = request.form["text"].lower()
        prediction = "Happy"

        for mood, keywords in mood_dataset.items():
            for word in keywords:
                if word in user_text:
                    prediction = mood
                    break
            if prediction != "Happy":
                break

        # Background selection
        bg_map = {
            "Happy": "happy.jpg",
            "Sad": "sad.jpg",
            "Angry": "angry.jpg",
            "Excited": "excited.jpg",
            "Romantic": "romantic.jpg",
            "Motivated": "motivated.jpg"
        }

        bg_image = bg_map.get(prediction, "bg.jpg")

    return render_template("index.html", prediction=prediction, bg_image=bg_image)
if __name__ == "__main__":
    app.run(debug=True)

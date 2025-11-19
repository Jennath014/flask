from flask import Flask, render_template, request, abort

app = Flask(__name__)

# Sample movie data (list of dicts). You can expand this later or load from a JSON/DB.
movies = [
    {
        "id": 1,
        "title": "Frankenstein ",
        "year": 2025,
        "genre": "Gothic novel and science fiction",
        "desc": "A Swiss student, Victor Frankenstein, creates a sapient creature in an unorthodox scientific experiment, only to abandon it in horror, leading the intelligent, yet isolated and embittered, monster to seek revenge on its creator and his family. ",
        "image": "franketein1.jpg"
    },
    {
        "id": 2,
        "title": "SPY X FAMILY",
        "year": 2022,
        "genre": "anime",
        "desc": "A spy must build a fake family to complete his mission, unaware that his adopted daughter is a telepath and his new wife is a professional assassin, and only the daughter knows everyone's secrets. ",
        "image": "SPY X FAMILY.jpg"
    },
    {
        "id": 3,
        "title": "Coco ",
        "year": 2017,
        "genre": "animation",
        "desc": "Aspiring musician Miguel is accidentally transported to the vibrant Land of the Dead, where he must seek the help of his deceased ancestors to return to the living world and uncover the real story behind his family's mysterious ban on music.",
        "image": "Coco.jpg"
    },
    {
        "id": 4,
        "title": "Zootopia",
        "year": 2016,
        "genre": "animation",
        "desc": "In a city of anthropomorphic animals, a rookie bunny police officer and a cynical con artist fox must work together to uncover a criminal conspiracy that threatens the peace between predators and prey.",
        "image": "zootopia.jpg"
    },
    {
        "id": 5,
        "title": "IT",
        "year": 2017,
        "genre": "Horror thriller",
        "desc": "A group of bullied children in Derry, Maine, band together to defeat an ancient, shape-shifting evil that emerges from the sewers every 27 years to prey on children by taking the form of a terrifying clown named Pennywise. ",
        "image": "it.jpg"
    }
]


@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    if query:
        q = query.lower()
        filtered = [m for m in movies if q in m["title"].lower() or q in m["genre"].lower()]
        return render_template("home.html", movies=filtered, query=query, results=len(filtered))
    return render_template("home.html", movies=movies, query="", results=len(movies))


@app.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if not movie:
        abort(404)
    return render_template("movie.html", movie=movie)


if __name__ == "__main__":
    app.run(debug=True)

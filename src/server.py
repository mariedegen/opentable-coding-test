from difflib import SequenceMatcher

from flask import Flask, request

from encoder import Encoder

app = Flask(__name__)
encoder = Encoder()


@app.route("/embeddings", methods=["GET"])
def route_get_embeddings():
    sentence = request.args.get("sentence")
    if sentence is None or type(sentence) is not str:
        return {"message": "Invalid input, pass sentence as string"}, 400

    return {
        "embedding": encoder.get_embeddings([sentence])[0],
    }


@app.route("/embeddings/bulk", methods=["POST"])
def post_embeddings_bulk():
    call_body = request.json
    sentences = call_body.get("sentences")

    if sentences is None or type(sentences) is not list:
        return {"message": "Invalid input, pass sentences as list of strings"}, 400

    return {
        "embeddings": encoder.get_embeddings(sentences),
    }


@app.route("/embeddings/similarity", methods=["POST"])
def post_embeddings_similarity():
    call_body = request.json
    sentence1 = call_body.get("sentence_1")
    sentence2 = call_body.get("sentence_2")

    if sentence1 is None or type(sentence1) is not str or sentence2 is None or type(sentence2) is not str:
        return {"message": "Invalid input, pass strings sentence_1 and sentence_2"}, 400

    seq_match = SequenceMatcher(None, sentence1, sentence2)
    similarity = seq_match.ratio()
    return {
        "similarity": similarity,
    }


if __name__ == "__main__":
    app.run(port=5000, debug=True)

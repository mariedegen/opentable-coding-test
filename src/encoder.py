from typing import List

import tensorflow_hub as hub

UNIVERSAL_SENTENCE_ENCODER = "https://tfhub.dev/google/universal-sentence-encoder/4"


def load_encoder(url=UNIVERSAL_SENTENCE_ENCODER):
    return hub.load(url)


class Encoder:
    def __init__(self):
        self.__embed = load_encoder()

    def get_embeddings(self, sentences: List[str]):
        return self.__embed(sentences).numpy().tolist()

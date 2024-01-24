import numpy as np
import pickle
import tensorflow_hub as hub
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from sklearn.metrics.pairwise import cosine_similarity
from chatterbot import languages


class DialogueManager(object):
    def __init__(self, use_model_url, dataset_path):
        self.model = hub.load(use_model_url)
        self.dataset = pickle.load(open(dataset_path, mode='rb'))
        self.QUESTION_VECTORS = self.dataset.Question_Vector
        self.COSINE_THRESHOLD = 0.5
        self.lng = languages.ENG
        self.lng.ISO_639_1 = 'en_core_web_sm'
        self.chitchat_bot = ChatBot("Chatterbot", tagger_language=self.lng)
        trainer = ChatterBotCorpusTrainer(self.chitchat_bot)
        trainer.train("chatterbot.corpus.english")

    def embed(self, input):
        return np.array(self.model([input]))

    def semantic_search(self, query):
        query_vec = self.embed(query)
        sims = [cosine_similarity(query_vec, que_vec)[0][0] for que_vec in self.QUESTION_VECTORS]
        most_similar_index = np.argmax(sims)
        most_relevant_sim_score = sims[most_similar_index]
        return most_similar_index, most_relevant_sim_score

    def generate_answer(self, question):
        index, similarity_score = self.semantic_search(question)

        if similarity_score >= self.COSINE_THRESHOLD:
            answer = self.dataset.Answer[index]
        else:
            answer = self.chitchat_bot.get_response(question)

        return answer

# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy

app = Flask(__name__)
CORS(app)

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")
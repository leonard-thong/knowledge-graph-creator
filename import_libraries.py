import pandas as pd
import re
import bs4
import requests
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm

import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokens import Span

nlp = spacy.load('en_core_web_sm')
pd.set_option('display.max_colwidth', 200)
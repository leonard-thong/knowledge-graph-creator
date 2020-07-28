from import_libraries import tqdm

from entity_extraction.get_entities import get_entities
from read_data import candidate_sentences

entity_pairs = []

for i in tqdm(candidate_sentences["sentence"]):
    entity_pairs.append(get_entities(i))

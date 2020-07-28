from read_data import candidate_sentences
from import_libraries import nlp, tqdm, Matcher


def get_relation(sent):
    doc = nlp(sent)

    # Matcher class object
    matcher = Matcher(nlp.vocab)

    # Define the pattern
    pattern = [{'DEP': 'ROOT'},
               {'DEP': 'prep', 'OP': "?"},
               {'DEP': 'agent', 'OP': "?"},
               {'POS': 'ADJ', 'OP': "?"}]

    # Add pattern to the matcher
    matcher.add("matching_1", None, pattern)

    # Get matches with the matcher function
    matches = matcher(doc)

    # Get the span
    k = len(matches) - 1
    span = doc[matches[k][1]:matches[k][2]]

    return (span.text)

relations = [get_relation(i) for i in tqdm(candidate_sentences['sentence'])]
print(relations)
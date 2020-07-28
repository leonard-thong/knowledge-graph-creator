from entity_extraction.extract_entities import entity_pairs
from relation_extraction.get_relation import relations
from import_libraries import pd

# extract subject
source = [i[0] for i in entity_pairs]

# extract object
target = [i[1] for i in entity_pairs]

kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})
print(kg_df)
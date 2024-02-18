import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import json

# Sample text
text = """
* Samsung Galaxy A546 A54 5G 8/128gb graph OEM EAN 8806094891973
* Samsung Galaxy A546 A54 5G 8/128gb violet OEM EAN 8806094891980
* Samsung Galaxy A546 A54 5G 8/128gb lime OEM EAN 8806094891997
* Samsung Galaxy A546 A54 5G 8/128gb white OEM EAN 8806094891966
"""

# Define the patterns for matching
patterns = [
    {"label": "BRAND", "pattern": [{"LOWER": {"IN": ["samsung", "galaxy"]}}]},
    {"label": "NAME", "pattern": [{"POS": "PROPN"}, {"POS": "PROPN"}, {"IS_DIGIT": True}]},
    {"label": "MODEL", "pattern": [{"POS": "PROPN"}, {"IS_DIGIT": True}, {"IS_ALPHA": True}, {"IS_DIGIT": True}]},
    {"label": "COLOR", "pattern": [{"POS": "ADJ"}]},
    {"label": "EAN", "pattern": [{"SHAPE": "xxxx"}]},
]

# Initialize Matcher with the patterns
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
for label, pattern in patterns:
    matcher.add(label, pattern)

# Define a custom pipeline component to extract structured information
def extract_info_component(doc):
    matcher = Matcher(nlp.vocab)
    for pattern in patterns:
        label = pattern["label"]
        pattern_definition = pattern["pattern"]
        matcher.add(label, pattern_definition)

# Add the custom component to the pipeline
nlp.add_pipe(extract_info_component, name="extract_info", last=True)

# Process the text
doc = nlp(text)

# Extracted entities
entities = []
for ent in doc.ents:
    entities.append({"label": ent.label_, "text": ent.text})

# Print the extracted entities
print(json.dumps(entities, indent=4))

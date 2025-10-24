import spacy
import concepcy

nlp = spacy.load('en_core_web_sm')
# Using default concepCy configuration
nlp.add_pipe('concepcy')

doc = nlp('WHO is a lovely company')

# Access all the 'RelatedTo' relations from the Doc
for word, relations in doc._.relatedto.items():
    print(f'Word: {word}{relations}')

# Access the 'RelatedTo' relations word by word
for token in doc:
    print(f'Word: {token} {token._.relatedto}')
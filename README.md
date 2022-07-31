<img src="figures/concepcy.png" width="40%" align="right"/>

# concepCy

[![PyPI version](https://badge.fury.io/py/concepCy.svg)](https://pypi.org/project/concepCy/)
[![github actions docs](https://github.com/JulesBelveze/concepcy/actions/workflows/documentation.yaml/badge.svg)](https://julesbelveze.github.io/concepcy/)

`concepCy` is a spaCy wrapper for [ConceptNet](https://conceptnet.io/), a freely-available semantic network designed to
help computers understand the meaning of words.

`concepCy` allows you to query [ConceptNet.io](https://conceptnet.io/) to extract word meanings directly from the
resource itself.

# Install

You can install `concepCy` via pip:

```
pip install concepcy
```

Alternatively you can directly clone the repository and install it using [poetry](https://python-poetry.org/docs/) by
running the following:

```
git clone https://github.com/JulesBelveze/concepcy.git
cd concepcy
poetry install
```

## Getting Started

To get started you need to install of one the pre-trained spaCy model available [here](https://spacy.io/models).

In `ConceptNet` words are represented as `Node` and relations between words as `Edge`. \
The `Node` object contains the following attributes:

* `id`: where you can look up all the information about that word
* `label`: which may be a more complete phrase such as "an example" instead of just the word "example" that appears in
  the URI.
* `language`: code for what language the `label` is in
* `term`: a link to the most general version of this term. In many cases this is just the same URI.

The `Edge` object features the following attributes:

* `start`: starting `Node`
* `end`: ending `Node`
* `relation`: name of the relation for those two nodes
* `text`: some of ConceptNet's data is extracted from text, `text` shows you what this text was
* `weight`: how believable the information is

### Simple start

In this case we will simply be interested in the *RelatedTo* relations between words.

```python
import spacy
import concepcy

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("concepcy")

doc = nlp("WHO is a lovely company")

# Access all the "RelatedTo" relations from the Doc
print("--- All the 'RelatedTo' relations from the Doc ---")
for word, relations in doc._.relatedto.items():
    print(f"Word: '{word}'\n{relations}")

# Access the "RelatedTo" relations word by word
print("--- The 'RelatedTo' relations word by word ---")
for token in doc:
    print(f"Word: '{token}'\n{token._.relatedto}\n")
```

```bash
--- All the 'RelatedTo' relations from the Doc ---
Word: 'company'
[{'start': {'id': '/c/en/company', 'type': 'Node', 'label': 'company', 'language': 'en', 'term': '/c/en/company'}, 'end': {'id': '/c/en/business', 'type': 'Node', 'label': 'business', 'language': 'en', 'term': '/c/en/business'}, 'relation': 'RelatedTo', 'text': '[[company]] is related to [[business]]', 'weight': 6.424017434596516}, {'start': {'id': '/c/en/company', 'type': 'Node', 'label': 'company', 'language': 'en', 'term': '/c/en/company'}, 'end': {'id': '/c/en/corporation', 'type': 'Node', 'label': 'corporation', 'language': 'en', 'term': '/c/en/corporation'}, 'relation': 'RelatedTo', 'text': '[[company]] is related to [[corporation]]', 'weight': 4.432155231938521}, {'start': {'id': '/c/en/company', 'type': 'Node', 'label': 'company', 'language': 'en', 'term': '/c/en/company'}, 'end': {'id': '/c/en/organization', 'type': 'Node', 'label': 'organization', 'language': 'en', 'term': '/c/en/organization'}, 'relation': 'RelatedTo', 'text': '[[company]] is related to [[organization]]', 'weight': 4.259107887809371}]

--- The 'RelatedTo' relations word by word ---
Word: 'WHO'
[]

Word: 'is'
[]

Word: 'a'
[]

Word: 'lovely'
[]

Word: 'company'
[{'start': {'id': '/c/en/company', 'type': 'Node', 'label': 'company', 'language': 'en', 'term': '/c/en/company'}, 'end': {'id': '/c/en/business', 'type': 'Node', 'label': 'business', 'language': 'en', 'term': '/c/en/business'}, 'relation': 'RelatedTo', 'text': '[[company]] is related to [[business]]', 'weight': 6.424017434596516}, {'start': {'id': '/c/en/company', 'type': 'Node', 'label': 'company', 'language': 'en', 'term': '/c/en/company'}, 'end': {'id': '/c/en/corporation', 'type': 'Node', 'label': 'corporation', 'language': 'en', 'term': '/c/en/corporation'}, 'relation': 'RelatedTo', 'text': '[[company]] is related to [[corporation]]', 'weight': 4.432155231938521}, {'start': {'id': '/c/en/company', 'type': 'Node', 'label': 'company', 'language': 'en', 'term': '/c/en/company'}, 'end': {'id': '/c/en/organization', 'type': 'Node', 'label': 'organization', 'language': 'en', 'term': '/c/en/organization'}, 'relation': 'RelatedTo', 'text': '[[company]] is related to [[organization]]', 'weight': 4.259107887809371}]
```

### Custom configuration

One can customize the `concepcy` wrapper by changing the default value of the config. The two parameters of interest
are:

* `relations_of_interest: List[str]`: ConceptNet currently support 34 word-relations. Some of them might not be needed
  for your use case. To only keep the ones needed pass a list of all the relations you want to keep (see all relations
  available [here](https://github.com/commonsense/conceptnet5/wiki/Relations)). Each relation then becomes an extension.
* `filter_edge_fct: Callable[Edge]`: Conceptnet is a crowd-sourced resource, meaning that some information might be more
  relevant than others. To only keep reliable relations you can pass a function that will take an `Edge` as input and
  will return a boolean indicating whether to filter that edge or not.

```python
import spacy
import concepcy

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe(
    "concepcy",
    config={
        "relations_of_interest": ["MotivatedByGoal", "CapableOf"],
        "filter_edge_weight": 3.0,
        "filter_missing_text": True,
        "as_dict": False
    }
)
```

# Documentation 📚

The whole documentation along with design decisions and examples can be
found [here](https://julesbelveze.github.io/concepcy/).

# References

* [ConceptNet 5.5: An Open Multilingual Graph of General Knowledge](https://arxiv.org/abs/1612.03975)

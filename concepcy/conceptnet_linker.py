import os
from collections import ChainMap, defaultdict
from typing import List, Dict

from request_boost import boosted_requests
from spacy.language import Language
from spacy.tokens import Doc, Token


@Language.factory(
    "concepcy",
    default_config={
        "url": "https://api.conceptnet.io/c/",
        "relations_of_interest": [
            "RelatedTo",
            "SimilarTo",
            "IsA",
            "PartOf",
            "InstanceOf"
        ]
    },
    assigns=["token._.concepts"]
)
class ConcepCyComponent:
    def __init__(
            self,
            nlp: Language,
            name: str,
            url: str,
            relations_of_interest: List[str]
    ):
        self.relations_of_interest = relations_of_interest
        self.url = os.path.join(url, nlp.lang)
        Doc.set_extension("concepts", default={})
        Token.set_extension("concepts", default={})

    def _make_requests(self, words: List[str]) -> List[Dict]:
        """"""
        urls = [os.path.join(self.url, word) for word in words]
        responses = boosted_requests(urls=urls, no_workers=32, max_tries=5, timeout=5, headers=None, parse_json=True)
        return responses

    def _parse_response(self, response: Dict) -> Dict[str, Dict[str, List]]:
        """"""
        word = response["@id"].split("/")[-1]  # retrieving word

        enrichments = defaultdict(list)
        for edge in response["edges"]:
            relation = edge["@id"].split("/")[4]
            if relation in self.relations_of_interest:
                enrichments[relation].append({"weight": edge["weight"], "text": edge["surfaceText"]})
        return {word: enrichments}

    def __call__(self, doc: Doc) -> Doc:
        """"""
        words = set()
        for token in doc:
            if token.is_punct or token.is_stop or token.ent_type != 0:
                continue
            words.add(token.lemma_)
        responses = self._make_requests(list(words))
        enrichments = dict(ChainMap(*map(self._parse_response, responses)))

        for token in doc:
            if token.is_punct or token.is_stop or token.ent_type != 0:
                continue
            token._.concepts = enrichments[token.lemma_]

        return doc


if __name__ == "__main__":
    import spacy
    import time

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("concepcy")

    s = time.time()
    doc = nlp(
        """The Jan. 6 select committee’s latest public hearing went inside the White House to detail then-President 
        Donald Trump’s hourslong refusal to call for an end to the Capitol riot. The hearing marked the final scheduled 
        presentation of the committee’s initial findings from its investigation of the Jan. 6, 2021, insurrection until 
        September."""
    )
    print(time.time() - s)

    for token in doc:
        print(token._.concepts)

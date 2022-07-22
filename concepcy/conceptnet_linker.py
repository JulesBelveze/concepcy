import os
from typing import List, Dict

import requests
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

    def _make_request(self, word: str) -> Dict[str, List[Dict]]:
        """"""
        response = requests.get(os.path.join(self.url, word))
        content = response.json()

        enrichments = {rel: [] for rel in self.relations_of_interest}
        for edge in content["edges"]:
            relation = edge["@id"].split("/")[4]
            if relation in self.relations_of_interest:
                enrichments[relation].append({"weight": edge["weight"], "text": edge["surfaceText"]})

        return enrichments

    def __call__(self, doc: Doc) -> Doc:
        """"""
        for token in doc:
            if token.is_punct or token.is_stop or token.ent_type != 0:
                continue
            enrichments = self._make_request(token.lemma_)
            token._.concepts = enrichments
            doc._.concepts = enrichments
        return doc


if __name__ == "__main__":
    import spacy

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("concepcy")

    import time
    s = time.time()
    doc = nlp(
        """The Jan. 6 select committee’s latest public hearing went inside the White House to detail then-President Donald Trump’s hourslong refusal to call for an end to the Capitol riot. The hearing marked the final scheduled presentation of the committee’s initial findings from its investigation of the Jan. 6, 2021, insurrection until September."""
    )
    print(time.time() - s)

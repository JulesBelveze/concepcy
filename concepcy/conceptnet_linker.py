from collections import ChainMap, defaultdict
from typing import List, Dict, Callable

from request_boost import boosted_requests
from spacy.language import Language
from spacy.tokens import Doc, Token

from .utils import ConceptnetParser


@Language.factory(
    "concepcy",
    default_config={
        "url": "https://api.conceptnet.io/query?node=/c/{lang}/{word}&other=/c/{lang}",
        "relations_of_interest": [
            "RelatedTo",
            "SimilarTo",
            "InstanceOf"
        ],
        "filter_edge_fct": lambda x: x.text is None or x.weight < 4.0
    }
)
class ConcepCyComponent:
    """ConceptNet component for spaCy pipeline"""

    def __init__(
            self,
            nlp: Language,
            name: str,
            url: str,
            relations_of_interest: List[str],
            filter_edge_fct: Callable = None,
            as_dict: bool = True
    ):
        """

        :param nlp: spaCy language object
        :param name:
        :param url: ConceptNet url to query
        :param relations_of_interest: list of relations to keep
        :param as_dict: whether to transform `Edge`s into a dict or not
        :param filter_edge_fct: function to filter out some `Edge`s
        """
        self.url = url
        self.lang = nlp.lang
        self.parser = ConceptnetParser(relations_of_interest, as_dict, filter_edge_fct)

        for relation in relations_of_interest:
            Doc.set_extension(relation.lower(), default=defaultdict(list))
            Token.set_extension(relation.lower(), default=[])

    def _make_requests(self, words: List[str]) -> List[Dict]:
        """
        Execute queries for every node in a parallel-fashion

        :param words: Node to query
        :return:
        """
        urls = [self.url.format(word=word, lang=self.lang) for word in words]
        responses = boosted_requests(urls=urls, no_workers=32, max_tries=5, timeout=5, headers=None, parse_json=True,
                                     verbose=False)
        return responses

    def __call__(self, doc: Doc) -> Doc:
        """
        Attaches enrichments to Tokens and Doc

        :param doc:
        :return: enriched Doc
        """
        words = set()
        for token in doc:
            # skipping punctuation, stop word and entities
            if token.is_punct or token.is_stop or token.ent_type != 0:
                continue
            words.add(token.lemma_)

        responses = self._make_requests(list(words))
        enrichments = dict(ChainMap(*map(self.parser, responses)))

        for token in doc:
            if token.is_punct or token.is_stop or token.ent_type != 0:
                continue

            token_enrichments = enrichments[token.lemma_]
            for relation, enrich in token_enrichments.items():
                token._.get(relation.lower()).extend(enrich)
                doc._.get(relation.lower())[token.text].extend(enrich)

        return doc


if __name__ == "__main__":
    import spacy

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("concepcy")

    doc = nlp(
        """The Jan. 6 select committee’s latest public hearing went inside the White House to detail then-President Donald Trump’s hourslong refusal to call for an end to the Capitol riot. The hearing marked the final scheduled presentation of the committee’s initial findings from its investigation of the Jan. 6, 2021, insurrection until September."""
    )

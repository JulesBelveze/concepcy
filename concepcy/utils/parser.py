import re
from collections import defaultdict
from typing import List, Dict, Union, Callable, Optional

from .types import Node, Edge


class ConceptnetParser:
    """
    Helper class to parse ConceptNet API responses
    """

    def __init__(self, relations_of_interest: List[str], as_dict: bool, filter_edge_fct: Optional[Callable]):
        """
        Args:
            relations_of_interest (List[str]):
                list of relations to keep
            as_dict (bool):
                whether to transform `Edge` objects into a dict
            filter_edge_fct (Optional[Callable]):
                function to filter out `Edge`
        """
        self.relations = relations_of_interest
        self.as_dict = as_dict
        self.filter_edge_fct = filter_edge_fct

    def parse_response(self, response: Dict) -> Dict[str, List[Union[Edge, Dict]]]:
        """
        Parses ConceptNet API response

        Args:
            response (Dict):
                ConceptNet API response
        Returns:
            Dict[str, List[Union[Edge, Dict]]]:
                dictionary with key the relation and value the list of edges corresponding
                to that relation
        """
        word = re.search(r"/(\w+)&other", response["@id"]).groups()[0]

        enrichments = defaultdict(list)
        for edge in response["edges"]:
            relation = edge["@id"].split("/")[4]
            if relation in self.relations:
                edge = Edge(
                    start=Node(**edge["start"]),
                    end=Node(**edge["end"]),
                    relation=relation,
                    text=edge["surfaceText"],
                    weight=edge["weight"]
                )
                if self.filter_edge_fct is not None:
                    if self.filter_edge_fct(edge):
                        continue

                if self.as_dict:
                    edge = edge.dict()

                enrichments[relation].append(edge)

        return {word: enrichments}

    def __call__(self, response: Dict) -> Dict[str, List[Union[Edge, Dict]]]:
        """
        Args:
            response (Dict):
                response sent by the ConceptNet API

        Returns:
            Dict[str, List[Union[Edge, Dict]]]:
                dictionary with key the relation and value the list of edges corresponding
                to that relation
        """
        return self.parse_response(response)

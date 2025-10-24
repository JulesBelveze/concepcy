import re
from collections import defaultdict
from typing import Callable, Dict, List, Optional, Union

from .types import Edge, Node


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
        if not response:
            return {}

        match = re.search(r"/(\w+)&other", response.get("@id", ""))
        if not match:
            return {}
        word = match.group(1)

        enrichments = defaultdict(list)
        for edge_data in response.get("edges", []):
            relation_id = edge_data.get("@id", "")
            parts = relation_id.split("/")
            relation = parts[4] if len(parts) > 4 else None
            if relation not in self.relations:
                continue

            start_data = edge_data.get("start")
            end_data = edge_data.get("end")
            if not start_data or not end_data:
                continue

            edge = Edge(
                start=Node(**start_data),
                end=Node(**end_data),
                relation=relation,
                text=edge_data.get("surfaceText"),
                weight=edge_data.get("weight", 0.0),
            )

            if self.filter_edge_fct is not None and self.filter_edge_fct(edge):
                continue

            if self.as_dict:
                enrichments[relation].append(edge.model_dump())
            else:
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

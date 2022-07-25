import re
from collections import defaultdict
from typing import List, Dict

from pydantic import BaseModel, Field


class Node(BaseModel):
    id: str = Field(alias="@id")
    type: str = Field(alias="@type")
    label: str
    language: str
    term: str

    class Config:
        extra = "allow"

    def __str__(self):
        return f"<Node='{self.label}'>"

    def __repr__(self):
        return f"<Node='{self.label}'>"


class Edge(BaseModel):
    start: Node
    end: Node
    relation: str
    text: str = None
    weight: float


class ConceptnetParser:
    def __init__(self, relations_of_interest: List[str]):
        self.relations = relations_of_interest

    def parse_response(self, response: Dict) -> Dict[str, List[Edge]]:
        """"""
        word = re.search(r"/(\w+)&other", response["@id"]).groups()[0]

        enrichments = defaultdict(list)
        for edge in response["edges"]:
            relation = edge["@id"].split("/")[4]
            if relation in self.relations:
                enrichments[relation].append(
                    Edge(
                        start=Node(**edge["start"]),
                        end=Node(**edge["end"]),
                        relation=relation,
                        text=edge["surfaceText"],
                        weight=edge["weight"]
                    )
                )
        return {word: enrichments}

    def __call__(self, response: Dict) -> Dict[str, List[Edge]]:
        return self.parse_response(response)

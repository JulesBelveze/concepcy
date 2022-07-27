from pydantic import BaseModel, Field


class Node(BaseModel):
    """Class representing a Node of ConceptNet which is a word of natural language"""
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
    """Class representing a ConceptNet's edge which is a relation linking one node to another"""
    start: Node
    end: Node
    relation: str
    text: str = None
    weight: float

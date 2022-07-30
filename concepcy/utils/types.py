from pydantic import BaseModel, Field


class Node(BaseModel):
    """Class representing a Node of ConceptNet which is a word of natural language"""

    id: str = Field(
        alias="@id",
        description="Where you can look up all the information about that node"
    )
    label: str = Field(
        description="A human-readable label, which may be a more complete phrase such as"
              "'an example' instead of just the word 'example' that appears in the URI."
    )
    language: str = Field(
        description="A language code for what language the label is in"
    )
    term: str = Field(
        description="A link to the most general version of this term"
    )

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

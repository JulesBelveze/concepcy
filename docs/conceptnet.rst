ConceptNet
==============================

Directly quoting `ConceptNet.io <https://conceptnet.io/>`_:

::

  ConceptNet is a freely-available semantic network, designed to help computers
  understand the meanings of words that people use.

It enables you given a word (a *node* in ConceptNet terms) to extract its different relations (an *edge* in ConceptNet terms) with other words.

It is multilingual and allows you to obtain relations between words from different languages.

At the time of writing the following relations are available:

.. list-table:: Relations
    :widths: 25 55 20
    :header-rows: 1

    * - Relation
      - Description
      - Examples
    * - RelatedTo
      - The most general relation. There is some positive relationship between A and B, but ConceptNet can't determine what that relationship is based on the data. This was called "ConceptuallyRelatedTo" in ConceptNet 2 through 4. Symmetric.
      - learn ↔ erudition
    * - FormOf
      - A is an inflected form of B; B is the root word of A.
      - slept → sleep
    * - IsA
      - A is a subtype or a specific instance of B; every A is a B. This can include specific instances; the distinction between subtypes and instances is often blurry in language. This is the hyponym relation in WordNet.
      - car → vehicle; Chicago → city
    * - PartOf
      - A is a part of B. This is the part meronym relation in WordNet.
      - gearshift → car
    * - HasA
      - B belongs to A, either as an inherent part or due to a social construct of possession. HasA is often the reverse of PartOf.
      - bird → wing; pen → ink
    * - UsedFor
      - A is used for B; the purpose of A is B.
      - bridge → cross water
    * - CapableOf
      - Something that A can typically do is B.
      - knife → cut
    * - AtLocation
      - A is a typical location for B, or A is the inherent location of B. Some instances of this would be considered meronyms in WordNet.
      - butter → refrigerator; Boston → Massachusetts
    * - Causes
      - A and B are events, and it is typical for A to cause B.
      - exercise → sweat
    * - HasSubevent
      - A and B are events, and B happens as a subevent of A.
      - eating → chewing
    * - HasFirstSubevent
      - A is an event that begins with subevent B.
      - sleep → close eyes
    * - HasLastSubevent
      - A is an event that concludes with subevent B.
      - cook → clean up kitchen
    * - HasPrerequisite
      - In order for A to happen, B needs to happen; B is a dependency of A.
      - dream → sleep
    * - HasProperty
      - A has B as a property; A can be described as B.
      - ice → cold
    * - MotivatedByGoal
      - Someone does A because they want result B; A is a step toward accomplishing the goal B.
      - compete → win
    * - ObstructedBy
      - A is a goal that can be prevented by B; B is an obstacle in the way of A.
      - sleep → noise
    * - Desires
      - A is a conscious entity that typically wants B. Many assertions of this type use the appropriate language's word for "person" as A.
      - person → love
    * - CreatedBy
      - B is a process or agent that creates A.
      - cake → bake
    * - Synonym
      - A and B have very similar meanings. They may be translations of each other in different languages. This is the synonym relation in WordNet as well. Symmetric.
      - sunlight ↔ sunshine
    * - Antonym
      - A and B are opposites in some relevant way, such as being opposite ends of a scale, or fundamentally similar things with a key difference between them. Counterintuitively, two concepts must be quite similar before people consider them antonyms. This is the antonym relation in WordNet as well. Symmetric.
      - black ↔ white; hot ↔ cold
    * - DistinctFrom
      - A and B are distinct member of a set; something that is A is not B. Symmetric.
      - red ↔ blue; August ↔ September
    * - DerivedFrom
      - A is a word or phrase that appears within B and contributes to B's meaning.
      - pocketbook → book
    * - SymbolOf
      - A symbolically represents B.
      - red → fervor
    * - DefinedAs
      - A and B overlap considerably in meaning, and B is a more explanatory version of A.
      - peace → absence of war
    * - MannerOf
      - A is a specific way to do B. Similar to "IsA", but for verbs.
      - auction → sale
    * - LocatedNear
      - A and B are typically found near each other. Symmetric.
      - chair ↔ table
    * - HasContext
      - A is a word used in the context of B, which could be a topic area, technical field, or regional dialect.
      - astern → ship; arvo → Australia
    * - SimilarTo
      - A is similar to B. Symmetric.
      - mixer ↔ food processor
    * - EtymologicallyRelatedTo
      - A and B have a common origin. Symmetric.
      - folkmusiikki ↔ folk music
    * - EtymologicallyDerivedFrom
      - A is derived from B.
      - dejta → date
    * - CausesDesire
      - A makes someone want B.
      - having no food → go to a store
    * - MadeOf
      - A is made of B.
      - bottle → plastic
    * - ReceivesAction
      - B can be done to A.
      - button → push
    * - ExternalURL
      - Instead of relating to ConceptNet nodes, this pseudo-relation points to a URL outside of ConceptNet, where further Linked Data about this term can be found. Similar to RDF's seeAlso relation.
      - knowledge → http://dbpedia.org/page/Knowledge

For a better understanding of how the knowledge base is articulated please refer to `ConceptNet - wiki <https://github.com/commonsense/conceptnet5/wiki>`_.
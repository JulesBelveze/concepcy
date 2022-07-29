Overview
==============

ConcepCy is a SpaCy wrapper of ConceptNet for semantical information.

The library comes with a `ConcepCyComponent` that is in charge of querying the ConceptNet network, retrieve the
information, parse it and extend the `spacy.Token` and `spacy.Doc` objects.

When firstly designing concepCy one of the main concern was the latency of the ConceptNet API calls. Indeed, we need to
make one API call for every word we want to get information for. It turns out that one API call takes approximately 0.5
seconds. So one can easily notice that sequentially sending API calls would lead to pretty long waiting time.

To overcome this problem we made the choice to send all the requests in parallel instead. For this we use the really
neat `request-boost <https://github.com/singhsidhukuldeep/request-boost>`_ library which allows us to retrieve
information in a decent time.
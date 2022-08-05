FAQ
###########

Which languages does concepCy support?
**********

As mentioned in the documentation ConceptNet is a multilingual resource (list of all available languages `here <https://github.com/commonsense/conceptnet5/wiki/Languages>`_).
However, concepCy being a SpaCy pipeline component it depends on a `spacy.Language <https://spacy.io/api/language/#_title>`_ object.
This means that you can use concepCy with any of the languages supported by SpaCy (list available `here <https://spacy.io/usage/models#languages>`_)!

Is there any rate limit?
**********

As you might have noticed concepCy makes requests to the ConceptNet API under the hood, which has rate limitations. Directly quoting their docs:

::

  You can make 3600 requests per hour to the ConceptNet API, with bursts of 120 requests per minute allowed. The /related and /relatedness endpoints count as two requests when you call them.
  This means you should design your usage of the API to average less than 1 request per second.

How do I cite this work?
**********

If you use concepCy in your research, you can cite it using:

.. code-block::

   @software{belveze_concepcy,
      author = {Belveze, Jules},
      title = {concepCy},
      url = {https://github.com/JulesBelveze/concepcy},
      version = {0.1.0}
   }
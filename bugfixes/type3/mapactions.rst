.. index::
  Performance; Expensive map events made faster
  Events; Expensive map events made faster

======================
Inefficient Map Events
======================

Map events `TechType exists` and `TechType does not exist` were implemented
inefficiently. Both iterated all available types each frame to resolve an ID to
a type and then iterated all technos to count the number of existing technos of
this type. :game:`Ares` always caches the type information and also optimizes
summing up the techno count by either using the house counters of each house, if
the type is :tag:`Insignificant=no` and :tag:`DontScore=no` or at least only
checking the list of the relevant object type otherwise.

.. versionadded:: 0.3
.. versionchanged:: 3.0

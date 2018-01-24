.. index::
  Performance; Expensive map events made faster
  Events; Expensive map events made faster

======================
Inefficient Map Events
======================

Map events `TechType exists` and `TechType does not exist` were implemented
inefficiently. Both iterated all available types each frame to resolve an ID to
a type and then iterated all technos to count the number of existing technos of
this type. :game:`Ares` caches the type information. :game:`Ares` also optimizes
summing up the techno count by using the house counters of each house, if the
type is :tag:`Insignificant=no` and :tag:`DontScore=no`.

.. versionadded:: 0.3

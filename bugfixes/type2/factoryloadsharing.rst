.. index:: Factories;  Factory load sharing for factories of the same type rather than just the same ID.

====================
Factory Load Sharing
====================

If you had queued up a lot of vehicles such that the primary factory
could not cope with the rapid exit cycle then the game would search
for alternative exits other instances of the same BuildingType. In
Ares this has been extended to search for all BuildingTypes with the
same ``Factory`` and ``Naval`` settings.

.. note:: This fix currently prevents the so-called 'kennel hack' from working.

.. versionadded:: 0.1
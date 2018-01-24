.. index:: Factories; Factory load sharing for factories of the same type

====================
Factory Load Sharing
====================

If you had queued up a lot of vehicles such that the primary factory could not
cope with the rapid exit cycle then the game would search for alternative exits
-- other instances of the same :type:`BuildingType`. In :game:`Ares` this has
been extended to search for all :type:`BuildingTypes` with the same
:tag:`Factory` and :tag:`Naval` settings.

.. note:: This fix prevents the so-called 'kennel hack' from working. See
  \ :doc:`/new/buildings/factoriesandcloning` for a solution.

.. versionadded:: 0.1

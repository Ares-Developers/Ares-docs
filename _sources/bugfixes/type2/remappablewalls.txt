.. index:: Walls;  Walls remap to the owning player's color.

================
Remappable Walls
================

Walls (i.e. :type:`OverlayTypes` with :tag:`Wall=yes`) always use the same color
in place of the remap for all players, regardless of the owning player's color.
:game:`Ares` will instead draw walls' remappable sections in their respective
owner's colors.

.. versionadded:: 0.2

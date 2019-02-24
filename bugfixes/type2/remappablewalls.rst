.. index::
  Walls; Remap to the owning player's color
  Art; Walls remap to the owning player's color

================
Remappable Walls
================

Walls (i.e. :type:`OverlayTypes` with :tag:`Wall=yes`) were always rendered in
the remap colors of the current player (the human playing on this computer),
instead of using the remap color of the wall's actual owner. :game:`Ares` will
instead draw walls' remappable sections in their respective owner's colors.

.. versionadded:: 0.2

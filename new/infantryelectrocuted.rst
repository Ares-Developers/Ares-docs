.. index::
  Warheads; InfantryElectrocuted animation
  Art; InfantryElectrocuted animation

:captiontag:`InfantryElectrocuted`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The animation displayed for a dying :type:`InfantryType` when the warhead that
killed them had :tag:`InfDeath=5` used to be hard-coded to the second animation
from the :tag:`[Animations]` list. You can now specify
:tag:`[AudioVisual]InfantryElectrocuted=` instead.

:tagdef:`[AudioVisual]InfantryElectrocuted=animation`
  If :tag:`InfantryElectrocuted` is not defined then the game will search for an
  animation named :value:`ELECTRO`, before finally falling back to the second
  animation like before.

.. versionadded:: 0.1

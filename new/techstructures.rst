Tech Structures Return to Neutral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In multiplayer games the neutral tech structures and occupiable structures a
player captured can be made to be returned to the neutral house in case the
owning player is defeated or gives up, instead of destroying them.

Only buildings that initially belonged to a :tag:`MultiplayPassive=yes` house
are eligible to be returned. In single player mode these settings are ignored.

The country the buildings are given back to is their initial owner.

:tagdef:`[General]ReturnStructures=boolean`
  Whether structures will by default return to the civilian side when a player
  is defeated or giving up. Defaults to :value:`no`.

:tagdef:`[General]Returnable=boolean`
  Whether this building type will return to the civilian side when the owning
  player is defeated or giving up. Defaults to :tag:`[General]ReturnStructures`.

.. index:: Tech Structures; Return to neutral when player defeated.

.. versionadded:: 0.6

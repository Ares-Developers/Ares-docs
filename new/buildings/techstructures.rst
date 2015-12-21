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

:tagdef:`[BuildingType]Returnable=boolean`
  Whether this building type will return to the civilian side when the owning
  player is defeated or giving up. Defaults to :tag:`[General]ReturnStructures`.

.. index:: Tech Structures; Return to neutral when player defeated.

.. versionadded:: 0.6


Tech Structure Notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:game:`Yuri's Revenge` has the :tag:`CaptureEvaEvent` setting that defines which
EVA event will play if a building of a type with :tag:`NeedsEngineer=yes` is
captured. :game:`Ares` makes the corresponding lost event customizable and adds
optional text messages for each of them.

:tagdef:`[BuildingType]LostEvaEvent=EVA event`
  The EVA message played when a building of this type is captured from the
  player. Requires :tag:`NeedsEngineer=yes`. Defaults to
  :value:`EVA_TechBuildingLost`.

:tagdef:`[BuildingType]Message.Capture=CSF label`
  The text printed when a building of this type is captured by the player.
  Requires :tag:`NeedsEngineer=yes`. Defaults to :value:`none`.

:tagdef:`[BuildingType]Message.Lost=CSF label`
  The text printed when a building of this type is captured by the enemy.
  Requires :tag:`NeedsEngineer=yes`. Defaults to :value:`none`.

.. index:: Tech Structures; EVA and text notifications when captured and lost.

.. versionadded:: 0.9

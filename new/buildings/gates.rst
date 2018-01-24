.. index::
  Gates; Sounds per building
  Buildings; Gate sounds

Gates
~~~~~

Gates are buildings that are passable for allies but act like a wall for
enemies. Introduced in :game:`Tiberian Sun`, they were not featured prominently
in the later games. They still work, and :game:`Ares` makes some of their
options customizable.

.. note:: Mind the naming scheme from :game:`Tiberian Sun`, which made sense
  when gates lowered into the ground: *down* means **opening**, *up* means
  **closing**.

:tagdef:`[BuildingType]GateDownSound=sound name`
  The sound played when this gate opens. Defaults to :tag:`[AudioVisual]GateDown`.
:tagdef:`[BuildingType]GateUpSound=sound name`
  The sound played when this gate closes. Defaults to :tag:`[AudioVisual]GateUp`.

.. versionadded:: 0.4

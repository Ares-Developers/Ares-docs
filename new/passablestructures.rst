Passable Structures
~~~~~~~~~~~~~~~~~~~

There are two ways to create buildings that units can move over, but both have
side effects: :tag:`LaserFence=yes` makes the building immune to damage and
enforces the electro infantry death in case it has a weapon, while
:tag:`Firestorm.Wall=yes` makes the building part of the Firestorm logic.

In :game:`Firestorm`, :tag:`IsLimpetMine` serves a similar purpose, though it
has other effects like not taking attack orders and being destroyed by EMP.

To create a proper land mine that occupies a cell transparently to moving units
while not having any other effect, :game:`Ares` adds a new tag to overcome these
considerations.

:tagdef:`[BuildingType]IsPassable=boolean`
  Whether the cells the building occupies can still be entered or stood on by
  vehicles and infantry. Defaults to :value:`no`.

.. index:: Structures; Buildings that can be driven upon.

.. versionadded:: 0.7

.. index::
  Bugs; Dock structures and Selling Units
  Changes; Soviet Repair Depot can by default sell units now

===============================
Selling Unit on Dock Structures
===============================

In the vanilla game, the Allied Service Depot could be used to sell units that
were currently docked, while the Soviet Repair Depot could not. This was because
of the different foundation both structures use: If the unit docked at the
building's center like for the 3x3 Service Depot, the unit could be sold, while
it couldn't on the 4x3 Repair Depot.

:game:`Ares` changes the logic to work with a unit's individual dock position on
each building instead. This feature can now be turned on or off per building.
See :doc:`Sell Units </new/sellunit>` on how to customize selling units.

.. versionadded:: 3.0

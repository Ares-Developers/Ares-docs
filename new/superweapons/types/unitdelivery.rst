:captiontag:`Type=UnitDelivery`
```````````````````````````````

The Unit Delivery super weapon will create the specified unit(s) in the target
cell. This uses the CellSpread model to place the units.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Deferment=integer - frames`
  Delay before the units are placed. Defaults to :value:`20`.
:tagdef:`[SuperWeapon]SW.ActivationSound=Sound`
  Played when the units are placed. Defaults to :value:`none`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`ParaDrop`.


Unit Delivery specific tags:

:tagdef:`[SuperWeapon]Deliver.Types=list of TechnoTypes`
  The list of units that will be delivered. This works for infantry, vehicles,
  aircraft and buildings.
:tagdef:`[SuperWeapon]Deliver.Buildups=boolean`
  Whether or not buildings delivered by this super weapon should play their
  buildup animation prior to becoming available. Defaults to :value:`no`.


All objects are placed on the ground, including aircraft. Flying units that
never land (e.g. the Rocketeer and Kirovs) will take off. If a cell is occupied,
the super weapon will retry on the next cell and so on, until the object gets
placed. Once the first unit is placed, this process starts again for the next
item in the list. Infantry squads are grouped in a single cell. The search will
skip an item if it has not been placed after testing 100 cells.

You can mix in naval units and they will be placed where they can normally
exist.

If you have more than one building, the resulting placement might look
odd.

The actual delivery of the units happens all at once, after firing the super
weapon and awaiting its deferment.

.. index:: Super Weapons; New super weapon type: UnitDelivery (create unit(s) at
  target cell).

.. versionadded:: 0.1
.. versionchanged:: 0.4

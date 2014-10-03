:captiontag:`Type=UnitDelivery`
```````````````````````````````

The Unit Delivery super weapon will create the specified unit(s) in the target
area.

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
:tagdef:`[SuperWeapon]Deliver.Owner=enum invoker|neutral|special|civilian`
  The country the delivered units will belong to. :value:`invoker` is the player
  who fired the super weapon, :value:`civilian` is the first country of the side
  named :value:`Civilian`, :value:`special` is the country named
  :value:`Special` and :value:`neutral` is the country named :value:`Neutral`.
  Defaults to :value:`invoker`.


The delivery of the units happens all at once, after firing the super weapon and
awaiting its deferment.

The super weapon will try to find a location close to the target area for each
object. This process depends on many factors and also involves randomness, thus
the placement order is not fixed. Do not rely on a specific order.

All objects are placed on the ground, including aircraft. Flying units that
never land (e.g. the Rocketeer and Kirovs) will take off. Infantry squads are
grouped in a single cell.

Units owned by AI are set to go on a hunt mission, buildings and human owned
units are put on a guard mission.

You can mix in naval units and they will be placed where they can normally
exist.


.. index:: Super Weapons; New super weapon type: UnitDelivery (create unit(s) at
  target location).

.. versionadded:: 0.1
.. versionchanged:: 0.8

:captiontag:`Type=GenericWarhead`
`````````````````````````````````

The Generic Warhead super weapon will detonate the specified warhead at the
target cell.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Damage=integer`
  The amount of damage that will be dealt by the warhead.
:tagdef:`[SuperWeapon]SW.Warhead=warhead`
  The warhead that will be detonated when in the target cell when the super
  weapon is fired. Note the warhead is detonated in a cell, not on a unit, so
  chances are you will want to set a :tag:`CellSpread` on the warhead to make
  sure the desired targets (especially :type:`InfantryTypes`) are affected.
:tagdef:`[SuperWeapon]SW.AITargeting=enumeration`
  Defaults to :value:`Offensive`.

Don't forget that the :type:`BuildingType` will need :tag:`DamageSelf=yes` set
(just like the Soviet Nuclear Missile Silo) if you want the warhead to be
capable of damaging the firing building.

.. index:: Super Weapons; New super weapon type: GenericWarhead (detonate any
  warhead at target cell).

.. versionadded:: 0.1

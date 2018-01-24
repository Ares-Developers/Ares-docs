.. index:: Warheads; Suppress death weapons

Suppress Death Weapons
``````````````````````

With these tags certain warheads can be made to not trigger death weapons of
units specified by a list of types, or to generally not trigger death weapons
for infantry or vehicle units. All tags only apply if the warhead kills a unit,
not when the unit is merely damaged and later killed by some other warhead.

:tagdef:`[Warhead]DeathWeapon.Suppress=list of TechnoTypes`
  When this warhead causes the death of a unit from this list, its death weapon
  will not fire.

:tagdef:`[Warhead]DeathWeapon.SuppressVehicles=boolean`
  Whether death weapons of all :type:`VehicleTypes` are suppressed when this
  warhead kills. If :value:`no`, :tag:`DeathWeapon.Suppress` is still checked.
  Defaults to :value:`no`.

:tagdef:`[Warhead]DeathWeapon.SuppressInfantry=boolean`
  Whether death weapons of all :type:`InfantryTypes` are suppressed when this
  warhead kills. If :value:`no`, :tag:`DeathWeapon.Suppress` is still checked.
  Defaults to :value:`no`.

.. versionadded:: 0.A

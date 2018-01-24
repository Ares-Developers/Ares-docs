.. index::
  Kill Driver; Neutralize vehicles
  Warheads; Kill the driver of a vehicle
  Universe; Kill drivers like Jarmen Kell or neutron rounds

Killing Drivers
~~~~~~~~~~~~~~~

Requested as a `"Jarmen Kell" functionality
<http://bugs.renegadeprojects.com/view.php?id=733>`_, this feature allows
specific warheads to kill the driver of a vehicle instead of damaging
it, and allows others to take over the now-neutral vehicle.

.. versionadded:: 0.2

.. versionchanged:: 0.E


Warhead Settings
----------------

This logic supports :tag:`CellSpread` and respects all immunities as any other
conventional warhead like :tag:`ImmuneToPoison` as well as their veteran
abilities, :tag:`AffectsAllies`, and :tag:`AffectsEnemies`.

:tagdef:`[Warhead]KillDriver=boolean`
  Specifies whether this warhead kills the driver of the vehicle, instead of
  damaging the vehicle itself. The first passenger matching the vehicle's
  :tag:`Operator` is considered the driver. All other passengers will be
  ejected. Defaults to :value:`no`.
:tagdef:`[Warhead]KillDriver.Owner=enumeration - civilian,special,neutral`
  Specifies the house the units are assigned to. Defaults to :value:`special`.
:tagdef:`[Warhead]KillDriver.KillBelowPercent=float`
  Specifies the percentage of health a unit cannot exceed to have its driver
  killed by a :tag:`KillDriver=yes` warhead. A unit above this health level
  is only damaged and the driver is not killed. Defaults to :value:`100%`.
:tagdef:`[Warhead]KillDriver.Chance=float - percentage`
  Specifies the chance that a unit hit by a :tag:`KillDriver=yes` warhead will
  have its driver killed. Defaults to :value:`100%`.


.. _killingdrivers-immunity:

.. index::
  Kill Driver; Protect drivers of vehicles
  TechnoTypes; Driver can't be killed

Protected Drivers
-----------------

The following settings can make a unit immune to the Kill Driver logic:

:tagdef:`[TechnoType]ProtectedDriver=boolean`
  Whether the driver of this vehicle cannot be killed, i.e. whether this vehicle
  is immune to :tag:`KillDriver`. :tag:`Organic=yes` and :tag:`Natural=yes`
  units are always immune to :tag:`KillDriver`. Defaults to :value:`no`.
:tagdef:`[TechnoType]ProtectedDriver.MinHealth=double - percentage`
  The minimum health below which the driver of this unit can be killed. If the
  unit's health is above this, the driver cannot be killed. If
  :tag:`KillDriver.KillBelowPercent` is also defined on the warhead, the
  minimum of the two values is used, that is, this tag can make a unit more
  resistant against driver killing weapons. Defaults to :value:`0.0` if
  :tag:`ProtectedDriver=yes`, to :value:`1.0` otherwise.

Driver protection can also be granted by specifying :value:`PROTECTED_DRIVER`
under :tag:`VeteranAbilities` or :tag:`EliteAbilities`. If specified, the unit's
driver becomes protected unconditionally against :tag:`KillDriver` (which means
that :tag:`ProtectedDriver.MinHealth` is no longer checked), but not against
damage or other special warhead effects.


.. index::
  Kill Driver; Reclaim vehicles
  Infantry; Capture units that had their drivers killed

Reclaim Vehicles
----------------

Drivers are infantry units that can capture neutral vehicles, like ones that had
their driver killed.

:tagdef:`[TechnoType]CanDrive=boolean`
  Whether this :type:`InfantryType` can act as the driver of vehicles whose
  driver has been killed, effectively reclaiming the vehicle. If the vehicle
  requires an :tag:`Operator` the infantry driver turns the unit and enters as
  passenger that can be ejected later, otherwise the driver is swallowed,
  becoming the permanent driver of the vehicle. Defaults to :value:`no`.

:tagdef:`[Country]CanBeDriven=boolean`
  Whether units owned by this country can be captured by :tag:`CanDrive=yes`
  infantry. This can be used to place units owned by neutral countries on the
  map without them being capturable. Defaults to :tag:`MultiplayPassive`.

.. note:: Vehicle Thieves cannot drive neutralized vehicles by default, but
  \ :tag:`VehicleThief=yes` can be combined with :tag:`CanDrive=yes` without
  problems.

See :doc:`/new/hijackers` for more options that relate to :tag:`CanDrive`.

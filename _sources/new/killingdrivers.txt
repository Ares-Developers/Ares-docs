Killing Drivers
~~~~~~~~~~~~~~~

Requested as a `"Jarmen Kell" functionality
<http://bugs.renegadeprojects.com/view.php?id=733>`_, this feature allows
specific warheads to kill the driver of a vehicle instead of damaging
it, and allows others to take over the now-neutral vehicle.

:tagdef:`[Warhead]KillDriver=boolean`
  Specifies whether this warhead kills the driver of the vehicle, instead of
  damaging the vehicle itself. The first passenger matching the vehicle's
  :tag:`Operator` is considered the driver. All other passengers will be
  ejected. Defaults to :value:`no`.
:tagdef:`[TechnoType]ProtectedDriver=boolean`
  Whether the driver of this vehicle cannot be killed, i.e. whether this vehicle
  is immune to :tag:`KillDriver`. :tag:`Organic=yes` and :tag:`Natural=yes`
  units are always immune to :tag:`KillDriver`. Defaults to :value:`no`.
:tagdef:`[TechnoType]CanDrive=boolean`
  Whether this :type:`InfantryType` can act as the driver of vehicles whose
  driver has been killed, effectively reclaiming the vehicle. If the vehicle
  requires an :tag:`Operator` the infantry driver turns the unit and enters as
  passenger that can be ejected later, otherwise the driver is swallowed,
  becoming the permanent driver of the vehicle. Defaults to :value:`no`.

.. note:: Vehicle Thieves cannot drive neutralized vehicles by default, but
  \ :tag:`VehicleThief=yes` can be combined with :tag:`CanDrive=yes` without
  problems.

See :doc:`/new/hijackers` for more options that relate to :tag:`CanDrive`.

.. index:: Warheads; Warheads can be set to kill the driver of a vehicle, instead of damaging it.

.. versionadded:: 0.2

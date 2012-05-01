Killing Drivers
~~~~~~~~~~~~~~~

Requested as a `"Jarmen Kell" functionality
<http://bugs.renegadeprojects.com/view.php?id=733>`_, this feature allows
specific warheads to kill the driver of a vehicle instead of damaging
it, and allows others to take over the now-neutral vehicle.

:tagdef:`[Warhead]KillDriver=boolean`
  Specifies whether this warhead kills the driver of the vehicle, instead of
  damaging the vehicle itself.
:tagdef:`[TechnoType]ProtectedDriver=boolean`
  Whether the driver of this vehicle cannot be killed, i.e. whether this vehicle
  is immune to :tag:`KillDriver`.
:tagdef:`[TechnoType]CanDrive=boolean`
  Whether this :type:`InfantryType` can act as the driver of vehicles whose
  driver has been killed.


NB: As of the time of this writing, the relationship between
`Operator=` and `KillDriver=` is not fully implemented; ideally,
`KillDriver` will kill all passengers in case of `_ANY_`, and only the
specific operator passengers when specific operators are required,
ejecting unharmed passengers in all cases.
At the moment, `KillDriver=` simply kills all passengers if an
`Operator=` case is encountered.

In addition, drivers entering a neutral vehicle need different
handling depending on whether they enter a neutral vehicle as part of
the Operator logic or as a "generic" driver - generic drivers should
vanish, becoming the permanent driver of the vehicle, whereas
operators should turn the unit and enter as a passenger, allowing
operator-switches as with all other units.

NB: As of the time of this writing, no reclaiming mechanism has been
implemented. You will need a ``VehicleThief``_ to acquire a neutral
vehicle.

.. index:: Warheads; Warheads can be set to kill the driver of a vehicle, instead of damaging it.

.. versionadded:: 0.2

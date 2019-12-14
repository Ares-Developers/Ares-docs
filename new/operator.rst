.. index::
  Operators; Vehicles and buildings need an operator (driver) before they will function
  Buildings; Require an operator before it will function
  Vehicles; Require a driver before it will function

Operator
~~~~~~~~

:type:`BuildingType`\ s and :type:`VehicleType`\ s can now require specific
:type:`InfantryType`\ s or :type:`VehicleType`\ s to be among its passengers
before they will function.

:tagdef:`[TechnoType]Operator=list of TechnoTypes or "_ANY_"`
  Specifies a list of :type:`InfantryType`\ s and :type:`VehicleType`\ s of
  which at least one unit must be among the passengers before this object will
  function. If ":value:`_ANY_`" (sans quotes) is specified, then it does not
  matter which passenger is inside, as long as any is. Use :value:`none` to
  remove the requirement of having an operator. Defaults to :value:`none`.

On the :type:`TechnoType` you will need to set :tag:`Passengers=1` (or higher)
and :tag:`SizeLimit=1` (or higher).

For :type:`BuildingTypes` you will also need to set :tag:`InfantryAbsorb=yes` or
:tag:`UnitAbsorb=yes`.

If the needed passenger is not inside then the :type:`TechnoType` will power
down in a similar fashion to the Robot Tank when the Robot Control Centre is
offline -- the unit will not be able to move or fire.

:type:`BuildingType`\ s without their Operator will not be able to fire their
weapon, if they have one.

No other building-specific functions will be affected (e.g. providing power,
being a factory, undeploying, super weapons, radar, etc).

Units and structures will not cloak themselves if they are not operated, but
they can still be cloaked by Cloak Generators. Mirage Tanks without their
Operator will still maintain their disguise.


+ Operator logic has no effect on Service Depots -- the Operator cannot enter.
+ Operator logic has no effect on deployed Siege Choppers. An Operator is never
  needed.
+ Operator logic will render Refineries unusable because the Operator will not
  be able to enter and the Harvester will not dock.
+ Operator logic will render :type:`InfantryTypes` unusable because
  :type:`InfantryTypes` cannot have passengers.
+ Operator logic cannot be used on vehicles that deploy into buildings
  (e.g. MCVs) because the passenger deploy function takes precedence
  over :tag:`DeploysInto=`.
+ Operator logic will render :type:`VehicleTypes` with :tag:`BalloonHover=yes`
  unusable because they will power down in mid-air without landing, so it is
  impossible to get an Operator into them (even flying infantry like the
  Rocketeer cannot enter them).
+ Operator logic cannot be used on :type:`AircraftTypes` for two reasons:

    #. Aircraft are produced in a place where the Operator cannot board them.
       You can issue a move order to an Operator-less aircraft but they will
       immediately crash.
    #. Assuming you manage to get an aircraft to a place where the Operator can
       board it, if the aircraft can attack then the act of attacking will cause
       the passengers (including the Operator) to parachute from the aircraft -
       whereupon it will crash.

.. note:: The AI behaves unpredictably when faced with units that require
  Operators and may not be subject to certain effects. You should prevent the
  AI from building anything that requires an Operator.

.. versionadded:: 0.1
.. versionchanged:: 3.0

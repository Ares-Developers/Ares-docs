Operator
~~~~~~~~

Any :type:`TechnoType` can now require a specific :type:`InfantryType` to be
among its passengers before it will function.

:tagdef:`[TechnoType]Operator=string, either an InfantryType or "_ANY_"`
  Specifies the :type:`InfantryType` that must be among the :type:`TechnoType`'s
  passengers before the :type:`TechnoType` will function. If ":value:`_ANY_`"
  (sans quotes) is specified then it doesn't matter which :type:`InfantryType`
  is inside as long as some :type:`InfantryType` is.


On the :type:`TechnoType` you will need to set :tag:`Passengers=1` (or higher)
and :tag:`SizeLimit=1` (or higher).

For :type:`BuildingTypes` you will also need to set :tag:`InfantryAbsorb=yes`.

If the needed passenger is not inside then the :tag:`TechnoType` will power down
in a similar fashion to the Robot Tank when the Robot Control Centre is offline
the unit will not be able to move or fire.

:type:`BuildingTypes` without their Operator will not be able to fire their
weapon, if they have one.

No other building-specific functions will be affected (e.g. providing power,
being a factory, undeploying, super weapons, radar, etc).

Mirage Tanks without their Operator will still maintain their disguise.


+ Operator logic has no effect on Service Depots the Operator cannot
  enter.
+ Operator logic has no effect on deployed Siege Choppers. An Operator is never
  needed.
+ Operator logic will render Refineries unusable because the Operator will not
  be able to enter and the Harvester will not dock.
+ Operator logic will render :type:`InfantryTypes` unusable because
  :type:`InfantryTypes` cannot have passengers.
+ Operator logic cannot be used on vehicles that deploy into buildings
  (e.g. MCVs) because the passenger deploy function takes precedence
  over :tag:`DeploysInto=`.
+ Operator logic will render :type:`VehicleTypes` with :tag:`BallonHover=yes`
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

.. note:: The AI behaves unpredicatably when faced with units that require
  Operators and may not be subject to certain effects. You should prevent the
  AI from building anything that requires an Operator.

.. index:: Operators; Vehicles and buildings can be made to require an operator (driver)
  before they will function.

.. versionadded:: 0.1

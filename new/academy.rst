Academies
~~~~~~~~~

Academies are buildings that grant their owners the right to train specified
units and structures with a certain promotion level. If a player owns more than
one academy buildings, the highest bonus is awarded. The effect does not stack.

Only :tag:`Trainable=yes` units or structures can get a veterancy bonus. If an
object has been promoted to a higher level by other means already (like from
:tag:`VeteranInfantry`, or by infiltrating an enemy War Factory), the veterancy
level is not reduced.

A value of :value:`1.0` means veteran, a value of :value:`2.0` means elite. You
can use decimal values to grant only partial levels, so the next promotion will
come earlier.

:tagdef:`[BuildingType]Academy.InfantryVeterancy=double - veterancy levels`
  The veterancy bonus to grant to any :type:`InfantryType` or any
  :tag:`Organic=yes` :type:`VehicleType` if a player owns one of these
  buildings. Defaults to :value:`0.0`.

:tagdef:`[BuildingType]Academy.AircraftVeterancy=double - veterancy levels`
  The veterancy bonus to grant to any :type:`AircraftType` or any
  :tag:`ConsideredAircraft=yes` :type:`VehicleType` if a player owns one of
  these buildings. Defaults to :value:`0.0`.

:tagdef:`[BuildingType]Academy.VehicleVeterancy=double - veterancy levels`
  The veterancy bonus to grant to any :type:`VehicleType` with :tag:`Organic=no`
  and :tag:`ConsideredAircraft=no` if a player owns one of these buildings.
  Defaults to :value:`0.0`.

:tagdef:`[BuildingType]Academy.BuildingVeterancy=double - veterancy levels`
  The veterancy bonus to grant to any :type:`BuildingType` if a player owns one
  of these buildings. Defaults to :value:`0.0`.

Each academy can be made to promote only specific types or to not promote all
but the specified types. By default, academies promote all types.

:tagdef:`[BuildingType]Academy.Types=list of TechnoTypes`
  The only types that are affected by this academy to get the defined bonuses.
  If the list is empty, all types are affected. Defaults to :value:`none`.

:tagdef:`[BuildingType]Academy.Ignore=list of TechnoTypes`
  The types that will never be affected by this academy. Defaults to
  :value:`none`.

.. index:: Tech Structures; Academies promote units when built

.. versionadded:: 0.8

Chrono Prisons
~~~~~~~~~~~~~~

Originally intended for *Yuri's Revenge*, with published concept art
and even appearing on the original version of the box art, the Chrono
Prison was planned as a unit which would suck units into a
"containment sphere" in its turret; the turret would grow with each
unit sucked in, and if the prison were destroyed, the units would be
free again.
Ares includes functionality which can be used to create such a unit,
but the implementation is liberal enough to use the parts for a
variety of other units. (Original requests: `#680`_ and `#1208`_,
`original concept art on RADEN`_) Chrono Prisons.

:[Weapon]Abductor=(boolean): If set to yes, weapons with this flag
  will absorb the target into the attacker's passenger hold. Should the
  attacking unit be destroyed, its passengers will emerge. NB: Please
  make sure you have a passenger hold when using this. Also remember
  that `SizeLimit` defaults to 0, so if you don't set it, abduction of
  most units will be denied. As usual, `PipScale` is required for all
  transports. NB: Due to the way `Passengers` for buildings was tacked
  on, it is possible buildings with abducting weapons will not work
  properly. (Using `InfantryAbsorb`/ `UnitAbsorb` increases your
  chances.) These malfunctions are considered out of the scope of the
  request and will not be considered bugs. The same goes for
  InfantryTypes. Malfunctions on VehicleTypes and AircraftTypes, on the
  other hand, should be reported immediately. Abductor=
:[TechnoType]PassengerTurret=(boolean): If set to yes, this unit's
turret will switch to the turret with the index equivalent to the
number of passengers it holds.

    + 0 passengers footur.vxl
    + 1 passenger footur1.vxl
    + 5 passengers footur5.vxl
NB: In order to use this, you have to use YR's multi-turret logic,
  that is, you have to specify `Turret=yes`, an appropriate
  `TurretCount`, and you have to use the `WeaponX` flags to specify
  weapons. PassengerTurret=


.. versionadded:: 0.2

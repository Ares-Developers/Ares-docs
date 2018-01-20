Survivors
~~~~~~~~~

In the original :game:`Red Alert`, pilots would parachute from destroyed
aircraft. :game:`Ares` reintroduces this feature along with some additional
improvements, all of which are customizable.

:type:`AircraftTypes` and :type:`VehicleTypes` have the option of spawning a
pilot (or driver) when they are destroyed. In order for a pilot to be spawned
from an airborne unit, the ground beneath the destroyed unit must be clear.

The following flags control the percent chance of a survivor being spawned, and
the type of unit that that survivor will be.


Units and Buildings
```````````````````

:tagdef:`[TechnoType]Survivor.Side#=InfantryType) (where # is the zero-based index of the side -- e.g. 0 for Allied, 1 for Soviet, 2 for Yuri`
  The :type:`InfantryType` that can emerge from this object as a survivor when
  the object was owned by the corresponding side. Use to :value:`<none>` to
  reset to default. Defaults to the owning side's :tag:`Crew`. 

  .. quickstart:: For example, :tag:`Survivor.Side0=E1` would cause the spawned
    survivor (if any) to be a GI when the destroyed unit was owned by an Allied
    player at the time of destruction.

:tagdef:`[TechnoType]Crew.TechnicianChance=integer - percent between 0 and 100`
  The chance the owning side's :tag:`Technician` is spawned instead of an
  ordinary crew member. Defaults to :value:`15` for :type:`BuildingTypes` with
  :tag:`Primary=` set, to :value:`0` otherwise.
  
  .. note:: \ :game:`Yuri's Revenge` also ejects :tag:`Technician` from units
    with :tag:`Primary=` set. Previous versions of :game:`Ares` did not, so the
    default value has been changed so there is no difference to previous
    versions. If you want to eject :tag:`Technician` from units, you have to
    manually set :tag:`Crew.TechnicianChance`.


Unit-specific
`````````````

:tagdef:`[Unit]Survivor.Pilots=integer`
  The number of pilots that will attempt to be spawned when this unit is
  destroyed (provided that the ground beneath the destroyed unit is clear).
  Defaults to :value:`1` if the unit has :tag:`Crewed=yes` set, to :value:`0`
  otherwise.

:tagdef:`[Unit]Survivor.RookiePilotChance=integer between 0 and 100`

:tagdef:`[Unit]Survivor.VeteranPilotChance=integer between 0 and 100`

:tagdef:`[Unit]Survivor.ElitePilotChance=integer between 0 and 100`
  The percent chance that each individual pilot will be spawned when this unit
  is destroyed. If this value is negative, :tag:`[General]CrewEscape` will be
  used. Defaults to :value:`-1`.

:tagdef:`[Unit]Survivor.RookiePassengerChance=integer between 0 and 100`

:tagdef:`[Unit]Survivor.VeteranPassengerChance=integer between 0 and 100`

:tagdef:`[Unit]Survivor.ElitePassengerChance=integer between 0 and 100`
  Determines the percent chance that each of the unit's passengers (if any) will
  survive. Rookie/Veteran/Elite refer to the veteran level of the transport unit
  -- a unit with a higher veteran level could be made to have a greater (or
  lesser) chance of allowing its passengers to survive. Passengers will be
  spawned in the cells around the destroyed unit and, so, if these cells are not
  clear then the passengers will not be spawned.

  These flags default to a special-case value of :value:`-1` which means "use
  the original game logic" (i.e. land-based vehicles such as the Battle Fortress
  will eject their passengers but jumpjet vehicles such as the Nighthawk will
  not). Note that, for airborne vehicles such as the Nighthawk, there is no way
  to say "passengers can survive on the ground, but aren't allowed to paradrop
  from the air" -- if they can survive they can survive.

If either the pilots or any passengers are 'killed' because they were not
spawned (i.e. because the ground was not clear or the random chance did not
luck in) then they count as having been killed by the unit that killed the
transport. If :tag:`Survivor.PilotChance=0` then the pilots will not count as
having been killed (however, passengers will always count as having been killed,
even if :tag:`Survivor.PassengerChance=0`).

Spawned pilots will be spawned with 50% of their maximum health and the same
amount of experience as the destroyed unit had. Passengers will emerge with both
their health and their experience unchanged.

.. index:: Percent chance for pilots and/or passengers to emerge/parachute from destroyed vehicles/aircraft.

.. versionadded:: 0.1


Building-specific
`````````````````

Buildings can spawn the owning side's :tag:`Engineers` in addition to
:tag:`Crew` and :tag:`Technician`. The number of crew members is determined by
the refund price of the building divided by the side's :tag:`SurvivorDivisor`.
If the building has been captured, the divisor is double, and thus the number of
survivors is halved. At least one survivor is spawned, but no more than five.

:tagdef:`[BuildingType]Crew.EngineerChance=integer - percent between 0 and 100`
  The chance the owning side's :tag:`Engineer` is spawned instead of an ordinary
  crew member. If the building has been captured, engineers are not allowed to
  be spawned regardless of this setting. Defaults to :value:`25` if
  :tag:`Factory=BuildingType`, to :value:`0` otherwise.

.. index:: Crew; Customizable buiding crew.
.. index:: Crew; Engineer spawn chance for buildings.

.. versionadded:: 0.5

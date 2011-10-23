EMP
~~~

Vehicles affected by EMP (Electromagnetic Pulse) are paralyzed in a
similar manner to a Chrono Legionnaire erasing a unit. Unlike the
Chrono Legionnaire however, EMP'd vehicles can still be attacked by
other units.
EMP paralysis affects units and buildings in various ways (given they
are not immune to EMP, see below): EMP weapons


+ Primary effect: units will not respond to any commands. They will
  stop moving and will not attack anything.
+ Hovering units (such as the Robot Tank) will land.
+ Units display the animation specified by
  `[General]EMPulseSparkles=EMP_FX01`. Note that the emp_fx01.shp file
  that comes with Red Alert 2 is in the Tiberian Sun palette and needs
  to be converted.
+ Voxel-based units are darkened (SHP-based units are not).
+ Buildings that can undeploy into vehicles (e.g. MCVs) still can, but
  the resulting vehicle will remain EMP'd until the effect wears off.
+ Aircraft will immediately crash.
+ Power plants cease to produce power.
+ Factories will stop working.
+ Base defenses will not be able to fire their weapon.
+ Gap Generators will stop emitting radar gap.
+ Laser Fence Posts will stop emitting laser fences.
+ Robot Control Centers will stop working.
+ Super weapon buildings will shut down and the super weapons
  themselves will stop charging, if they have
  `[SuperWeapon]IsPowered=yes` set.
+ Radar buildings will stop providing radar.
+ SpySat buildings will stop to reveal the map.
+ Units that spawn other units will cease to do so. If the spawner
  unit has launched any aircraft then the aircraft will immediately
  crash.
+ Slave Miner slaves will stop working.
+ Units that are in their unloading state (such as ore harvesters
  depositing ore or Siege Choppers transforming) will only become EMP'd
  once they have finished unloading.
+ Harvesters that were in the middle of harvesting when hit by EMP
  will resume harvesting after EMP wears off.


Quickstart: If you want a warhead to EMP a target for ten seconds, set
EMP.Duration=150 on the warhead.

NB: Tiberian Sun used the weapon's Damage flag to determine how long
the EMP effect would last. Ares, however, uses 2 new flags
(EMP.Duration and EMP.Cap) to provide greater control. The weapon's
Damage will be delivered independently from EMP paralysis (so a weapon
can both damage and paralyze its target). Tiberian Sun also used the
flag EMEffect=yes, which is not used in Ares.

:[Warhead]EMP.Duration= (integer frames) [Warhead]EMP.Cap= (integer
  frames): The above two flags are used together to determine how long
  (in frames) the affected units will be EMP'd for. EMP.Duration=
  EMP.Cap=


The game keeps track of how much longer each unit will remain
paralyzed. Each unit essentially has a hidden EMP counter that counts
down frame by frame until it reaches zero, at which point the unit
will be re-activated. This counter is what gets modified by EMP
warheads.

A unit does not get affected by EMP if `Verses` is equal to `0%`,
otherwise the target is endowed with the full effect.

First we will look at positive EMP.Duration the targets are going to
be paralyzed.


+ `EMP.Cap` is greater than zero. Makes this EMP effect stackable, but
  capped. The target's EMP counter is increased by `EMP.Duration` up to
  but not exceeding `EMP.Cap`. If the target's EMP counter is already
  greater than `EMP.Cap` (e.g. caused by some other EMP weapon) then it
  will not be reduced. Examples: EMP counter is 0, `EMP.Duration=10`,
  `EMP.Cap=20`. Result: EMP counter will be set to 10. EMP counter is
  15, `EMP.Duration=10`, `EMP.Cap=20`. Result: EMP counter will be set
  to 20. EMP counter is 60, `EMP.Duration=10`, `EMP.Cap=20`. EMP counter
  will remain at 60.
+ `EMP.Cap=0` Makes this EMP effect stackable, but uncapped. The
  target's EMP counter is incremented by `EMP.Duration`, without limit.
  This is Ares legacy behavior (before the `EMP.Cap` flag was added).
  Example: EMP counter is 25, `EMP.Duration=10`. Result: EMP counter
  will be set to 35.
+ `EMP.Cap=-1` The target's EMP counter is set to the exact number of
  frames specified by `EMP.Duration`, unless the target's EMP counter is
  already greater than this. Examples: EMP counter is 5,
  `EMP.Duration=10`. Result: EMP counter will be set to 10. EMP counter
  is 20, `EMP.Duration=10`. EMP counter will remain at 20.


Next we will look at negative `EMP.Duration` for example, a friendly
unit trying to re-activate the already-paralyzed unit.


+ `EMP.Cap=-1` The target's EMP counter is reduced by the number of
  frames specified by `EMP.Duration`. Examples: EMP counter is 50,
  `EMP.Duration=10`. Result: EMP counter will be set to 40. EMP counter
  is 7, `EMP.Duration=10`. Result: EMP counter will be set to zero and
  the unit will re-activate.
+ `EMP.Cap` is greater than zero. The target's EMP counter is reduced
  by the number of frames specified by `EMP.Duration`. If this value is
  still greater than `EMP.Cap` then the EMP counter is reduced further
  so that it is equal to `EMP.Cap`. Examples: EMP counter is 50,
  `EMP.Duration=10`, `EMP.Cap=70`. Result: EMP counter will be set to
  40. EMP counter is 50, `EMP.Duration=10`, `EMP.Cap=20`. Result: EMP
  counter will be set to 20. EMP counter is 7, `EMP.Duration=10`.
  Result: EMP counter will be set to zero and the unit will re-activate.
+ `EMP.Cap=0` `EMP.Duration` is irrelevant. The EMP counter will be
  set to zero and the unit will re-activate.


Quickstart: If you want a unit to be immune to EMP, set
ImmuneToEMP=yes on the unit.

:[TechnoType]ImmuneToEMP= (boolean): The above flag specifies whether
or not the TechnoType is immune to the effects of EMP. The default
immunity status is determined based on the following rules:

    + BuildingTypes: `ImmuneToEMP` defaults to no for BuildingTypes that
      have `Powered=yes` and a negative `Power=` value set. `ImmuneToEMP`
      defaults to no for BuildingTypes that provide one or more of the
      following special functions:

        + Radar
        + Super weapons
        + Undeploy into a vehicle (e.g. Construction Yards)
        + Powers vehicles (e.g. Robot Control Centre)
        + Gap Generator
        + Sensors
        + Laser Fence Posts
      `ImmuneToEMP` defaults to yes for all other BuildingTypes. For
      instance, power plants and pillboxes are immune to EMP by default, as
      well as SpySat buildings and factories.
    + InfantryTypes: `ImmuneToEMP` defaults to yes for InfantryTypes
      unless `Cyborg=yes` is set (in which case, `ImmuneToEMP` defaults to
      no).
    + VehicleTypes and AircraftTypes: `ImmuneToEMP` defaults to no for
      VehicleTypes and AircraftTypes unless `Organic=yes` is set (in which
      case, `ImmuneToEMP` defaults to yes).
Manually setting `ImmuneToEMP` always overrides the default. EMP
  immunity can also be granted via the new veteran/elite ability
  "EMPIMMUNE". Just set `VeteranAbilities=EMPIMMUNE` or
  `EliteAbilities=EMPIMMUNE` on the TechnoType. EMP immunity also
  respects `TypeImmune`, `AffectsAllies` and `AffectsEnemies` on the
  warhead. ImmuneToEMP=
:[TechnoType]EMP.Modifier= (multiplier): If the EMP effect duration is
  positive it will be multiplied by this factor. You can create units
  that are more or less prone to the Electromagnetic Pulse.
  `EMP.Modifier` defaults to `100%`. EMP.Modifier=


See Destroy Units by EMP to learn how to crash flying TechnoTypes.

.. versionadded:: 0.1



<<<SEPARATOR>>>

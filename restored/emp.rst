EMP
~~~

Vehicles affected by EMP (Electromagnetic Pulse) are paralyzed in a similar
manner to a Chrono Legionnaire erasing a unit. Unlike the Chrono Legionnaire
however, EMP'd vehicles can still be attacked by other units.

EMP paralysis affects units and buildings in various ways (given they are not
immune to EMP, see below):


+ Primary effect: units will not respond to any commands. They will stop moving
  and will not attack anything.
+ Hovering units (such as the Robot Tank) will land.
+ Units display the animation specified by
  :tag:`[General]EMPulseSparkles=EMP_FX01`. Note that the :file:`emp_fx01.shp`
  file that comes with :game:`Red Alert 2` is in the :game:`Tiberian Sun`
  palette and needs to be converted.
+ Voxel-based units are darkened (SHP-based units are not).
+ Buildings that can undeploy into vehicles (e.g. MCVs) still can, but the
  resulting vehicle will remain EMP'd until the effect wears off.
+ Aircraft will immediately crash.
+ Power plants cease to produce power.
+ Factories will stop working.
+ Base defenses will not be able to fire their weapon.
+ Gap Generators will stop emitting radar gap.
+ Laser Fence Posts will stop emitting laser fences.
+ Robot Control Centers will stop working.
+ Super weapon buildings will shut down and the super weapons themselves will
  stop charging, if they have :tag:`[SuperWeapon]IsPowered=yes` set.
+ Radar buildings will stop providing radar.
+ SpySat buildings will stop to reveal the map.
+ Units that spawn other units will cease to do so. If the spawner unit has
  launched any aircraft then the aircraft will immediately crash.
+ Slave Miner slaves will stop working.
+ Units that are in their unloading state (such as ore harvesters depositing ore
  or Siege Choppers transforming) will only become EMP'd once they have finished
  unloading.
+ Harvesters that were in the middle of harvesting when hit by EMP will resume
  harvesting after EMP wears off.


.. quickstart:: If you want a warhead to EMP a target for ten seconds, set
    \ :tag:`EMP.Duration=150` on the warhead.

.. note:: \ :game:`Tiberian Sun` used the weapon's :tag:`Damage` flag to
  determine how long the EMP effect would last. :game:`Ares`, however, uses 2
  new flags (:tag:`EMP.Duration` and :tag:`EMP.Cap`) to provide greater control.
  The weapon's :tag:`Damage` will be delivered independently from EMP paralysis
  (so a weapon can both damage and paralyze its target). :game:`Tiberian Sun`
  also used the flag :tag:`EMEffect=yes`, which is not used in :tag:`Ares`.

:tagdef:`[Warhead]EMP.Duration=integer - frames`
  Defaults to :value:`0`.
:tagdef:`[Warhead]EMP.Cap=integer - frames`
  Defaults to :value:`-1`.

The above two flags are used together to determine how long (in frames) the
affected units will be EMP'd for.

The game keeps track of how much longer each unit will remain paralyzed. Each
unit essentially has a hidden EMP counter that counts down frame by frame until
it reaches zero, at which point the unit will be re-activated. This counter is
what gets modified by EMP warheads.

A unit does not get affected by EMP if :tag:`Verses` is equal to :value:`0%`,
otherwise the target is endowed with the full effect.

First we will look at positive :tag:`EMP.Duration` -- the targets are going to
be paralyzed.


+ :tag:`EMP.Cap` is greater than zero.
    Makes this EMP effect stackable, but capped. The target's EMP counter is
    increased by :tag:`EMP.Duration` up to but not exceeding :tag:`EMP.Cap`. If
    the target's EMP counter is already greater than :tag:`EMP.Cap` (e.g. caused
    by some other EMP weapon) then it will not be reduced.

    Examples:

    + EMP counter is 0, :tag:`EMP.Duration=10`, :tag:`EMP.Cap=20`. Result: EMP
      counter will be set to 10, because the cap is not reached yet.
    + EMP counter is 15, :tag:`EMP.Duration=10`, :tag:`EMP.Cap=20`. Result: EMP
      counter will be set to 20. This weapon will not go beyond the cap.
    + EMP counter is 60, :tag:`EMP.Duration=10`, :tag:`EMP.Cap=20`. EMP counter
      will remain at 60, because it was higher than the cap already.

+ :tag:`EMP.Cap=0`
  Makes this EMP effect stackable, but uncapped. The target's EMP counter is
  incremented by :tag:`EMP.Duration`, without limit. This is :game:`Ares` legacy
  behavior (before the :tag:`EMP.Cap` flag was added).

  Example:

  + EMP counter is 25, :tag:`EMP.Duration=10`. Result: EMP counter will be set
    to 35. Because there is no cap, firing this warhead will always add 10.

+ `EMP.Cap=-1`
  The target's EMP counter is set to this absolute number of frames specified by
  :tag:`EMP.Duration`, unless the target's EMP counter is already greater than
  this.

  Examples:

  + EMP counter is 5, :tag:`EMP.Duration=10`. Result: EMP counter will be set to
    the absolute value of 10.
  + EMP counter is 20, :tag:`EMP.Duration=10`. EMP counter will remain at 20,
    because it was already higher.

Next we will look at negative :tag:`EMP.Duration` -- for example, a friendly
unit trying to re-activate the already-paralyzed unit.

+ :tag:`EMP.Cap=-1`
  The target's EMP counter is reduced by the number of frames specified by
  :tag:`EMP.Duration`.

  Examples:

  + EMP counter is 50, :tag:`EMP.Duration=-10`. Result: EMP counter will be set
    to 40.
  + EMP counter is 7, `EMP.Duration=-10`. Result: EMP counter will be set to
    zero and the unit will re-activate, because EMP effect was removed
    completely.

+ :tag:`EMP.Cap` is greater than zero.
  The target's EMP counter is reduced by the number of frames specified by
  :tag:`EMP.Duration`. If this value is still greater than :tag:`EMP.Cap` then
  the EMP counter is reduced further to equal :tag:`EMP.Cap`.

  Examples:

  + EMP counter is 50, :tag:`EMP.Duration=-10`, :tag:`EMP.Cap=70`. Result: EMP
    counter will be set to 40.
  + EMP counter is 50, :tag:`EMP.Duration=-10`, :tag:`EMP.Cap=20`. Result: EMP
    counter will be set to 20. It is reduced to the value of the cap.
  + EMP counter is 7, `EMP.Duration=-10`. Result: EMP counter will be set to
    zero and the unit will re-activate. Even without the cap the unit would
    reacivate.

+ :tag:`EMP.Cap=0`
  :tag:`EMP.Duration` does not matter because the EMP counter will be set to
  zero by the cap and the unit will re-activate immediately. This is a special
  case of the description above.


:tagdef:`[TechnoType]ImmuneToEMP=boolean`
  The above flag specifies whether or not the :type:`TechnoType` is immune to
  the effects of EMP. The default immunity status is determined based on the
  following rules:

    + :type:`BuildingTypes`: :tag:`ImmuneToEMP` defaults to :value:`no` for
      :type:`BuildingTypes` that have :tag:`Powered=yes` and a negative
      :tag:`Power=` value set. :tag:`ImmuneToEMP` defaults to :value:`no` for
      :type:`BuildingTypes` that provide one or more of the following special
      functions:

        + Radar
        + Super weapons
        + Undeploy into a vehicle (e.g. Construction Yards)
        + Powers vehicles (e.g. Robot Control Centre)
        + Gap Generator
        + Sensors
        + Laser Fence Posts

      :tag:`ImmuneToEMP` defaults to :value:`yes` for all other
      :tag:`BuildingTypes`. For instance, power plants and pillboxes are immune
      to EMP by default, as well as SpySat buildings and factories.
    + :type:`InfantryTypes`: :tag:`ImmuneToEMP` defaults to :value:`yes` for
      :type:`InfantryTypes` unless :tag:`Cyborg=yes` is set (in which case,
      :tag:`ImmuneToEMP` defaults to :value:`no`).
    + :type:`VehicleTypes` and :type:`AircraftTypes`: :tag:`ImmuneToEMP`
      defaults to :value:`no` for :type:`VehicleTypes` and :type:`AircraftTypes`
      unless :tag:`Organic=yes` is set (in which case, `ImmuneToEMP` defaults to
      :value:`yes`).

  Manually setting :tag:`ImmuneToEMP` always overrides the default. EMP immunity
  can also be granted via the new veteran/elite ability "EMPIMMUNE". Just set
  :tag:`VeteranAbilities=EMPIMMUNE` or :tag:`EliteAbilities=EMPIMMUNE` on the
  :type:`TechnoType`. EMP immunity also respects :tag:`TypeImmune` on the
  :type:`TechnoType`, as well as :tag:`AffectsAllies` and :tag:`AffectsEnemies`
  on the warhead.
:tagdef:`[TechnoType]EMP.Modifier=float - multiplier`
  If the EMP effect duration is positive it will be multiplied by this factor.
  You can create units that are more or less prone to the Electromagnetic Pulse.
  :tag:`EMP.Modifier` defaults to :value:`100%`.

.. quickstart:: If you want a unit to be immune to EMP, set
  :tag:`ImmuneToEMP=yes` on the unit.

See :doc:`/new/destroyunitsbyemp` to learn how to crash flying
:type:`TechnoTypes` as if they were aircraft.

.. versionadded:: 0.1

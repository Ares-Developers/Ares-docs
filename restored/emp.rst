Electromagnetic Pulse (EMP)
===========================

EMP disables susceptible units and buildings along with their special functions
and makes them vulnerable to attacks. EMP can affect units and buildings in
various ways:

+ Primary effect: units will not respond to any commands. They will stop moving
  and will not attack anything.
+ Hovering units (such as the Robot Tank) will land.
+ Units display the animation specified by
  :tag:`[General]EMPulseSparkles=EMP_FX01`. Note that the :file:`emp_fx01.shp`
  file that comes with :game:`Red Alert 2` is in the :game:`Tiberian Sun`
  palette and needs to be converted.
+ Voxel-based units are darkened (SHP-based units are not).
+ Buildings that can undeploy into vehicles (e.g. MCVs) still can, but the
  resulting vehicle will remain deactivated until the effect wears off.
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
  or Siege Choppers transforming) will only become deactivated once they have
  finished unloading.
+ Harvesters that were in the middle of harvesting when hit by EMP will resume
  harvesting after EMP wears off.

.. versionadded:: 0.1


Defining EMP Weapons
--------------------

:game:`Tiberian Sun` used the weapon's :tag:`Damage` tag to determine how long
the EMP effect should last. :game:`Ares`, however, uses two new tags to provide
greater control. The weapon's :tag:`Damage` will be delivered independently from
EMP, so a weapon can both damage and deactivate its target. :game:`Tiberian Sun`
also used the tag :tag:`EMEffect=yes`, which is not used in :tag:`Ares`.

The following two tags are used together to determine how long (in frames) the
affected units will be affected by EMP for.

:tagdef:`[Warhead]EMP.Duration=integer - frames`
  Defaults to :value:`0`.
:tagdef:`[Warhead]EMP.Cap=integer - frames`
  Defaults to :value:`-1`.

The game keeps track of how much longer each unit will remain deactivated. Each
unit essentially has a hidden EMP counter that counts down frame by frame until
it reaches zero, at which point the unit will re-activate. This counter is what
gets modified by EMP warheads.

A unit does not get affected by EMP if :tag:`Verses` is equal to :value:`0%`,
otherwise the target is endowed with the full effect.

.. quickstart:: If you want a warhead to EMP a target for ten seconds, set
    \ :tag:`EMP.Duration=150` on the warhead.


Damaging EMP
~~~~~~~~~~~~

With a positive :tag:`EMP.Duration` the targets are going to be deactivated.

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
  behavior (before the :tag:`EMP.Cap` tag was added).

  Example:

  + EMP counter is 25, :tag:`EMP.Duration=10`. Result: EMP counter will be set
    to 35. Because there is no cap, firing this warhead will always add 10.

+ :tag:`EMP.Cap=-1`
  The target's EMP counter is set to this absolute number of frames specified by
  :tag:`EMP.Duration`, unless the target's EMP counter is already greater than
  this.

  Examples:

  + EMP counter is 5, :tag:`EMP.Duration=10`. Result: EMP counter will be set to
    the absolute value of 10.
  + EMP counter is 20, :tag:`EMP.Duration=10`. EMP counter will remain at 20,
    because it was already higher.


Healing EMP
~~~~~~~~~~~

This can be used for re-activating deactivated allied units. With a negative
:tag:`EMP.Duration`, the EMP counter is reduced by this number of frames.

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
    reactivate.

+ :tag:`EMP.Cap=0`
  :tag:`EMP.Duration` does not matter because the EMP counter will be set to
  zero by the cap and the unit will re-activate immediately. This is a special
  case of the description above.


EMP Immunity
------------

There are several ways to create units that are not affected by EMP weapons.

:tagdef:`[TechnoType]ImmuneToEMP=boolean`
  The above tag specifies whether or not the :type:`TechnoType` is immune to the
  effects of EMP. The default immunity status is determined based on the
  following rules:

  + :type:`BuildingTypes`: Defaults to :value:`no` if :tag:`Powered=yes` and
    :tag:`Power` is negative. Defaults to :value:`no` if providing one or more
    of the following special functions:

    + Radar
    + Super weapons (:tag:`SuperWeapon` and :tag:`SuperWeapon2` only)
    + Undeploy into a vehicle (e.g. Construction Yards)
    + Powers vehicles (e.g. Robot Control Centre)
    + Gap Generator
    + Sensors
    + Laser Fence Posts

    Defaults to :value:`yes` otherwise.
  + :type:`InfantryTypes`: Defaults to :value:`no` if :tag:`Cyborg=yes`, to
    :value:`yes` otherwise.
  + :type:`VehicleTypes` and :type:`AircraftTypes`: Defaults to :value:`yes` if
    :tag:`Organic=yes`, to :value:`no` otherwise.

EMP immunity can also be granted using the new veteran/elite ability
:value:`EMPIMMUNE`. Set :tag:`VeteranAbilities` or :tag:`EliteAbilities` on the
:type:`TechnoType`.

EMP immunity also respects :tag:`TypeImmune` on the :type:`TechnoType`, as well
as :tag:`AffectsAllies` and :tag:`AffectsEnemies` on the warhead.


Modifying the Effect Duration
-----------------------------

Instead of either affecting an object fully or not at all, :game:`Ares` allows
to also reduce or increase the duration of EMP for each type. A high tech tank
could thus stay deactivated longer than a normal tank, while a low tech jeep
could reactivate sooner than the tank.

:tagdef:`[TechnoType]EMP.Modifier=float - multiplier`
  If the EMP effect duration is positive it will be multiplied by this factor.
  You can create units that are more or less prone to the Electromagnetic Pulse.
  Defaults to :value:`100%`.


Destructive EMP
---------------

See :doc:`/new/destroyunitsbyemp` to learn how to crash flying
:type:`TechnoTypes` as if they were aircraft.

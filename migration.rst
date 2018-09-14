---------------
Migration Guide
---------------

If you are upgrading from previous versions of :game:`Ares`, you may have to
account for the following changes.

From Ares 0.1
~~~~~~~~~~~~~

Changed tags:

  :tag:`[SuperWeapon]SW.Deliver` --> :tag:`[SuperWeapon]Deliver.Types`.
    Replace the old tag name by the new tag name.
  
  :tag:`[SuperWeapon]SW.DeliverBuildups` --> :tag:`[SuperWeapon]Deliver.Buildups`.
    Replace the old tag name by the new tag name.
  
  :tag:`[SuperWeapon]SonarPulse.Range` --> :tag:`[SuperWeapon]SW.Range`.
    Replace the old tag name by the new tag name.
  
  :tag:`[SuperWeapon]GenericWarhead.Warhead` --> :tag:`[SuperWeapon]SW.Warhead`.
    Replace the old tag name by the new tag name.
  
  :tag:`[SuperWeapon]GenericWarhead.Damage` --> :tag:`[SuperWeapon]SW.Damage`.
    Replace the old tag name by the new tag name.
  
  :tag:`[SuperWeapon]Nuke.Sound` --> :tag:`[SuperWeapon]SW.ActivationSound`.
    Replace the old tag name by the new tag name.

Other changes:

  :game:`Ares` 0.1 supported options in :file:`ares.ini` to configure how
  graphics surfaces were allocated. The tags :tag:`Surface.*.Memory` and
  :tag:`Surface.*.Force3D` are obsolete now and have no effect any more.

From Ares 0.2 and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  No changes required.

Other changes:

  The ini file reader has been updated for :game:`Ares` 0.3. Values that were
  invalid previously might now be valid, and previously valid notations might
  have become invalid. If values cannot be parsed correctly, :game:`Ares`
  puts a message into the debug log.

  For example, it was possible to supply only one or two numbers when three
  comma separated numbers were expected. In that case, the value became
  inconsistent. This is no longer allowed and will result in a message in the
  debug log.

From Ares 0.3 and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  The following tags have been changed to use the actual value of their default
  tags, not the value the default tags have in :file:`rulesmd.ini`. If a default
  is changed in a game mode or map file, this updated value will be used. In
  other words: It now uses the last value, while previously the first would have
  been used.

  If you do not change a default tag in game modes or maps, no action is needed.
  If you want to use the value the default tag has in :file:`rulesmd.ini`, you
  have to copy the default value to the respective tag. 

  :tag:`[Weapon]IvanBomb.AttachSound`
    Defaults to :tag:`[AudioVisual]BombAttachSound`.

  :tag:`[Weapon]IvanBomb.TickingSound`
    Defaults to :tag:`[AudioVisual]BombTickingSound`.

  :tag:`[SuperWeapon]Lightning.Sounds`
    Defaults to :tag:`[AudioVisual]LightningSounds`.

  :tag:`[SuperWeapon]Lightning.Clouds`
    Defaults to :tag:`[General]WeatherConClouds`.

  :tag:`[SuperWeapon]Lightning.Bolts`
    Defaults to :tag:`[General]WeatherConBolts`.

  :tag:`[SuperWeapon]Lightning.Debris`
    Defaults to :tag:`[General]MetallicDebris`.

Other changes:

  Animations that have an owner now also respect :tag:`AffectsAllies`.
  Previously only :tag:`AffectsEnemies` was supported.

  The original tag :tag:`Crashable` does now also apply to
  :type:`AircraftTypes`. Previously it had no function.

  The original tags :tag:`Pip` and :tag:`OccupyPip` have been changed to also
  support integers. Previously, integers were invalid and defaulted to
  :value:`green`.

From Ares 0.4 and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  The following tags have been changed to use the actual value of their default
  tags. (Continued work from the :game:`Ares` 0.4 release.)

  :tag:`[Side]DefaultDisguise`
    Defaults to the original tag for a side.

  :tag:`[Side]Crew`
    Defaults to the original tag for a side.

  :tag:`[Side]SurvivorDivisor`
    Defaults to the original tag for a side.

  :tag:`[Side]AI.BaseDefenses`
    Defaults to the original tag for a side.

  :tag:`[Side]AI.BaseDefenseCounts`
    Defaults to the original tag for a side.

  :tag:`[Weapon]IvanBomb.Warhead`
    Defaults to :tag:`[CombatDamage]IvanWarhead`.

  :tag:`[Weapon]IvanBomb.Damage`
    Defaults to :tag:`[CombatDamage]IvanDamage`.

  :tag:`[Weapon]IvanBomb.Delay`
    Defaults to :tag:`[CombatDamage]IvanTimedDelay`.

  :tag:`[Weapon]IvanBomb.FlickerRate`
    Defaults to :tag:`[CombatDamage]IvanIconFlickerRate`.

Other changes:

  Values in :tag:`[Side]Crew` and :tag:`[Side]DefaultDisguise` will not be added
  to the list of :type:`InfantryTypes` automatically any more. Make sure these
  values are listed under the :type:`InfantryTypes` list.

  Previously, destroyed units did not eject survivors if they were owned by
  :value:`Neutral` or :value:`Special`, because :game:`Ares` did not support
  survivors for them. The original handling has been restored, and these houses
  will use :tag:`[General]Technician` as crew.

From Ares 0.5 and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  The following tags have been changed to use the actual value of their default
  tags. (Continued work from earlier :game:`Ares` releases.)

  :tag:`[Side]ParaDrop.Num`
    Defaults to the original tag for a side.

  :tag:`[Side]ParaDrop.Types`
    Defaults to the original tag for a side.

  :tag:`[Side]Parachute.Anim`
    Defaults to :tag:`[General]Parachute`.

  :tag:`[Country]ParaDrop.Num`
    Defaults to the side's :tag:`ParaDrop.Num`.

  :tag:`[Country]ParaDrop.Types`
    Defaults to the side's :tag:`ParaDrop.Types`.

  :tag:`[Country]AI.PowerPlants`
    If empty or not set, the side's default power plants are used.

  :tag:`[Weapon]Wave.Color`
    Default depends on wave type.

  :tag:`[SuperWeapon]SW.Damage`
    Default depends on :tag:`Type`.

  :tag:`[SuperWeapon]SW.Range`
    Default depends on :tag:`Type`.

  :tag:`[SuperWeapon]SW.Deferment`
    Defaults to :tag:`[General]LightningDeferment` for
    :tag:`Type=LightningStorm`.

  :tag:`[SuperWeapon]SW.Animation`
    Default depends on :tag:`Type`.

  :tag:`[SuperWeapon]SW.Sound`
    Default depends on :tag:`Type`.

  :tag:`[SuperWeapon]SW.ActivationSound`
    Default depends on :tag:`Type`.

  :tag:`[SuperWeapon]Lightning.Duration`
    Defaults to :tag:`[General]LightningStormDuration`.

  :tag:`[SuperWeapon]Lightning.RadarOutage`
    Defaults to :tag:`[General]LightningStormDuration`.

  :tag:`[SuperWeapon]Lightning.HitDelay`
    Defaults to :tag:`[General]LightningHitDelay`.

  :tag:`[SuperWeapon]Lightning.ScatterDelay`
    Defaults to :tag:`[General]LightningScatterDelay`.

  :tag:`[SuperWeapon]Lightning.Separation`
    Defaults to :tag:`[General]LightningSeparation`.

  :tag:`[SuperWeapon]Lightning.PrintText`
    Defaults to :tag:`[General]LightningPrintText`.

  :tag:`[SuperWeapon]Lightning.BoltExplosion`
    Defaults to :tag:`[General]WeatherConBoltExplosion`.

  :tag:`[SuperWeapon]Nuke.TakeOff`
    Defaults to :tag:`[General]NukeTakeOff`.

  :tag:`[SuperWeapon]Dominator.FireAtPercentage`
    Defaults to :tag:`[General]DominatorFireAtPercentage`.

  :tag:`[SuperWeapon]Chronosphere.BlastSrc`
    Defaults to :tag:`[General]ChronoBlast`.

  :tag:`[SuperWeapon]Chronosphere.BlastDest`
    Defaults to :tag:`[General]ChronoBlastDest`.

  :tag:`[SuperWeapon]Mutate.Explosion`
    Defaults to :tag:`[General]MutateExplosion`.

From Ares 0.6 and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  No changes required.

Other changes:

  Only unpowered units create sparkle particle systems. Deactivation because of
  EMP and Operator logics does not make the unit sparkle any more. This is not
  optional at the moment.

From Ares 0.7 and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  No changes required.

Other changes:

  The Unit Delivery super weapon uses a new placing method. Compared to previous
  versions, unit and buildings are placed more random now. Delivered objects are
  put on guard, area guard or hunt mission.

  Force Shield no longer considers buildings with :tag:`ForceShield.Modifier`
  less than or equal to :value:`0.0` eligible targets.

  Super weapon targeting mode :value:`Self` now centers on the firing building
  instead of using the origin.

From Ares 0.8 and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  The following tags have been changed to use the actual value of their default
  tags. (Continued work from earlier :game:`Ares` releases.)

  :tag:`[BuildingType]SecretLab.PossibleBoons`
    Defaults to the combination of the latest :tag:`[General]SecretInfantry`,
    :tag:`[General]SecretUnits` and :tag:`[General]SecretBuildings`.

Other changes:

  The way projectiles deliver the new warhead effects has changed. Previously,
  they were applied on the location the projectile was supposed to hit, not
  where it actually detonated. Short distance misses still count as direct hit.
  Abduction, KillDriver and Occupant Damage are only applied on direct hits.

  AttachEffect only checked verses if it had an owner. Now verses are applied
  even if owner-less. Previously affected victims might not get affected any
  more.

  The default :tag:`SW.AITargeting` for :tag:`Type=HunterSeeker` super weapons
  has been changed from :value:`NoTarget` to :value:`HunterSeeker`. It now only
  fires if the house has selected a favorite enemy.

  The targeting type :value:`Stealth` now adheres to :tag:`SW.AIRequiresTarget`
  and :tag:`SW.AIRequiresHouse` instead of :tag:`SW.RequiresTarget` and
  :tag:`SW.RequiresHouse`. The targeting type :value:`Offensive` no longer
  requires :tag:`SW.AffectedHouse` to include :value:`enemies`.

  Prism Forwarding now properly uses negative intensity values for supporting
  beams. A :tag:`PrismSupportModifier` related bug has been fixed.

  Lasers were often drawn too big. This has been changed.

From Ares 0.9 and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  No changes required.

Other changes:

  Solid Buildings have been reworked. The feature now works with invisible
  projectiles. Also, units will now change positions instead of just firing
  through a Solid Building.

  The Firestorm Wall active and idle animations will now draw in the building's
  palette, while they were drawn using the animation palette before.

  :file:`ares.csf` will always be read, no matter which language the game is run
  in.

From Ares 0.A and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  No changes required.

Other changes:

  None.

From Ares 0.B and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  :tag:`[TechnoType]Spotlight.StartHeight`
    Default has been changed to :value:`430`. Defaulted to :value:`200` before.

  :tag:`[TechnoType]Spotlight.AttachedTo`
    The value :value:`barrel` is no longer supported. Use :value:`turret`
    instead.

  :tag:`[Country]AI.PowerPlants`
    Default for the second side and all sides after side 3 now includes
    :tag:`[General]NodAdvancedPower` again.

  :tag:`[Projectile]SubjectToFirewall`
    The tag has been removed. Use :tag:`[Projectile]IgnoresFirestorm` instead.

Other changes:

  None.

From Ares 0.C and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  :tag:`[General]EngineerDamageCursor`
    The tag has been removed. Customize the :value:`EngineerDamage` cursor
    instead.

  :tag:`[General]TogglePowerCursor`
    The tag has been removed. Customize the :value:`TogglePower` cursor
    instead.

  :tag:`[General]TogglePowerNoCursor`
    The tag has been removed. Customize the :value:`NoTogglePower` cursor
    instead.

  :tag:`[SuperWeapon]Cursor`
    The tag has been changed to only support mouse cursor names.

  :tag:`[SuperWeapon]NoCursor`
    The tag has been changed to only support mouse cursor names.

  :tag:`[SuperWeapon]Deliver.Buildups`
    The tag has been removed. Buildups are now always on.

Other changes:

  Some :type:`ArmorType` parsing issues have been resolved to improve defaulting
  to other types, and to not reset data unexpectedly.

  The Unit Delivery super weapon has been reworked. It now allows placing units
  on ore, and delivered objects are put on guard, area guard or hunt mission.
  The option to skip the buildup animations has been deprecated, because it
  never worked correctly.

  Hunter Seekers no longer target objects under the effect of the Iron Curtain
  or objects being temporally attacked.

From Ares 0.D and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  :tag:`[SuperWeapon]Nuke.Payload`
    No longer automatically adds the weapon to the list. Ensure that the weapon
    is known to the game by adding it to the :tag:`[WeaponTypes]` list.

Other changes:

  :tag:`KillDriver` has been changed to be applied like regular damage. It now
  respects immunities and supports :tag:`CellSpread`. Thus, the effect might
  not be applied in all cases where it was applied before, and might be applied
  in cases where it previously was not.

From Ares 0.E and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  No changes required.

Other changes:

  Some Super Weapon Targeting Modes used the wrong target cell when firing at
  buildings. Now, the centers of the buildings are targeted. Affected modes are
  :value:`Nuke`, :value:`LightningStorm`, :value:`Offensive`, :value:`Stealth`,
  :value:`Self`, and :value:`MultiMissile`.

From Ares 1.0 and below
~~~~~~~~~~~~~~~~~~~~~~~

Changed tags:

  :tag:`[BuildingType]SpyEffect.UnitVeterancy`
    This setting has been replaced by finer grained options. Replace with
    :tag:`SpyEffect.InfantryVeterancy=yes` for :type:`BuildingType`\ s with
    :tag:`Factory=InfantryType`, and with :tag:`SpyEffect.VehicleVeterancy=yes`
    for :type:`BuildingType`\ s with :tag:`Factory=UnitType` to achieve the
    previous effect.

  :tag:`[BuildingType]FactoryOwners.HaveAllPlans=` --> :tag:`[BuildingType]FactoryOwners.Permanent=`.
    Replace the old tag name by the new tag name.

  :tag:`[Warhead]Ripple.Radius=` --> :tag:`[Warhead]IonCannon.Ripple=`.
    Replace the old tag name by the new tag name.

  :tag:`[Weapon]Abductor.ChangeOwner=`.
    Respects :value:`PSIONICSIMMUNE` veteran ability.

Other changes:

  Splits logic only targets air units if the :tag:`AirburstWeapon` projectile is
  :tag:`AA=yes`. Furthermore, Splits logic now only retargets objects that the
  projectile's warhead can affect.

  Units lifted by a Magnetron no longer count as being actively in air, and EMP
  might no longer destroy them.

  The AI supports other Iron Curtains and it might now use super weapons with
  :tag:`Type=IronCurtain` it has not used before, because of the changed default
  for :tag:`SW.AITargetingMode`. To restore previous behavior, manually set
  :tag:`SW.AITargetingMode=none` on all but the first super weapon with
  :tag:`Type=IronCurtain`.

  :tag:`DeployToLand=yes` units will only turn towards :tag:`DeployDir` if they
  have a :tag:`DeployingAnim`.

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
  puts a message to the debug log.

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
    Defaults depends on :tag:`Type`.

  :tag:`[SuperWeapon]SW.Range`
    Defaults depends on :tag:`Type`.

  :tag:`[SuperWeapon]SW.Deferment`
    Defaults to :tag:`[General]LightningDeferment` for
    :tag:`Type=LightningStorm`.

  :tag:`[SuperWeapon]SW.Animation`
    Defaults depends on :tag:`Type`.

  :tag:`[SuperWeapon]SW.Sound`
    Defaults depends on :tag:`Type`.

  :tag:`[SuperWeapon]SW.ActivationSound`
    Defaults depends on :tag:`Type`.

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

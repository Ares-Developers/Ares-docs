---------------
Migration Guide
---------------

If you are upgrading from previous versions of :game:`Ares`, you may have to
account for the following changes.

From Ares 0.1
~~~~~~~~~~~~~

Changed tags:

  :tag:`[Superweapon]SW.Deliver` --> :tag:`[Superweapon]Deliver.Types`.
    Replace the old tag name by the new tag name.
  
  :tag:`[Superweapon]SW.DeliverBuildups` --> :tag:`[Superweapon]Deliver.Buildups`.
    Replace the old tag name by the new tag name.
  
  :tag:`[Superweapon]SonarPulse.Range` --> :tag:`[Superweapon]SW.Range`.
    Replace the old tag name by the new tag name.
  
  :tag:`[Superweapon]GenericWarhead.Warhead` --> :tag:`[Superweapon]SW.Warhead`.
    Replace the old tag name by the new tag name.
  
  :tag:`[Superweapon]GenericWarhead.Damage` --> :tag:`[Superweapon]SW.Damage`.
    Replace the old tag name by the new tag name.
  
  :tag:`[Superweapon]Nuke.Sound` --> :tag:`[Superweapon]SW.ActivationSound`.
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

  :tag:`[Superweapon]Lightning.Sounds`
    Defaults to :tag:`[AudioVisual]LightningSounds`.

  :tag:`[Superweapon]Lightning.Clouds`
    Defaults to :tag:`[General]WeatherConClouds`.

  :tag:`[Superweapon]Lightning.Bolts`
    Defaults to :tag:`[General]WeatherConBolts`.

  :tag:`[Superweapon]Lightning.Debris`
    Defaults to :tag:`[General]MetallicDebris`.

Other changes:

  Animations that have an owner now also respect :tag:`AffectsAllies`.
  Previously only :tag:`AffectsEnemies` was supported.

  The original tag :tag:`Crashable` does now also apply to
  :type:`AircraftTypes`. Previously it had no function.

  The original tags :tag:`Pip` and :tag:`OccupyPip` have been changed to also
  support integers. Previously, integers were invalid and defaulted to
  :value:`green`.

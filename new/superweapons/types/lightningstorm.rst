:captiontag:`Type=LightningStorm`
`````````````````````````````````

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Area around the target location the Lightning Storm strikes. Note that a
  single value denotes the diameter of a circle -- this is not the radius.
  Defaults to :tag:`[General]LightningCellSpread`.
:tagdef:`[SuperWeapon]SW.Damage=integer`
  The damage each lightning bolt delivers. Defaults to
  :tag:`[General]LightningDamage`.
:tagdef:`[SuperWeapon]SW.Warhead=Warhead`
  The warhead used to deal the damage of each lightning bolt. Defaults to
  :tag:`[General]LightningWarhead`.
:tagdef:`[SuperWeapon]SW.Deferment=integer frames`
  Defaults to :tag:`[General]LightningDeferment`.
:tagdef:`[SuperWeapon]SW.ActivationSound=Sound`
  Defaults to :tag:`[AudioVisual]StormSound`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`LightningStorm`.
:tagdef:`[SuperWeapon]Light.*=integer`
  Default to the scenario's :tag:`[Lighting]Ion*`.


Lightning Storm specific tags:

:tagdef:`[SuperWeapon]Lightning.Duration=integer - frames`
  The length the Lightning Storm endures. A value of :value:`-1` means
  indefinite duration. Defaults to :tag:`[General]LightningStormDuration`.
:tagdef:`[SuperWeapon]Lightning.RadarOutage=integer - frames`
  The number of frames radars are jammed for players defined by
  :tag:`SW.AffectsHouse`. Defaults to :tag:`[General]LightningStormDuration`.
:tagdef:`[SuperWeapon]Lightning.RadarOutageAffects=enum`
  Specifies the houses affected by radar outage. Defaults to :value:`enemies`.
:tagdef:`[SuperWeapon]Lightning.HitDelay=integer - frames`
  The number of frames between two clouds being created over the target cell.
  Values of 0 or lower will disable direct hits. Clouds created by this
  mechanism are never subject to separation rules (see below). Defaults to
  :tag:`[General]LightningHitDelay`.
:tagdef:`[SuperWeapon]Lightning.ScatterDelay=integer - frames`
  The number of frames between clouds getting created over a random cell in the
  super weapon's range. Values of 0 or lower will disable random hits. Only
  clouds created by this mechanism are subject to separation rules (see below).
  Defaults to :tag:`[General]LightningScatterDelay`.
:tagdef:`[SuperWeapon]Lightning.ScatterCount=integer`
  The number of new clouds created every :tag:`Lightning.ScatterDelay` frames.
  Values of 0 or lower will disable random hits. Defaults to :value:`1`.
:tagdef:`[SuperWeapon]Lightning.Separation=integer - distance`
  The least number of cells between two random clouds to better distribute
  damage. This is not the direct distance, but rather the sum of the differences
  of the x and y components. Values of 0 or lower will disable separation rules.
  Defaults to :tag:`[General]LightningSeparation`.
:tagdef:`[SuperWeapon]Lightning.PrintText=boolean`
  Enables the warning text appearing shortly before the Lightning Storm strikes.
  Defaults to :tag:`[General]LightningPrintText`.
:tagdef:`[SuperWeapon]Lightning.IgnoreLightningRod=boolean`
  Disables the special handling for buildings with :tag:`LightningRod=yes` set.
  Defaults to :value:`no`.
:tagdef:`[SuperWeapon]Lightning.DebrisMin=integer`
  The least number of debris created when lightning strikes empty cells or
  destroys a building or a unit. Defaults to :value:`2`.
:tagdef:`[SuperWeapon]Lightning.DebrisMax=integer`
  The largest number of debris created when lightning strikes empty cells or
  destroys a building or a unit. Defaults to :value:`4`.
:tagdef:`[SuperWeapon]Lightning.CloudHeight=integer - leptons`
  The height above the ground the clouds get created in. Values less than 0 will
  center the cloud image on top of the first bolt anim from the list (for the
  original game this is about 1200). Defaults to :value:`-1`.
:tagdef:`[SuperWeapon]Lightning.BoltExplosion=Animation`
  Every lightning bolt will display this damage animation upon impact. Defaults
  to :tag:`[General]WeatherConBoltExplosion`.
:tagdef:`[SuperWeapon]Lightning.Sounds=list of Sounds`
  A comma separated list of sounds played when lightning strikes. Defaults to
  :tag:`[AudioVisual]LightningSounds`.
:tagdef:`[SuperWeapon]Lightning.Clouds=list of Animation`
  A comma separated list of cloud animations. Defaults to
  :tag:`[General]WeatherConClouds`.

  .. note:: If this list is empty, the Lightning Storm super weapon will
    not function. 
:tagdef:`[SuperWeapon]Lightning.Bolts=list of Animation`
  A comma separated list of bolt animations. If this list is empty, the damage
  is caused even though no bolts are shown. Defaults to
  :tag:`[General]WeatherConBolts`.

  .. warning:: Do not use :tag:`Bouncer=yes` animations with
    \ :tag:`Lightning.Bolts`. This leads to crashes if a building is hit.

:tagdef:`[SuperWeapon]Lightning.Debris=list of Animation`
  A comma separated list of animations used as debris when lightning strikes.
  Defaults to :tag:`[General]MetallicDebris`.


Other changes:

Lightning rods attract random lightning that is about to strike in close range.
For more information see the :doc:`Lightning Rods
</new/buildings/lightningrods>` section.

.. versionadded:: 0.2

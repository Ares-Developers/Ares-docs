Super Weapons
~~~~~~~~~~~~~

In Yuri's Revenge, there is very little you can do to change or add to
the existing super weapons most super weapon-related features are
hard-coded to only work as designed for the original super weapons.
Ares, however, includes several new ways to customize existing super
weapons as well as several wholly new super weapons. Super Weapons:

NB: You cannot change a super weapon's `Type=` or `Action=` values in
any of the game mode specific INI files (like mpfreeforallmd.ini) or
map files. To achive the same effect, add a new super weapon to
rulesmd.ini with the different `Type=` or `Action=` and change
`SuperWeapon=` for the respective owner buildings to use the new super
weapon in the INI file instead.



Building Animations
```````````````````

Buildings can display specific animations for when the attached super
weapon is charging, is nearly charged (1 minute remaining in the
normal game), is ready to be fired, and when it fires. However, in
Yuri's Revenge, these animations only work properly for the original
super weapons. In Ares, these will work for any super weapon. Building
animations played correctly for new super weapons.

.. versionadded:: 0.1



General properties
``````````````````

:[SuperWeapon]SW.Range= (float,int): Most superweapons having a ranged
  effect can take a float or two integers. One float is taken as radius
  around the target cell, two integers separated by comma denote a
  rectangular area. For example, `SW.Range=3.5` defines a circle with 7
  cells diameter, `SW.Range=4,6` defines a rectangle 4 cells wide and 6
  cells high. The range is no longer bound to cell spread's limitation
  of a maximum range of 10. SW.Range=
:[SuperWeapon]SW.CreateRadarEvent= (bool): Creates a radar event
  rectangle for every player centered above the super weapon's target
  cell. SW.CreateRadarEvent=
:[SuperWeapon]SW.AffectsHouse= (enum
  none|owner|allies|team|enemies|all): Which houses items are affected
  by this super weapon. You can combine multiple values by comma. `team`
  equals `owner,allies`, `all` equals `owner,allies,enemies`. Defaults
  to `team` for the Force Shield, to `all` otherwise. SW.AffectsHouse=
:[SuperWeapon]SW.AffectsTarget= (enum
  land|water|empty|infantry|units|buildings): Which items are allowed to
  be affected by this super weapon. You can combine multiple values by
  comma. If you don't specify either land or water, both will be
  allowed. If you don't specify any of the other values, everything can
  be affected. For example, `SW.AffectsTarget=land,buildings` affects
  all buildings that aren't water-bound, `SW.AffectsTarget=water`
  affects every water cell, occupied or empty. SW.AffectsTarget=
:[SuperWeapon]SW.ShowCameo= (boolean): Sets whether this super weapon
  will appear in the side bar. This setting is ignored if
  `SW.AutoFire=no` is set. Defaults to `yes`. SW.ShowCameo=
:[SuperWeapon]SW.Deferment= (integer frames): The number of frames
  after the fired super weapon takes effect. Not all super weapons
  support deferment. SW.Deferment=


.. versionadded:: 0.1



Hardcoded Values
````````````````

It made no sense to have the values `PreClick`, `PostClick`, and
`PreDependent` customizable. Ares hardcodes these values and they have
no effect any more. Instead, `SW.PostDependent` takes their place.
PreClick, PostClick, and PreDependent are replaced by PostDependent.

:[SuperWeapon]SW.PostDependent= (SuperWeapon): The super weapon
  invoked right after firing this super weapon. As in Red Alert 2 the
  only super weapon using this is the ChronoSphere invoking the
  ChronoWarp. To distinguish between multiple of such super weapons you
  can provide the specific super weapon ID here. For example,
  `[ChronoSphereSpecial]SW.PostDependent=ChronoWarpSpecial` switches to
  the ChronoWarp type super weapon after you chose the source location
  SW.PostDependent=


.. versionadded:: 0.2



Targeting
`````````

:[SuperWeapon]SW.FireIntoShroud= (boolean): Whether or not this super
  weapon is allowed to fire into an unexplored area of the map. Default
  is `yes`. FireIntoShroud optional. SW.FireIntoShroud=
:[SuperWeapon]SW.AutoFire= (boolean): Sets whether this super weapon
  should be launched automatically even for human players. If this is
  set to `yes`, the AI targeting options are used to infer the best
  target cell. Defaults to `no`. SW.AutoFire=
:[SuperWeapon]SW.ManualFire= (boolean): Sets whether this super weapon
  can be fired by the owning player. If set to `no`, the player will not
  be able to launch the super weapon. This setting is ignored if
  `SW.AutoFire=no` is set. Defaults to `yes`. SW.ManualFire=
:[SuperWeapon]SW.RequiresTarget= (enum
  land|water|empty|infantry|units|buildings): Which items this super
  weapon can fire upon. Hovering above an allowed item will show the
  `Cursor`, otherwise the player gets the `NoCursor` and it is not
  possible to launch the super weapon. For an example see
  `SW.AffectsTarget=`. Please be aware of the problems that can arise if
  this and `SW.AffectsTarget=` are set to mutually exclusive values not
  allowing the super weapon to affect anything. SW.RequiresTarget=
:[SuperWeapon]SW.RequiresHouse= (enum
  none|owner|allies|team|enemies|all): Which house's items this super
  weapon can fire upon. SW.RequiresHouse=
:[SuperWeapon]SW.AITargeting= (enum SW Targeting Type): Select one of
  the following values to define how the AI will use this super weapon:
  SW.AITargetingType=



+ None : The AI will not use this super weapon and it cannot auto-
  fire.
+ LightningStorm : Targets offensively, but waits until a currently
  striking Lightning Storm subsides.
+ Nuke : Targets offensively, or strikes the waypoint set by map
  triggers.
+ PsychicDominator : Targets the largest group of enemy units.
+ GeneticMutator : Targets the largest group of enemy infantry (in a
  3x3 area).
+ ParaDrop : Targets the least defended cell near the enemy base.
+ ForceShield : Targets the position an enemy super weapon is about to
  hit to protect against it.
+ NoTarget : This super weapon doesn't need any valid coordinates to
  strike.
+ Offensive : Targets offensively, without any special handling like
  `LightningStorm` or `Nuke`.
+ Stealth : Targets stealth units or buildings only. Respects
  `SW.RequiresTarget` and `SW.RequiresHouse`.
+ Base : Targets the owning player's base center.
+ Self : Targets buildings providing this very super weapon, belonging
  to the owning player only.


.. versionadded:: 0.1



Cursors
```````

Ares allows you to specify custom mouse cursors for the super weapon,
using the following flags: Custom cursors.

:[SuperWeapon]Cursor.Frame= (integer): Starting frame of the cursor
  from mouse.sha. Defaults to the Attack cursor. Cursor.Frame=
:[SuperWeapon]Cursor.Count= (integer): Number of frames in the
  animated cursor. Cursor.Count=
:[SuperWeapon]Cursor.Interval= (integer) Cursor.Interval= : How often
  to animate the cursor? Default is 5.
:[SuperWeapon]Cursor.MiniFrame= (integer): Same as `Cursor.Frame`,
  except this is for the mouse cursor when positioned on the minimap.
  Cursor.MiniFrame=
:[SuperWeapon]Cursor.MiniCount= (integer): Same as `Cursor.Count`,
  except this is for the mouse cursor when positioned on the minimap.
  Cursor.MiniCount=
:[SuperWeapon]Cursor.HotSpot= (HotSpot X, HotSpot Y): Specifies the
  coordinates on the cursor that are considered to be the 'tip' that is,
  the point from which the click event will handled. HotSpot X should be
  one of "Left", "Center" or "Middle". HotSpot Y should be one of "Top",
  "Middle" or "Bottom". For example, `Cursor.HotSpot=Left,Top` will
  treat the top-left corner of the cursor as the tip. Default is
  "Center,Middle".


All of the above " `Cursor.`" flags have a corresponding "
`NoCursor.`" flag, which allows you to specify the cursor that will be
displayed then the mouse pointer is positioned over a point where the
super weapon cannot be fired (e.g. the Force Shield cannot be fired
over empty ground, so will display an alternate cursor to indicate
this). Cursor.HotSpot=

:[SuperWeapon]NoCursor.Frame= [SuperWeapon]NoCursor.Count=
  [SuperWeapon]NoCursor.Interval= [SuperWeapon]NoCursor.MiniFrame=
  [SuperWeapon]NoCursor.MiniCount= [SuperWeapon]NoCursor.HotSpot=: The "
  `NoCursor.`" flags default to the same value as their " `Cursor.`"
  counterparts. NoCursor.Count= NoCursor.Frame= NoCursor.HotSpot=
  NoCursor.Interval= NoCursor.MiniCount= NoCursor.MiniFrame=


.. versionadded:: 0.1



Charge/Drain Super Weapons
``````````````````````````

Instead of one global setting, Ares supports customizable
ChargeToDrainRatio settings for each super weapon. All settings here
only apply for super weapons having `UseChargeDrain=yes` set.
Customizable charge to drain ratio for each superweapon.

:[SuperWeapon]SW.ChargeToDrainRatio= (float multiplier): The recharge
  time multiplied by this value is how long the super weapon will stay
  active. Must not be `0`. Defaults to `[General]ChargeToDrainRatio`.
  SW.ChargeToDrainRatio=
:[SuperWeapon]SW.Unstoppable= (boolean): Whether this super weapon can
  be stopped when active. Otherwise clicks on the super weapon's cameo
  are ignored. Defaults to `no`. SW.Unstoppable=


Note that `UseChargeDrain` is supported for the Firewall super weapon
only. Using it along with any other super weapon types it will lead to
unexpected results.

.. versionadded:: 0.2



Cost
````

The firing of a super weapon can now add or subtract credits from the
firing player's cash reserve. If the player doesn't have enough funds
the launch is aborted and an EVA event is triggered to notify the
player. Super weapons costing money will show the needed amount in the
super weapon's cameo tool tip. Money deductable when firing a
superweapon.

:[SuperWeapon]Money.Amount= (integer credits): This many credits are
  added to the firing player's account when the super weapon is fired.
  Use a negative number to subtract credits. Money.Amount=
:[SuperWeapon]Money.DrainAmount= (integer credits): This many credits
  are added to the firing player's account when a `UseChargeDrain=yes`
  super weapon is active. Use a negative number to subtract credits.
  Money.DrainAmount=
:[SuperWeapon]Money.DrainDelay= (integer frames): After this many
  frames the credits defined in `Money.DrainAmount=` are added to the
  firing player's account when a `UseChargeDrain=yes` super weapon is
  active. Money.DrainDelay=


.. versionadded:: 0.1



Animation/Sound
```````````````

The default values depend on the super weapon's actual `Type`.

:[SuperWeapon]SW.Animation= (animation): The animation to display at
  the super weapon's target cell. SW.Animation=
:[SuperWeapon]SW.AnimationHeight= (integer): How high above the target
  cell to display the animation. Custom animation played at target cell.
  SW.AnimationHeight=
:[SuperWeapon]SW.AnimationVisibility= (enumeration
  none|owner|allies|team|enemies|all): Defines who will see this
  animation. Custom SW animation visibility. SW.AnimationVisibility=
:[SuperWeapon]SW.Sound= (sound): The sound to play at the super
  weapon's target cell. SW.Sound=
:[SuperWeapon]SW.ActivationSound= (sound): The sound to play when a
  Nuke is fired or a deferrable super weapon like the Lightning Storm is
  activated. SW.ActivationSound=


.. versionadded:: 0.1



EVA Events
``````````

:[SuperWeapon]EVA.Detected= (EVA event): The EVA event that will be
  triggered when the super weapon building is constructed (the EVA event
  is not played for the owner of the building). EVA.Detected=
:[SuperWeapon]EVA.Ready= (EVA event): The EVA event that will be
  triggered when the super weapon is ready to fire (the EVA event is
  only played for the owner of the super weapon). EVA.Ready=
:[SuperWeapon]EVA.Activated= (EVA event): The EVA event that will be
  triggered when the super weapon is fired. EVA.Activated=
:[SuperWeapon]EVA.Impatient= (EVA event): The EVA event that will be
  triggered when a super weapon cameo is clicked but isn't ready to fire
  yet. EVA.Impatient=
:[SuperWeapon]EVA.InsufficientFunds= (EVA event): The EVA event that
  will be triggered when a super weapon can't be fired because the
  player doesn't have enough money. Defaults to `EVA_InsufficientFunds`.
  EVA.InsufficientFunds=


To disable an EVA event, use the value `none`. Custom EVA events.

.. versionadded:: 0.1



Messages
````````

:[SuperWeapon]Message.Detected= (CSF label): Message displayed to
  every player the moment the super weapon building is detected.
  Message.Detected=
:[SuperWeapon]Message.Ready= (CSF label): Message displayed to the
  firing player when the super weapon becomes ready to launch.
  Message.Ready=
:[SuperWeapon]Message.Launch= (CSF label): Message displayed to every
  player the moment the super weapon is launched. Message.Launch=
:[SuperWeapon]Message.Activate= (CSF label): Message displayed to
  every player the moment a deferrable super weapon is activated.
  Message.Activate=
:[SuperWeapon]Message.Abort= (CSF label): Message displayed to the
  firing player if the super weapon cannot be fired right now because
  another super weapon is active. Message.Abort=
:[SuperWeapon]Message.InsufficientFunds= (CSF label): Message
  displayed if the firing player doesn't have enough money to launch
  this super weapon. Message.InsufficientFunds=
:[SuperWeapon]Message.FirerColor= (boolean): Messages are displayed in
  the firing house's color scheme. Defaults to `no`. Message.FirerColor=
:[SuperWeapon]Message.Color= (Color scheme): If set, messages are
  always displayed in this color scheme instead of the player's color
  scheme. This is not respected if `Message.FirerColor=yes` is set.
  Message.Color=


.. versionadded:: 0.2



Cameo Overlay Texts
```````````````````

These texts will overlay the cameo in the sidebar to show the super
weapon's current status.

:[SuperWeapon]Text.Hold= (CSF label): Overlay displayed in case this
  super weapon is powered and can't currently charge because the
  building is shut down. Text.Hold=
:[SuperWeapon]Text.Ready= (CSF label): Overlay displayed in case this
  super weapon is fully charged and ready to be launched. Text.Ready=
:[SuperWeapon]Text.Charging= (CSF label): Overlay displayed in case
  this super weapon has `UseChargeDrain=yes` set and can be fired, but
  it isn't fully charged yet. Text.Charging=
:[SuperWeapon]Text.Active= (CSF label): Overlay displayed in case this
  super weapon has `UseChargeDrain=yes` set and is currently enabled and
  draining. Text.Active=
:[SuperWeapon]Text.Preparing= (CSF label): Overlay displayed in case
  none of the above texts are shown for this super weapon. That is, for
  example, charging for super weapons not using charge drain.
  Text.Preparing=


.. versionadded:: 0.2



Super Weapon Lighting
`````````````````````

The three major super weapons allow for a temporary change of
lighting. You can change any of these values without having to change
the others, too. If you want to use the scenario's respective default
value, use `-1` for ambient or colors.

:[SuperWeapon]Light.Enabled= (boolean): Whether the lighting gets
  respected or not. Currently only the primary super weapons support
  lighting changes. Light.Enabled=
:[SuperWeapon]Light.Ambient= (int): The brightness of the environment.
  Too high values will cause a slow-down. Light.Ambient=
:[SuperWeapon]Light.Red= (int): The red component of the lighting.
  Light.Red=
:[SuperWeapon]Light.Green= (int): The green component of the lighting.
  Light.Green=
:[SuperWeapon]Light.Blue= (int): The blue component of the lighting.
  Light.Blue=


.. versionadded:: 0.2



Enhanced Super Weapon Types
```````````````````````````



`Type=LightningStorm`
+++++++++++++++++++++

Default values for general tags:

:[SuperWeapon]SW.Range= (float,integer): Area around the target
  location the Lightning Storm strikes. Note that a single value denotes
  the diameter of a circle this is not the radius. Defaults to
  `[General]LightningCellSpread`.
:[SuperWeapon]SW.Damage= (integer): The damage each lightning bolt
  delivers. Defaults to `[General]LightningDamage`.
:[SuperWeapon]SW.Warhead= (Warhead): The warhead used to deal the
  damage of each lightning bolt. Defaults to
  `[General]LightningWarhead`.
:[SuperWeapon]SW.Deferment= (integer frames): Defaults to
  `[General]LightningDeferment`.
:[SuperWeapon]SW.ActivationSound= (Sound): Defaults to
  `[AudioVisual]StormSound`.
:[SuperWeapon]SW.AITargeting= (enum): Defaults to `LightningStorm`.
:[SuperWeapon]Light.*= (int): Default to the scenario's
  `[Lighting]Ion*`.


Lightning Storm specific tags:

:[SuperWeapon]Lightning.Duration= (integer frames): The length the
  Lightning Storm endures. A value of `-1` means indefinite duration.
  Defaults to `[General]LightningStormDuration`. Lightning.Duration=
:[SuperWeapon]Lightning.RadarOutage= (integer frames): The number of
  frames radars are jammed for players defined by `SW.AffectsHouse`.
  Defaults to `[General]LightningStormDuration`. Lightning.RadarOutage=
:[SuperWeapon]Lightning.RadarOutageAffects= (enum): Specifies the
  houses affected by radar outage. Defaults to `enemies`.
:[SuperWeapon]Lightning.HitDelay= (integer frames): The number of
  frames between two clouds being created over the target cell. Values
  of 0 or lower will disable direct hits. Clouds created by this
  mechanism are never subject to separation rules (see below). Defaults
  to `[General]LightningHitDelay`. Lightning.HitDelay=
:[SuperWeapon]Lightning.ScatterDelay= (integer frames): The number of
  frames between clouds getting created over a random cell in the super
  weapon's range. Values of 0 or lower will disable random hits. Only
  clouds created by this mechanism are subject to separation rules (see
  below). Defaults to `[General]LightningScatterDelay`.
  Lightning.ScatterDelay=
:[SuperWeapon]Lightning.ScatterCount= (integer): The number of new
  clouds created every `Lightning.ScatterDelay` frames. Values of 0 or
  lower will disable random hits. Defaults to `1`.
  Lightning.ScatterCount=
:[SuperWeapon]Lightning.Separation= (integer distance): The least
  number of cells between two random clouds to better distribute damage.
  This is not the direct distance, but rather the sum of the differences
  of the x and y components. Values of 0 or lower will disable
  separation rules. Defaults to `[General]LightningSeparation`.
  Lightning.Separation=
:[SuperWeapon]Lightning.PrintText= (boolean): Enables the warning text
  appearing shortly before the Lightning Storm strikes. Defaults to
  `[General]LightningPrintText`. Lightning.PrintText=
:[SuperWeapon]Lightning.IgnoreLightningRod= (boolean): Disables the
  special handling for buildings with `LightningRod=yes` set. Defaults
  to `no`. Lightning.IgnoreLightningRod=
:[SuperWeapon]Lightning.DebrisMin= (integer): The least number of
  debris created when lightning strikes empty cells or destroys a
  building or a unit. Defaults to `2`. Lightning.MinDebris=
:[SuperWeapon]Lightning.DebrisMax= (integer): The largest number of
  debris created when lightning strikes empty cells or destroys a
  building or a unit. Defaults to `4`. Lightning.MaxDebris=
:[SuperWeapon]Lightning.CloudHeight= (integer leptons): The height
  above the ground the clouds get created in. Values less than 0 will
  center the cloud image on top of the first bolt anim from the list
  (for the original game this is about 1200). Defaults to `-1`.
  Lightning.CloudHeight=
:[SuperWeapon]Lightning.BoltExplosion= (Animation): Every lightning
  bolt will display this damage animation upon impact. Defaults to
  `[General]WeatherConBoltExplosion`. Lightning.BoltExplosion=
:[SuperWeapon]Lightning.Sounds= (list of Sounds): A comma separated
  list of sounds played when lightning strikes. Defaults to
  `[AudioVisual]LightningSounds`. Lightning.Sounds=
:[SuperWeapon]Lightning.Clouds= (list of Animation): A comma separated
  list of cloud animations. If this list is empty, the Lightning Storm
  super weapon will not function. Defaults to
  `[General]WeatherConClouds`. Lightning.Clouds=
:[SuperWeapon]Lightning.Bolts= (list of Animation): A comma separated
  list of bolt animations. If this list is empty, the damage is caused
  even though no bolts are shown. Defaults to
  `[General]WeatherConBolts`. Lightning.Bolts=
:[SuperWeapon]Lightning.Debris= (list of Animation): A comma separated
  list of animations used as debris when lightning strikes. Defaults to
  `[General]MetallicDebris`. Lightning.Debris=


Other changes:

Lightning rods attract random lightning that is about to strike in
close range. For more information see the Lightning Rods section.

NB: Do not use `Bouncer=yes` animations with `Lightning.Bolts`. This
leads to crashes if a building is hit.

.. versionadded:: 0.2



`Type=MultiMissile`
+++++++++++++++++++

Default values for general tags:

:[SuperWeapon]SW.Damage= (integer): The damage the nuclear missile
  delivers. Negative values indicate to use the payload weapon's damage.
  Defaults to `-1`.
:[SuperWeapon]SW.Warhead= (Warhead): The warhead used to deal the
  damage of the nuke. If this is empty, the payload weapon's warhead
  will be used. Defaults to `none`.
:[SuperWeapon]SW.ActivationSound= (Sound): The nuke warn siren played
  at the destination. Defaults to `[AudioVisual]DigSound`.
:[SuperWeapon]SW.AITargeting= (enum): Defaults to `Nuke`.
:[SuperWeapon]Light.*= (int): Default to `Light.Ambient=200`,
  `Light.Red=175`, `Light.Green=150`, and `Light.Blue=125` respectively.


Nuclear missile specific tags:

:[SuperWeapon]Nuke.Payload= (Weapon): The Weapon used to display the
  downward-pointing nuke and as default, if `SW.Damage` and `SW.Warhead`
  aren't set. Defaults to `NukePayload`. Nuke.Payload=
:[SuperWeapon]Nuke.TakeOff= (Animation): The Animation played on the
  missile silo when the missile is launched. Defaults to
  `[General]NukeTakeOff`. Nuke.TakeOff=
:[SuperWeapon]Nuke.PsiWarning= (Animation): The Animation played at
  the nuke target, detectable by Psychic Sensors. Defaults to `PSIWARN`.
  Nuke.PsiWarning=
:[SuperWeapon]Nuke.SiloLaunch= (boolean): Whether this missile is
  launched from a building with `NukeSilo=yes` providing this super
  weapon. Otherwise the weapon defined by `Nuke.Payload` is created off-
  screen, aiming for the target cell. Defaults to `yes`.
  Nuke.SiloLaunch=


Other changes:

Use `WeaponType` to control the properties of the upward flying
animation (especially its `Projectile`). Ares respects the
`WeaponType` for every nuke, it will not use the `WeaponType` of the
first superweapon with `Type=Nuke` like Yuri's Revenge did. Also mind
to set `NukeMaker=yes` on the `WeaponType`, otherwise the nuke will
not come down again.

Ares supports multiple buildings with `NukeSilo=yes` providing this
super weapon. Yuri's Revenge only tried to find the first building
type that matched those criteria.

Yuri's Revenge supported the nuke impact animation only for the
warhead called `NUKE`, hardcoded to `NUKEBALL`. To change this
animation in Ares, have a look at PreImpactAnim.

.. versionadded:: 0.2



`Type=PsychicDominator`
+++++++++++++++++++++++

Default values for general tags:

:[SuperWeapon]SW.Range= (float,integer): Area around the target
  location the Psychic Dominator captures. This does not affect the
  damage. Defaults to `[General]DominatorCaptureRange`.
:[SuperWeapon]SW.Damage= (integer): The damage the Psychic Dominator
  delivers right before capturing. No damage is dealt if this value is
  null or negative. Defaults to `[General]DominatorDamage`.
:[SuperWeapon]SW.Warhead= (Warhead): The warhead used to deal the
  damage. Defaults to `[General]DominatorWarhead`.
:[SuperWeapon]SW.Deferment= (integer frames): Defaults to `0`.
:[SuperWeapon]SW.ActivationSound= (Sound): Defaults to
  `[AudioVisual]PsychicDominatorActivateSound`.
:[SuperWeapon]SW.AITargeting= (enum): Defaults to `PsychicDominator`.
:[SuperWeapon]SW.AffectsHouse= (enum): Specifies the houses affected
  by the capture. Defaults to `all`.
:[SuperWeapon]SW.AffectsTarget= (enum): Specifies which types the
  capture affects. Defaults to `infantry,units`.
:[SuperWeapon]Light.*= (int): Default to the scenario's
  `[Lighting]Dominator*`.


Psychic Dominator specific tags:

:[SuperWeapon]Dominator.FirstAnim= (Animation): The Animation hovering
  above the target for some time before the Psychic Dominator strikes.
  Defaults to `[General]DominatorFirstAnim`. Dominator.FirstAnim=
:[SuperWeapon]Dominator.FirstAnimHeight= (integer leptons): The height
  the `Dominator.FirstAnim` is played above the ground. Defaults to
  `750`. Dominator.FirstAnimHeight=
:[SuperWeapon]Dominator.SecondAnim= (Animation): The Animation
  hovering above the target when the Psychic Dominator strikes. Defaults
  to `[General]DominatorSecondAnim`. Dominator.SecondAnim=
:[SuperWeapon]Dominator.SecondAnimHeight= (integer leptons): The
  height the `Dominator.SecondAnim` is played above the ground. Defaults
  to `0`. Dominator.SecondAnimHeight=
:[SuperWeapon]Dominator.FireAtPercentage= (integer): After this
  percentage of the `Dominator.FirstAnim`'s frames have been played, the
  Dominator is fired. This is the actual percentage, `20` is 20%. Don't
  use decimal numbers. Defaults to `[General]DominatorFireAtPercentage`.
  Dominator.FireAtPercentage=
:[SuperWeapon]Dominator.ControlAnim= (Animation): The Animation
  displayed above unit being mind-controlled by the Dominator
  permanently. Defaults to `[CombatDamage]PermaControlledAnimationType`.
  Dominator.ControlAnim=
:[SuperWeapon]Dominator.Capture= (boolean): Defines whether this
  Psychic Dominator captures units in its range. Otherwise only the
  damage is dealt. Defaults to `yes`. Dominator.Captures=
:[SuperWeapon]Dominator.Ripple= (boolean): Defines whether this
  Psychic Dominator creates a ripple effect when the Psychic Dominator
  strikes. Defaults to `yes`. Dominator.Ripple=
:[SuperWeapon]Dominator.CaptureMindControlled= (boolean): Defines
  whether this Psychic Dominator can capture units that are mind-
  controlled already. Otherwise already mind-controlled units are
  ignored. Defaults to `yes`. Dominator.CaptureMindControlled=
:[SuperWeapon]Dominator.CapturePermaMindControlled= (boolean): Defines
  whether this Psychic Dominator can capture units that are permanently
  mind-controlled already. Otherwise already permanently mind-controlled
  units are ignored. Defaults to `yes`.
  Dominator.CapturePermaMindControlled=
:[SuperWeapon]Dominator.CaptureImmuneToPsionics= (boolean): Defines
  whether this Psychic Dominator can capture units that usually aren't
  mind-controllable. Setting this to `yes` ignores the
  `ImmuneToPsionics` tag on its victims. Defaults to `no`.
  Dominator.CaptureImmuneToPsionics=
:[SuperWeapon]Dominator.PermanentCapture= (boolean): Defines whether
  the victims are permanently mind-controlled. Setting this to `no`
  allows other mind-controllers to re-capture the victim, otherwise it
  will be uncapturable. Defaults to `yes`. Dominator.PermanentCapture=


.. versionadded:: 0.2



`Type=ChronoSphere`
+++++++++++++++++++

The `ChronoSphere` type super weapon needs a `ChronoWarp` type super
weapon. If you have more than one `ChronoSphere` super weapons, you
can use the same `ChronoWarp` super weapon for all of them or create
dedicated super weapons, if you want to. See SW.PostDependent.

Default values for general tags:

:[SuperWeapon]SW.Range= (float,integer): Range affected by the
  chronoshift. Defaults to `3,3`.
:[SuperWeapon]SW.Animation= (Animation): The placement animation
  indicating the source location for the chronoshift. Defaults to
  `[General]ChronoPlacement`.
:[SuperWeapon]SW.AnimationHeight= (integer): The height the
  `SW.Animation` is played above the ground. Defaults to `5`.
:[SuperWeapon]SW.AITargeting= (enum): Defaults to `none`. The AI
  cannot use this.
:[SuperWeapon]SW.AffectsHouse= (enum): Specifies the houses affected
  by the chronoshift. Defaults to `all`.
:[SuperWeapon]SW.AffectsTarget= (enum): Specifies which types the
  chronoshift affects. Defaults to `infantry,units`. Please note that
  buildings with `Chronoshift.IsVehicle=yes` are considered units and
  not buildings, if `Chronosphere.ReconsiderBuildings=yes`.
:[SuperWeapon]SW.PostDependent= (super weapon): Specifies the super
  weapon used to select the target cell for the chronoshift by ID.
  Defaults to the first `ChronoWarp` type super weapon in the
  `SuperWeaponTypes` list.


Chronosphere specific tags:

:[SuperWeapon]Chronosphere.BlastSrc= (Animation): The Animation played
  above the source when the chronoshift is started. Defaults to
  `[General]ChronoBlast`. Chronosphere.BlastSrc=
:[SuperWeapon]Chronosphere.BlastDest= (Animation): The Animation
  played above the destination when the chronoshift is started. Defaults
  to `[General]ChronoBlastDest`. Chronosphere.BlastDest=
:[SuperWeapon]Chronosphere.ReconsiderBuildings= (boolean): Defines
  whether the chronoshift will consider buildings with
  `Chronoshift.IsVehicle=yes` as vehicles instead. Otherwise deployed-
  vehicle type buildings always count as buildings like with the
  original Chronosphere. Defaults to `yes`.
  Chronosphere.ReconsiderBuildings=
:[SuperWeapon]Chronosphere.KillOrganic= (boolean): Defines whether the
  chronoshift will kill all organic units. Otherwise the units will not
  be killed by the chronoshift and teleport instead. Defaults to `yes`.
  Chronosphere.KillOrganic=
:[SuperWeapon]Chronosphere.KillTeleporters= (boolean): Defines whether
  the chronoshift will kill units with `Teleporter=yes` set. Otherwise
  the units will be chronoshifted. Defaults to `no`.
  Chronosphere.KillTeleporters=
:[SuperWeapon]Chronosphere.AffectsIronCurtain= (boolean): Defines
  whether the chronoshift will affect iron curtained units. Otherwise
  the units will be ignored. Defaults to `no`.
  Chronosphere.AffectsIronCurtain=
:[SuperWeapon]Chronosphere.AffectsUnwarpable= (boolean): Defines
  whether the chronoshift will affect units with `Warpable=no` set.
  Otherwise the units will be ignored. Defaults to `yes`.
  Chronosphere.AffectsUnwarpable=
:[SuperWeapon]Chronosphere.AffectsUndeployable= (boolean): Defines
  whether the chronoshift will affect buildings that can be undeployed
  into units again. Effectively, if a building is undeployable and this
  value is `yes`, `SW.AffectsTarget` and `Chronoshift.IsVehicle` are
  bypassed and the building is chronoshifted with vehicle placement
  rules. Defaults to `no`. Chronosphere.AffectsUndeployable=
:[SuperWeapon]Chronosphere.BlowUnplaceable= (boolean): Defines whether
  the chronoshift will destroy buildings that don't fit in the target
  location, otherwise the buildings will stay at the source location.
  This function will not spare units that have been deployed into
  buildings. Defaults to `yes`. Chronosphere.BlowUnplaceable=


Other changes:

It is now possible to chronoshift buildings. Note that there is a
difference to chronoporting units: If a building cannot be placed in
the target location it will blow up in the source location (if the
default `Chronosphere.BlowUnplaceable=yes` is used). Vehicle-type
buildings will try to find a fitting place just like units would.

See Chronoshift to prevent objects from being chronoshifted.

NB: There are several known issues with chronoshifting buildings that
haven't been fixed yet. For example, buildup animations will restart
and the turret facing is reset.

.. versionadded:: 0.2



`Type=ChronoWarp`
+++++++++++++++++

The `ChronoWarp` type super weapon is fired at the target location of
the chronoshift and marks the position the units will be teleported
to. If you have a `ChronoSphere` type super weapon you have to have
one `ChronoWarp` type super weapon, too.

From the `ChronoWarp` type super weapon only the targeting and cursor
properties are used, as well as `Range` to indicate the area of
effect.
For the actual chronoshifting tags, see ChronoSphere.
.. versionadded:: 0.2



`Type=IronCurtain` and `Type=ForceShield`
+++++++++++++++++++++++++++++++++++++++++

The difference between `Type=IronCurtain` and `Type=ForceShield` are
the default values used. `Type=ForceShield` will always use the force
shield protection color for buildings, otherwise the iron curtain
color is used.

Default values for general tags:

:[SuperWeapon]SW.Range= (float,integer): Range affected by the
  protection. Defaults to `[General]ForceShieldRadius` for
  `ForceShield`, `3,3` otherwise.
:[SuperWeapon]SW.Animation= (Animation): Defaults to
  `[General]ForceShieldInvokeAnim` for `ForceShield`,
  `[General]IronCurtainInvokeAnim` otherwise.
:[SuperWeapon]SW.AnimationHeight= (integer): The height the
  `SW.Animation` is played above the ground. Defaults to `5`.
:[SuperWeapon]SW.AITargeting= (enum): Defaults to `ForceShield` for
  `ForceShield`, `none` otherwise and the AI cannot use this.
:[SuperWeapon]SW.AffectsHouse= (enum): Specifies the houses affected
  by the protection. Defaults to `team` for `ForceShield`, `all`
  otherwise.
:[SuperWeapon]SW.AffectsTarget= (enum): Specifies which types the
  protection affects. Defaults to `buildings` for `ForceShield`, `all`
  otherwise.
:[SuperWeapon]SW.RequiresTarget= (enum): Specifies which types the
  protection can be fired upon. Defaults to `buildings` for
  `ForceShield`, `all` otherwise.
:[SuperWeapon]SW.RequiresHouse= (enum): Defaults to `team` for
  `ForceShield`, `none` otherwise.


Iron Curtain and Force Shield specific tags:

:[SuperWeapon]Protect.Duration= (integer frames): The length the
  protection effect endures. Defaults to `[General]ForceShieldDuration`
  for `ForceShield`, `[CombatDamage]IronCurtainDuration` otherwise.
  Protect.Duration=
:[SuperWeapon]Protect.PowerOutage= (integer frames): The length the
  owning player will expericence a power outage after firing this super
  weapon. Defaults to `[General]ForceShieldBlackoutDuration` for
  `ForceShield`, `0` otherwise. Protect.PowerOutage=
:[SuperWeapon]Protect.PlayFadeSoundTime= (integer frames): This many
  frames before the protection effect ends the
  `[SuperWeapon]SpecialSound` is played. Must be smaller than
  `Protect.Duration`. Defaults to
  `[General]ForceShieldPlayFadeSoundTime` for `ForceShield`, `0`
  otherwise. Protect.PlayFadeSoundTime=


.. versionadded:: 0.2



`Type=GeneticConverter`
+++++++++++++++++++++++

Default values for general tags:

:[SuperWeapon]SW.Range= (float,integer): The area the Genetic Mutator
  affects. Ignored if `Mutate.Explosion=yes`. Defaults to `3,3`.
:[SuperWeapon]SW.Damage= (integer): The damage the Genetic Mutator
  delivers if `Mutate.Explosion=yes`. Defaults to `10000`.
:[SuperWeapon]SW.Warhead= (Warhead): The warhead used to deal the
  damage. Defaults to `[SpecialWeapons]MutateExplosionWarhead` if
  `Mutate.Explosion=yes`, to `[SpecialWeapons]MutateWarhead` otherwise.
:[SuperWeapon]SW.Sound= (Sound): Defaults to
  `[AudioVisual]GeneticMutatorActivateSound`.
:[SuperWeapon]SW.AITargeting= (enum): Defaults to `GeneticMutator`.
:[SuperWeapon]SW.AffectsHouse= (enum): Specifies the houses affected
  by the mutation, if `Mutate.Explosion=no`. Defaults to `all`.
:[SuperWeapon]SW.AffectsTarget= (enum): Specifies whether the mutation
  effect should be limited to `land` or `water` targets. You cannot
  define any unit type here and they will be ignored. Ignored if
  `Mutate.Explosion=yes`. Defaults to `all`.


Genetic Mutator specific tags:

:[SuperWeapon]Mutate.Explosion= (boolean): Switches between two modes.
  If `yes`, the Genetic Mutator will cause an explosion using
  `SW.Warhad` and `SW.Damage` without respecting any other Genetic
  Mutator specific tags. Otherwise all infantry units in range are
  killed using `SW.Warhead`, verses and immunities are ignored. Defaults
  to `[General]MutateExplosion`. Mutate.Explosion=
:[SuperWeapon]Mutate.IgnoreCyborg= (boolean): Whether the Genetic
  Mutator will not affect infantry with `Cyborg=yes` set. Ignored if
  `Mutate.Explosion=yes`. Defaults to `no`. Mutate.IgnoreCyborg=
:[SuperWeapon]Mutate.IgnoreNotHuman= (boolean): Whether the Genetic
  Mutator will not affect infantry with `NotHuman=yes` set. Ignored if
  `Mutate.Explosion=yes`. Defaults to `no`. Mutate.IgnoreNotHuman=
:[SuperWeapon]Mutate.KillNatural= (boolean): Whether the Genetic
  Mutator will just kill infantry with `Natural=yes` set opposed to
  affecting it using `SW.Warhead`. Ignored if `Mutate.Explosion=yes`.
  Defaults to `yes`. Mutate.KillNatural=


.. versionadded:: 0.2



`Type=ParaDrop` and `Type=AmerParaDrop`
+++++++++++++++++++++++++++++++++++++++

Default values for general tags:

:[SuperWeapon]SW.AITargeting= (enum): Defaults to `ParaDrop`.


The original flags that control the units provided by the generic
paradrop super weapons ( `AllyParaDropInf`, `SovParaDropInf` and
`YuriParaDropInf`) and the American paradrop ( `AmerParaDropInf`) only
accept InfantryTypes. If you try to include a VehicleType via these
lists then the game will create a new InfantryType instead - with the
same parameters as the existing VehicleType - ultimately resulting in
an invisible InfantryType being delivered in the paradrop.

With Ares, there are new country-specific flags that override the old
flags and enhance the way paradrops are delivered. `ParaDrop.Types`
will accept VehicleTypes as well as InfantryTypes. You can send
multiple airplanes of user-defined type.

Each plane consists of the following properties:

:[SuperWeapon]ParaDrop.Types= (list of InfantryTypes and/or
  VehicleTypes): The units that will be paradropped by this super
  weapon. For `Type=AmerParaDrop` super weapons, this defaults to
  `AmerParaDropInf=`. NB: The original flags used to control the
  paradrop units only accept InfantryTypes. To include VehicleTypes in a
  paradrop you must use the new ParaDrop.Types and ParaDrop.Num flags.
  ParaDrop.Types=
:[SuperWeapon]ParaDrop.Num= (list of integers): The quantity of each
  corresponding unit (listed against ParaDrop.Types) that will be
  paradropped. For `Type=AmerParaDrop` super weapons, this defaults to
  `AmerParaDropNum=`. ParaDrop.Num=
:[SuperWeapon]ParaDrop.Aircraft= (AircraftType): The type of aircraft
  that will deliver the units. Defaults to the corresponding country's
  `ParaDrop.Aircraft=`. ParaDrop.Aircraft=
:[SuperWeapon]ParaDrop.Count= (integer - number of planes): This
  controls how many planes should be send to drop paratroopers. Defaults
  to `1`. ParaDrop.Count=


You can define every plane for each country, side or the super weapon
separately. The syntax is as follows:
`[Superweapon]Paradrop. *ID*.Plane *X*.*=`
*ID* is name of the country or side. *X* is a positive integer, with
no leading zeros, starting with *2* up to `Count`. To customize the
first plane (which will also act as the default plane), do not use the
*PlaneX* segment. If you want to set the default properties for all
sides, do not use the *ID* segment. Of course, the `Count` tags can't
have a *PlaneX* segment.

The Airplane and its contents will be read separately, thus just
defining the `Aircraft` will result in `Types` and `Nums` being read
from the next tag from this list (and vice versa). `Types` and `Nums`
have to be defined together; it is not possible to change the number
of units without restating the types.


#. `[Superweapon]Paradrop.Country.PlaneX.*=` (the SW's country-
   specific plane X)
#. `[Superweapon]Paradrop.Side.PlaneX.*=` (the SW's side-specific
   plane X)
#. `[Superweapon]Paradrop.PlaneX.*=` (the SW's default plane X)
#. `[Superweapon]Paradrop.Country.*=` (the SW's country-specific
   default plane)
#. `[Superweapon]Paradrop.Side.*=` (the SW's side-specific default
   plane)
#. `[Superweapon]Paradrop.*=` (the SW's default plane)
#. `[Country]Paradrop.*=` (the country-specific default plane)
#. `[Side]Paradrop.*=` (the side-specific default plane)
#. `[General]*=` (the Rules' default plane)


You can create unlimited new paradrop superweapons with different
properties. `Type=ParaDrop` and `Type=AmerParaDrop` are treated
equally, but they differ by the default values. The AI will use both
types as in the unmodified game.

.. versionadded:: 0.2



`Type=SpyPlane`
+++++++++++++++

Default values for general tags:

:[SuperWeapon]SW.AITargeting= (enum): Defaults to `ParaDrop`.


Spy Plane specific tags:

:[SuperWeapon]SpyPlane.Type= (AircraftType): The AircraftType that
  will be sent as a spy plane. Defaults to `SPYP`. SpyPlane.Type=
:[SuperWeapon]SpyPlane.Count= (integer): The number of spy planes to
  be sent out. Defaults to 1. SpyPlane.Count=
:[SuperWeapon]SpyPlane.Mission= (mission): The mission that the
  aircraft will be sent on (Guard, Attack, Move, etc). Defaults to
  SpyPlane_Approach. SpyPlane can now specify which AircraftType, how
  many, and what mission to perform. SpyPlane.Mission=


.. versionadded:: 0.1



`Type=PsychicReveal`
++++++++++++++++++++

Default values for general tags:

:[SuperWeapon]SW.Range= (float,integer): Range revealed by this super
  weapon. Defaults to `[CombatDamage]PsychicRevealRadius`. The default
  value is capped at 10, mimicking the original implementation using
  Cell Spread. To disable this limitation, set `SW.Range` explicitly.
:[SuperWeapon]SW.Sound= (Sound): Defaults to
  `[AudioVisual]PsychicRevealActivateSound`.
:[SuperWeapon]SW.AITargeting= (enum): Defaults to `ParaDrop`.


.. versionadded:: 0.2



New Super Weapon Types
``````````````````````



`Type=SonarPulse`
+++++++++++++++++

The Sonar Pulse is a variation of the original Sonar Pulse known from
Red Alert it will cause any cloaked units in range or on the entire
map to temporarily decloak. New super weapon type: SonarPulse (briefly
reveals cloaked units).

Default values for general tags:

:[SuperWeapon]SW.Range= (float,integer): The radius, in cells, that
  the decloak effect will be applied. Use negative values to reveal all
  units on the map. When using full-map sonar you don't have to select a
  target location, instead the super weapon will be fired when you click
  its cameo icon. Defaults to `10`.
:[SuperWeapon]SW.AITargeting= (enum): Defaults to `Stealth`.
:[SuperWeapon]SW.AffectsHouse= (enum): Specifies the houses affected
  by the sonar reveal. Defaults to `enemies`.
:[SuperWeapon]SW.AffectsTarget= (enum): Specifies which types the
  sonar affects. Defaults to `water`, all unit types situated on water
  cells.


Sonar Pulse specific tags:

:[SuperWeapon]SonarPulse.Delay= (integer frames): The duration that
  the decloak effect will last. Defaults to `60`. SonarPulse.Delay=


NB: If the affected unit gained its cloaking ability via
VeteranAbilities or EliteAbilities then it will only decloak for a
moment, as opposed to the full duration specified by the super weapon.

.. versionadded:: 0.1



`Type=GenericWarhead`
+++++++++++++++++++++

The Generic Warhead super weapon will detonate the specified warhead
at the target cell. New super weapon type: GenericWarhead (detonate
any warhead at target cell).

Default values for general tags:

:[SuperWeapon]SW.Damage= (integer): The amount of damage that will be
  dealt by the warhead.
:[SuperWeapon]SW.Warhead= (warhead): The warhead that will be
  detonated when in the target cell when the super weapon is fired. Note
  the warhead is detonated in a cell, not on a unit, so chances are you
  will want to set a `CellSpread` on the warhead to make sure the
  desired targets (especially InfantryTypes) are affected.
:[SuperWeapon]SW.AITargeting= (enum): Defaults to `Offensive`.

Don't forget that the BuildingType will need `DamageSelf=yes` set
(just like the Soviet Nuclear Missile Silo) if you want the warhead to
be capable of damaging the firing building.
.. versionadded:: 0.1



`Type=UnitDelivery`
+++++++++++++++++++

The Unit Delivery super weapon will create the specified unit(s) in
the target cell. This uses the CellSpread model to place the units.
New super weapon type: UnitDelivery (create unit(s) at target cell).

Default values for general tags:

:[SuperWeapon]SW.AITargeting= (enum): Defaults to `ParaDrop`.


Unit Delivery specific tags:

:[SuperWeapon]Deliver.Types= (list of TechnoTypes): The list of units
  that will be delivered. This works for infantry, vehicles, aircraft
  and buildings. Deliver.Types=
:[SuperWeapon]Deliver.Buildups= (boolean): Whether or not buildings
  delivered by this super weapon should play their buildup animation
  prior to becoming available. Deliver.Buildups=


All objects are placed on the ground, including aircraft. Flying units
that never land (e.g. the Rocketeer and Kirovs) will take off.
If a cell is occupied, the super weapon will retry on the next cell
and so on, until the object gets placed. Once the first unit is
placed, this process starts again for the next item in the list.
Infantry squads are grouped in a single cell. The search will skip an
item if it has not been placed after testing 100 cells.

You can mix in naval units and they will be placed where they can
normally exist.

If you have more than one building, the resulting placement might look
odd.

The actual delivery of the units happens all at once, on the 20th
frame after firing the super weapon. This delayed-effect logic will
most likely be customizable in future and so, in future, the delay for
this super weapon may default to a different amount.

.. versionadded:: 0.1


.. _firestorm:

`Type=Firestorm`
++++++++++++++++

This superweapon is a recreation of the Tiberian Sun Firestorm
superweapon.
When activated, all structures owned by the firing player that have
`Firestorm.Wall=yes` set will emit an energy field, blocking all
hostile projectiles (except those with `SubjectToFirestorm=no` set)
from passing through. The energy field also destroys any friend or foe
unlucky (or stupid) enough to come into direct contact with active
cells.

BuildingTypes with `Firestorm.Wall=yes` set will act as a section of
the Firestorm Wall and auto-connect to other nearby pieces (check the
original building's SHP from Tiberian Sun to see how the art is
controlled).

This Superweapon uses the old Charge-Drain logic: once activated, the
effect will persist for a duration determined by
`[General]ChargeToDrainRatio`, after which it will automatically shut
down and the superweapon will restart its charging process. Whilst the
effect is active you can click the super weapon button again to
manually deactivate it, thus allowing the recharge process to begin
earlier and finish faster. Refer to `ModEnc`_ for more information
about Charge-Drain logic.

In Tiberian Sun, the Charge-Drain feature was disableable through an
INI flag ( `[SuperWeapon]UseChargeDrain=no`) however: Ares forces this
logic to be used regardless of the value of that flag. Ares also
forces this super weapon to ignore its assigned `Action`, if any, as
this is required to make it activate from a single click of the
sidebar icon.

The AI will not use this super weapon.
NB: The animations used by this logic are temporarily hard-coded to
"FSIDLE", "FSGRND" and "FSAIR", as was used in Tiberian Sun.
NB: The AI has a lot of problems with targets behind an active
Firestorm Wall, although this should not be a major problem due to the
relatively small amount of game time that the Wall is active for.
Firestorm Wall Firestorm.Wall= SubjectToFirestorm=

.. versionadded:: 0.1



<<<SEPARATOR>>>

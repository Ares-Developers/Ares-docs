Super Weapons
~~~~~~~~~~~~~

In :game:`Yuri's Revenge`, there is very little you can do to change or add to
the existing super weapons - most super weapon-related features are hard-coded
to only work as designed for the original super weapons. Ares, however, includes
several new ways to customize existing super weapons as well as several wholly
new super weapons.

.. note:: You cannot change a super weapon's :tag:`Type=` or :tag:`Action=`
  values in any of the game mode specific INI files (like
  \ :file:`mpfreeforallmd.ini`) or map files. To achive the same effect, add a
  new super weapon to :file:`rulesmd.ini` with the different :tag:`Type=` or
  \ :tag:`Action=` and change :tag:`SuperWeapon=` for the respective owner
  buildings to use the new super weapon in the INI file instead.



Building Animations
```````````````````

Buildings can display specific animations for when the attached super weapon is
charging, is nearly charged (1 minute remaining in the normal game), is ready to
be fired, and when it fires. However, in :game:`Yuri's Revenge`, these
animations only work properly for the original super weapons. In :game:`Ares`,
these will work for any super weapon. Building animations played correctly for
new super weapons.

.. versionadded:: 0.1



General properties
``````````````````

:tagdef:`[SuperWeapon]SW.Range=float,int`
  Most superweapons having a ranged effect can take a float or two integers. One
  float is taken as radius around the target cell, two integers separated by
  comma denote a rectangular area. For example, :tag:`SW.Range=3.5` defines a
  circle with 7 cells diameter, :tag:`SW.Range=4,6` defines a rectangle 4 cells
  wide and 6 cells high. The range is no longer bound to cell spread's
  limitation of a maximum range of 10.
:tagdef:`[SuperWeapon]SW.CreateRadarEvent=bool`
  Creates a radar event rectangle for every player centered above the super
  weapon's target cell.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum none|owner|allies|team|enemies|all`
  Which houses items are affected by this super weapon. You can combine multiple
  values by comma. :value:`team` equals :value:`owner,allies`, :value:`all`
  equals :value:`owner,allies,enemies`. Defaults to :value:`team` for the Force
  Shield, to :value:`all` otherwise.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum land|water|empty|infantry|units|buildings`
  Which items are allowed to be affected by this super weapon. You can combine
  multiple values by comma. If you don't specify either land or water, both will
  be allowed. If you don't specify any of the other values, everything can be
  affected. For example, :tag:`SW.AffectsTarget=land,buildings` affects all
  buildings that aren't water-bound, :tag:`SW.AffectsTarget=water` affects every
  water cell, occupied or empty.
:tagdef:`[SuperWeapon]SW.ShowCameo=boolean`
  Sets whether this super weapon will appear in the side bar. This setting is
  ignored if :tag:`SW.AutoFire=no` is set. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]SW.Deferment=integer frames`
  The number of frames after the fired super weapon takes effect. Not all super
  weapons support deferment.

.. versionadded:: 0.1


.. _sw-postdependent:

Hardcoded Values
````````````````

It made no sense to have the values :tag:`PreClick`, :tag:`PostClick`, and
:tag:`PreDependent` customizable. :game:`Ares` hardcodes these values and they
have no effect any more. Instead, :tag:`SW.PostDependent` takes their place.

:tagdef:`[SuperWeapon]SW.PostDependent=SuperWeapon`
  The super weapon invoked right after firing this super weapon. As in
  :game:`Red Alert 2` the only super weapon using this is the ChronoSphere
  invoking the ChronoWarp. To distinguish between multiple of such super weapons
  you can provide the specific super weapon ID here. For example,
  :tag:`[ChronoSphereSpecial]SW.PostDependent=ChronoWarpSpecial` switches to the
  ChronoWarp type super weapon after you chose the source location.

.. index:: Super Weapons; PreClick, PostClick, and PreDependent are replaced by PostDependent.

.. versionadded:: 0.2



Targeting
`````````

:tagdef:`[SuperWeapon]SW.FireIntoShroud=boolean`
  Whether or not this super weapon is allowed to fire into an unexplored area of
  the map. Default is :value:`yes`.
:tagdef:`[SuperWeapon]SW.AutoFire=boolean`
  Sets whether this super weapon should be launched automatically even for human
  players. If this is set to :value:`yes`, the AI targeting options are used to
  infer the best target cell. Defaults to :value:`no`.
:tagdef:`[SuperWeapon]SW.ManualFire=boolean`
  Sets whether this super weapon can be manually fired by the owning player. If
  set to :value:`no`, the player will not be able to get a selection cursor for
  this super weapon when clicking the cameo. This setting is ignored if
  :tag:`SW.AutoFire=no` is set, because the player would have no way to fire
  this super weapon. You can use this on auto-firing super weapons where the
  targeting mode might prevents it from being fired (like the Lightning Storm
  or Psychic Dominator, if another super weapon of this type is currently
  active). Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]SW.RequiresTarget=enum land|water|empty|infantry|units|buildings`
  Which items this super weapon can fire upon. Hovering above an allowed item
  will show the :tag:`Cursor`, otherwise the player gets the :tag:`NoCursor` and
  it is not possible to launch the super weapon. For an example see
  :tag:`SW.AffectsTarget=`.
  
  .. note:: Please be aware of the problems that can arise if this and
    \ :tag:`SW.AffectsTarget=` are set to mutually exclusive values not allowing
    the super weapon to affect anything.
:tagdef:`[SuperWeapon]SW.RequiresHouse=enum none|owner|allies|team|enemies|all`
  Which house's items this super weapon can fire upon.
:tagdef:`[SuperWeapon]SW.AITargeting=enum SW Targeting Type`
  Select one of the following values to define how the AI will use this super
  weapon:

+ :value:`None`: The AI will not use this super weapon and it cannot auto-fire.
+ :value:`LightningStorm`: Targets offensively, but waits until a currently
  striking Lightning Storm subsides.
+ :value:`Nuke`: Targets offensively, or strikes the waypoint set by map
  triggers.
+ :value:`PsychicDominator`: Targets the largest group of enemy units.
+ :value:`GeneticMutator`: Targets the largest group of enemy infantry (in a 3x3
  area). 
+ :value:`ParaDrop`: Targets the least defended cell near the enemy base. 
+ :value:`ForceShield`: Targets the position an enemy super weapon is about to
  hit to protect against it.
+ :value:`NoTarget`: This super weapon doesn't need any valid coordinates to
  strike. You can use this for map-wide super weapons.
+ :value:`Offensive`: Targets offensively, without any special handling like
  :value:`LightningStorm` or :value:`Nuke`.
+ :value:`Stealth`: Targets stealth units or buildings only. Respects
  :value:`SW.RequiresTarget` and :value:`SW.RequiresHouse`.
+ :value:`Base`: Targets the owning player's base center.
+ :value:`Self`: Targets buildings providing this very super weapon, belonging
  to the owning player only.

.. note:: The AI will only respect :tag:`SW.AITargeting` when finding a target,
  if not noted otherwise. For example, this means :value:`Nuke` cannot be used
  to target allies only.

.. index:: Super Weapons; FireIntoShroud optional.

.. versionadded:: 0.2


.. _sw-cursors:

Cursors
```````

:game:`Ares` allows you to specify custom mouse cursors for the super weapon,
using the following flags:

:tagdef:`[SuperWeapon]Cursor.Frame=integer`
  Starting frame of the cursor from \ :file:`mouse.sha`. Defaults to the Attack
  cursor.
:tagdef:`[SuperWeapon]Cursor.Count=integer`
  Number of frames in the animated cursor.
:tagdef:`[SuperWeapon]Cursor.Interval=integer`
  How often to animate the cursor? Default is :value:`5`.
:tagdef:`[SuperWeapon]Cursor.MiniFrame=integer`
  Same as :tag:`Cursor.Frame`, except this is for the mouse cursor when
  positioned on the minimap.
:tagdef:`[SuperWeapon]Cursor.MiniCount=integer`
  Same as :tag:`Cursor.Count`, except this is for the mouse cursor when
  positioned on the minimap.
:tagdef:`[SuperWeapon]Cursor.HotSpot=HotSpot X, HotSpot Y`
  Specifies the coordinates on the cursor that are considered to be the 'tip'
  that is, the point from which the click event will handled. HotSpot X should
  be one of :value:`Left`, :value:`Center` or :value:`Right`. HotSpot Y should
  be one of :value:`Top`, :value:`Middle` or :value:`Bottom`. For example,
  :tag:`Cursor.HotSpot=Left,Top` will treat the top-left corner of the cursor as
  the tip. Default is :value:`Center,Middle`.


All of the above :tag:`Cursor.*` flags have a corresponding :tag:`NoCursor.*`
flag, which allows you to specify the cursor that will be displayed when the
mouse pointer is positioned over a point where the super weapon cannot be fired
(e.g. the Force Shield cannot be fired over empty ground, so will display an
alternate cursor to indicate this).

The :tag:`NoCursor.*` flags default to the same value as their :tag:`Cursor.*`
counterparts.

.. index:: Super Weapons; Custom SW Cursors.

.. versionadded:: 0.1


.. _charge-drain-sw:

Charge/Drain Super Weapons
``````````````````````````

Instead of one global setting, :value:`Ares` supports customizable
:tag:`ChargeToDrainRatio` settings for each super weapon. All settings here
only apply for super weapons with :tag:`UseChargeDrain=yes` set.

:tagdef:`[SuperWeapon]SW.ChargeToDrainRatio=float multiplier`
  The recharge time multiplied by this value is how long the super weapon will
  stay active. Must not be :value:`0`. Defaults to
  :tag:`[General]ChargeToDrainRatio`.
:tagdef:`[SuperWeapon]SW.Unstoppable=boolean`
  Whether this super weapon can be stopped when active. Otherwise clicks on the
  super weapon's cameo are ignored. Defaults to :value:`no`.

.. note:: Note that :tag:`UseChargeDrain` is supported for the Firewall super
  weapon only. Using it along with any other super weapon types it will lead to
  unexpected results.

.. index:: Super Weapons; Customizable charge to drain ratio for each superweapon.

.. versionadded:: 0.2



Cost
````

The firing of a super weapon can now add or subtract credits from the firing
player's cash reserve. If the player doesn't have enough funds the launch is
aborted and an EVA event is triggered to notify the player. Super weapons
costing money will show the needed amount in the super weapon's cameo tool tip.

:tagdef:`[SuperWeapon]Money.Amount=integer - credits`
  This many credits are added to the firing player's account when the super
  weapon is fired. Use a negative number to subtract credits. Defaults to
  :value:`0`.
:tagdef:`[SuperWeapon]Money.DrainAmount=integer - credits`
  This many credits are added to the firing player's account when a
  :tag:`UseChargeDrain=yes` super weapon is active. Use a negative number to
  subtract credits. Defaults to :value:`0`.
:tagdef:`[SuperWeapon]Money.DrainDelay=integer - frames`
  After this many frames the credits defined in :tag:`Money.DrainAmount=` are
  added to the firing player's account when a :tag:`UseChargeDrain=yes` super
  weapon is active. Defaults to :value:`0`.

.. index:: Super Weapons; Money deductable when firing a superweapon.

.. versionadded:: 0.1



Animation/Sound
```````````````

The default values depend on the super weapon's actual :tag:`Type`.

:tagdef:`[SuperWeapon]SW.Animation=animation`
  The animation to display at the super weapon's target cell.
:tagdef:`[SuperWeapon]SW.AnimationHeight=integer`
  How high above the target cell to display the animation.
:tagdef:`[SuperWeapon]SW.AnimationVisibility=enumeration none|owner|allies|team|enemies|all`
  Defines who will see this animation.
:tagdef:`[SuperWeapon]SW.Sound=sound`
  The sound to play at the super weapon's target cell.
:tagdef:`[SuperWeapon]SW.ActivationSound=sound`
  The sound to play when a Nuke is fired or a deferrable super weapon like the
  Lightning Storm is activated.

.. index:: Super Weapons; Custom animation played at target cell.

.. index:: Super Weapons; Custom SW animation visibility.

.. versionadded:: 0.1



EVA Events
``````````

:tagdef:`[SuperWeapon]EVA.Detected=EVA event`
  The EVA event that will be triggered when the super weapon building is
  constructed (the EVA event is not played for the owner of the building).
:tagdef:`[SuperWeapon]EVA.Ready=EVA event`
  The EVA event that will be triggered when the super weapon is ready to fire
  (the EVA event is only played for the owner of the super weapon).
:tagdef:`[SuperWeapon]EVA.Activated=EVA event`
  The EVA event that will be triggered when the super weapon is fired.
:tagdef:`[SuperWeapon]EVA.Impatient=EVA event`
  The EVA event that will be triggered when a super weapon cameo is clicked but
  isn't ready to fire yet.
:tagdef:`[SuperWeapon]EVA.InsufficientFunds=EVA event`
  The EVA event that will be triggered when a super weapon can't be fired
  because the player doesn't have enough money. Defaults to
  :value:`EVA_InsufficientFunds`.

To disable an EVA event, use the value :value:`none`.

.. index:: Super Weapons; Custom EVA events.

.. versionadded:: 0.1



Messages
````````

:tagdef:`[SuperWeapon]Message.Detected=CSF label`
  Message displayed to every player the moment the super weapon building is
  detected.
:tagdef:`[SuperWeapon]Message.Ready=CSF label`
  Message displayed to the firing player when the super weapon becomes ready to
  launch.
:tagdef:`[SuperWeapon]Message.Launch=CSF label`
  Message displayed to every player the moment the super weapon is launched.
:tagdef:`[SuperWeapon]Message.Activate=CSF label`
  Message displayed to every player the moment a deferrable super weapon is
  activated.
:tagdef:`[SuperWeapon]Message.Abort=CSF label`
  Message displayed to the firing player if the super weapon cannot be fired
  right now because another super weapon is active.
:tagdef:`[SuperWeapon]Message.InsufficientFunds=CSF label`
  Message displayed if the firing player doesn't have enough money to launch
  this super weapon.
:tagdef:`[SuperWeapon]Message.FirerColor=boolean`
  Messages are displayed in the firing house's color scheme. Defaults to
  :value:`no`.
:tagdef:`[SuperWeapon]Message.Color=Color scheme`
  If set, messages are always displayed in this color scheme instead of the
  player's color scheme. This is not respected if
  :value:`Message.FirerColor=yes` is set.


.. versionadded:: 0.2



Cameo Overlay Texts
```````````````````

These texts will overlay the cameo in the sidebar to show the super weapon's
current status.

:tagdef:`[SuperWeapon]Text.Hold=CSF label`
  Overlay displayed in case this super weapon is powered and can't currently
  charge because the building is shut down.
:tagdef:`[SuperWeapon]Text.Ready=CSF label`
  Overlay displayed in case this super weapon is fully charged and ready to be
  launched.
:tagdef:`[SuperWeapon]Text.Charging=CSF label`
  Overlay displayed in case this super weapon has :tag:`UseChargeDrain=yes` set
  and can be fired, but it isn't fully charged yet.
:tagdef:`[SuperWeapon]Text.Active=CSF label`
  Overlay displayed in case this super weapon has :tag:`UseChargeDrain=yes` set
  and is currently enabled and draining.
:tagdef:`[SuperWeapon]Text.Preparing=CSF label`
  Overlay displayed in case none of the above texts are shown for this super
  weapon. That is, for example, charging for super weapons not using charge
  drain.


.. versionadded:: 0.2



Super Weapon Lighting
`````````````````````

The three major super weapons allow for a temporary change of lighting. You can
change any of these values without having to change the others too. If you want
to use the scenario's respective default value, use :value:`-1` for ambient or
colors.

:tagdef:`[SuperWeapon]Light.Enabled=boolean`
  Whether the lighting gets respected or not. Currently only the primary super
  weapons support lighting changes.
:tagdef:`[SuperWeapon]Light.Ambient=integer`
  The brightness of the environment. Too high values will cause a slow-down.
:tagdef:`[SuperWeapon]Light.Red=integer`
  The red component of the lighting.
:tagdef:`[SuperWeapon]Light.Green=integer`
  The green component of the lighting.
:tagdef:`[SuperWeapon]Light.Blue=integer`
  The blue component of the lighting.


.. versionadded:: 0.2



Enhanced Super Weapon Types
```````````````````````````



:captiontag:`Type=LightningStorm`
+++++++++++++++++++++++++++++++++

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Area around the target location the Lightning Storm strikes. Note that a
  single value denotes the diameter of a circle - this is not the radius.
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
For more information see the :doc:`Lightning Rods </new/lightningrods>` section.

.. versionadded:: 0.2



:captiontag:`Type=MultiMissile`
+++++++++++++++++++++++++++++++

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Damage=integer`
  The damage the nuclear missile delivers. Negative values indicate to use the
  payload weapon's damage. Defaults to :value:`-1`.
:tagdef:`[SuperWeapon]SW.Warhead=Warhead`
  The warhead used to deal the damage of the nuke. If this is empty, the payload
  weapon's warhead will be used. Defaults to :value:`none`.
:tagdef:`[SuperWeapon]SW.ActivationSound=Sound`
  The nuke warn siren played at the destination. Defaults to
  :tag:`[AudioVisual]DigSound`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`Nuke`.
:tagdef:`[SuperWeapon]Light.*=integer`
  Default to :tag:`Light.Ambient=200`, :tag:`Light.Red=175`,
  :tag:`Light.Green=150`, and :tag:`Light.Blue=125` respectively.


Nuclear missile specific tags:

:tagdef:`[SuperWeapon]Nuke.Payload=Weapon`
  The Weapon used to display the downward-pointing nuke and as default, if
  :tag:`SW.Damage` and :tag:`SW.Warhead` aren't set. Defaults to
  :value:`NukePayload`.
:tagdef:`[SuperWeapon]Nuke.TakeOff=Animation`
  The Animation played on the missile silo when the missile is launched.
  Defaults to :tag:`[General]NukeTakeOff`.
:tagdef:`[SuperWeapon]Nuke.PsiWarning=Animation`
  The Animation played at the nuke target, detectable by Psychic Sensors.
  Defaults to :value:`PSIWARN`.
:tagdef:`[SuperWeapon]Nuke.SiloLaunch=boolean`
  Whether this missile is launched from a building with :tag:`NukeSilo=yes`
  providing this super weapon. Otherwise the weapon defined by
  :tag:`Nuke.Payload` is created off-screen, aiming for the target cell.
  Defaults to :value:`yes`.


Other changes:

Use :tag:`WeaponType` to control the properties of the upward flying animation
(especially its :tag:`Projectile`). :game:`Ares` respects the :tag:`WeaponType`
for every nuke, it will not use the :tag:`WeaponType` of the first superweapon
with :tag:`Type=Nuke` like :game:`Yuri's Revenge` did. Also mind to set
:tag:`NukeMaker=yes` on the :tag:`WeaponType`, otherwise the nuke will not come
down again.

:game:`Ares` supports multiple buildings with :tag:`NukeSilo=yes` providing this
super weapon. :game:`Yuri's Revenge` only tried to find the first building type
that matched those criteria.

:game:`Yuri's Revenge` supported the nuke impact animation only for the warhead
called :tag:`NUKE`, hardcoded to :tag:`NUKEBALL`. To change this animation in
:game:`Ares`, have a look at :ref:`PreImpactAnim <preimpactanim>`.

.. versionadded:: 0.2



:captiontag:`Type=PsychicDominator`
+++++++++++++++++++++++++++++++++++

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Area around the target location the Psychic Dominator captures. This does not
  affect the damage. Defaults to :tag:`[General]DominatorCaptureRange`.
:tagdef:`[SuperWeapon]SW.Damage=integer`
  The damage the Psychic Dominator delivers right before capturing. No damage is
  dealt if this value is 0 or negative. Defaults to
  :tag:`[General]DominatorDamage`.
:tagdef:`[SuperWeapon]SW.Warhead=Warhead`
  The warhead used to deal the damage. Defaults to
  :tag:`[General]DominatorWarhead`.
:tagdef:`[SuperWeapon]SW.Deferment=integer - frames`
  Defaults to :value:`0`.
:tagdef:`[SuperWeapon]SW.ActivationSound=Sound`
  Defaults to :tag:`[AudioVisual]PsychicDominatorActivateSound`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`PsychicDominator`.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum`
  Specifies the houses affected by the capture. Defaults to :value:`all`.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum`
  Specifies which types the capture affects. Defaults to
  :value:`infantry,units`.
:tagdef:`[SuperWeapon]Light.*=integer`
  Default to the scenario's :tag:`[Lighting]Dominator*`.


Psychic Dominator specific tags:

:tagdef:`[SuperWeapon]Dominator.FirstAnim=Animation`
  The Animation hovering above the target for some time before the Psychic
  Dominator strikes. Defaults to :tag:`[General]DominatorFirstAnim`.
:tagdef:`[SuperWeapon]Dominator.FirstAnimHeight=integer - leptons`
  The height the :tag:`Dominator.FirstAnim` is played above the ground. Defaults
  to :value:`750`.
:tagdef:`[SuperWeapon]Dominator.SecondAnim=Animation`
  The Animation hovering above the target when the Psychic Dominator strikes.
  Defaults to :tag:`[General]DominatorSecondAnim`.
:tagdef:`[SuperWeapon]Dominator.SecondAnimHeight=integer - leptons`
  The height the :tag:`Dominator.SecondAnim` is played above the ground.
  Defaults to :value:`0`.
:tagdef:`[SuperWeapon]Dominator.FireAtPercentage=integer`
  After this percentage of the :tag:`Dominator.FirstAnim`'s frames have been
  played, the Dominator is fired. This is the actual percentage, :value:`20` is
  20%. Don't use decimal numbers. Defaults to
  :tag:`[General]DominatorFireAtPercentage`.
:tagdef:`[SuperWeapon]Dominator.ControlAnim=Animation`
  The Animation displayed above units being mind-controlled by the Dominator
  permanently. Defaults to :tag:`[CombatDamage]PermaControlledAnimationType`.
:tagdef:`[SuperWeapon]Dominator.Capture=boolean`
  Defines whether this Psychic Dominator captures units in its range. Otherwise
  only the damage is dealt. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]Dominator.Ripple=boolean`
  Defines whether this Psychic Dominator creates a ripple effect when the
  Psychic Dominator strikes. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]Dominator.CaptureMindControlled=boolean`
  Defines whether this Psychic Dominator can capture units that are
  mind-controlled already. Otherwise already mind-controlled units are ignored.
  Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]Dominator.CapturePermaMindControlled=boolean`
  Defines whether this Psychic Dominator can capture units that are permanently
  mind-controlled already. Otherwise already permanently mind-controlled units
  are ignored. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]Dominator.CaptureImmuneToPsionics=boolean`
  Defines whether this Psychic Dominator can capture units that usually aren't
  mind-controllable. Setting this to :value:`yes` ignores the
  :tag:`ImmuneToPsionics` tag on its victims. Defaults to :value:`no`.
:tagdef:`[SuperWeapon]Dominator.PermanentCapture=boolean`
  Defines whether the victims are permanently mind-controlled. Setting this to
  :value:`no` allows other mind-controllers to re-capture the victim, otherwise
  it will be uncapturable. Defaults to :value:`yes`.


.. versionadded:: 0.2


.. _chronosphere:

:captiontag:`Type=ChronoSphere`
+++++++++++++++++++++++++++++++

The :value:`ChronoSphere` type super weapon needs a :value:`ChronoWarp` type
super weapon. If you have more than one :value:`ChronoSphere` super weapons, you
can reuse the same :value:`ChronoWarp` super weapon for all of them, or create
dedicated super weapons if you want to. See :ref:`SW.PostDependent
<sw-postdependent>`.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Range affected by the chronoshift. Defaults to :value:`3,3`.
:tagdef:`[SuperWeapon]SW.Animation=Animation`
  The placement animation indicating the source location for the chronoshift.
  Defaults to :tag:`[General]ChronoPlacement`.
:tagdef:`[SuperWeapon]SW.AnimationHeight=integer`
  The height the :tag:`SW.Animation` is played above the ground. Defaults to
  :value:`5`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`none`. The AI cannot use this.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum`
  Specifies the houses affected by the chronoshift. Defaults to :value:`all`.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum`
  Specifies which types the chronoshift affects. Defaults to
  :value:`infantry,units`.
  
  .. note:: Please note that buildings with :tag:`Chronoshift.IsVehicle=yes` are
    considered units and not buildings, if
    \ :tag:`Chronosphere.ReconsiderBuildings=yes` is set.
:tagdef:`[SuperWeapon]SW.PostDependent=super weapon`
  Specifies the super weapon used to select the target cell for the chronoshift
  by ID. Defaults to the first :value:`ChronoWarp` type super weapon in the
  :type:`SuperWeaponTypes` list.


Chronosphere specific tags:

:tagdef:`[SuperWeapon]Chronosphere.BlastSrc=Animation`
  The Animation played above the source when the chronoshift is started.
  Defaults to :tag:`[General]ChronoBlast`.
:tagdef:`[SuperWeapon]Chronosphere.BlastDest=Animation`
  The Animation played above the destination when the chronoshift is started.
  Defaults to :tag:`[General]ChronoBlastDest`.
:tagdef:`[SuperWeapon]Chronosphere.ReconsiderBuildings=boolean`
  Defines whether the chronoshift will consider buildings with
  :tag:`Chronoshift.IsVehicle=yes` as vehicles instead. Otherwise
  deployed-vehicle type buildings always count as buildings like with the
  original Chronosphere. Defaults to :value:`yes`.
:tagdef:`[SuperWeapon]Chronosphere.KillOrganic=boolean`
  Defines whether the chronoshift will kill all organic units. Otherwise the
  units will not be killed by the chronoshift and teleport instead. Defaults to
  :value:`yes`.
:tagdef:`[SuperWeapon]Chronosphere.KillTeleporters=boolean`
  Defines whether the chronoshift will kill units with :tag:`Teleporter=yes`
  set. Otherwise the units will be chronoshifted. Defaults to :value:`no`.
:tagdef:`[SuperWeapon]Chronosphere.AffectsIronCurtain=boolean`
  Defines whether the chronoshift will affect iron curtained units. Otherwise
  the units will be ignored. Defaults to :tag:`no`.
:tagdef:`[SuperWeapon]Chronosphere.AffectsUnwarpable=boolean`
  Defines whether the chronoshift will affect units with :tag:`Warpable=no` set.
  Otherwise the units will be ignored. Defaults to :tag:`yes`.
:tagdef:`[SuperWeapon]Chronosphere.AffectsUndeployable=boolean`
  Defines whether the chronoshift will affect buildings that can be undeployed
  into units again. Effectively, if a building has :tag:`UndeploysInto=` set and
  this value is :value:`yes`, :tag:`SW.AffectsTarget` and
  :tag:`Chronoshift.IsVehicle` are bypassed and the building is chronoshifted
  with vehicle placement rules. Defaults to :value:`no`.

  .. note:: "Undeployable" means *buildings that can undeploy*, rather than
    "vehicles that cannot deploy".

:tagdef:`[SuperWeapon]Chronosphere.BlowUnplaceable=boolean`
  Defines whether the chronoshift will destroy buildings that don't fit in the
  target location, otherwise the buildings will stay at the source location.
  This function will not spare units that have been deployed into buildings.
  Defaults to :value:`yes`.


Other changes:

It is now possible to chronoshift buildings. Note that there is a difference to
chronoporting units: If a building cannot be placed in the target location it
will blow up in the source location (if the default
:tag:`Chronosphere.BlowUnplaceable=yes` is used). Vehicle-type buildings will
try to find a fitting place just like units would.

See :doc:`Chronoshift </new/chronoshift>` to prevent objects from being
chronoshifted.

.. warning:: There are several known issues with chronoshifting buildings that
  haven't been fixed yet. For example, buildup animations will restart and the
  turret facing is reset.

.. versionadded:: 0.2



:captiontag:`Type=ChronoWarp`
+++++++++++++++++++++++++++++

The :tag:`ChronoWarp` type super weapon is fired at the target location of the
chronoshift and marks the position the units will be teleported to. If you have
a :value:`ChronoSphere` type super weapon you have to have one
:value:`ChronoWarp` type super weapon, too.

From the :value:`ChronoWarp` type super weapon only the targeting and cursor
properties are used, as well as :value:`Range` to indicate the area of effect by
drawing radial lines around the cursor. :tag:`SW.Range` is not used.

For the actual chronoshifting tags, see :ref:`ChronoSphere <chronosphere>`.

.. versionadded:: 0.2



:captiontag:`Type=IronCurtain` and :captiontag:`Type=ForceShield`
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The difference between :tag:`Type=IronCurtain` and :tag:`Type=ForceShield` are
the default values used. :tag:`Type=ForceShield` will always use the force
shield protection color for buildings, otherwise the iron curtain color is used.
At the moment, the color cannot be customized.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Range affected by the protection. Defaults to
  :tag:`[General]ForceShieldRadius` for :value:`ForceShield`, to :value:`3,3`
  otherwise.
:tagdef:`[SuperWeapon]SW.Animation=Animation`
  Defaults to :tag:`[General]ForceShieldInvokeAnim` for :value:`ForceShield`, to
  :tag:`[General]IronCurtainInvokeAnim` otherwise.
:tagdef:`[SuperWeapon]SW.AnimationHeight=integer`
  The height the :tag:`SW.Animation` is played above the ground. Defaults to
  :value:`5`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`ForceShield` for :value:`ForceShield`, to :value:`none`
  otherwise and the AI cannot use this.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum`
  Specifies the houses affected by the protection. Defaults to :value:`team` for
  :value:`ForceShield`, to :value:`all` otherwise.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum`
  Specifies which types the protection affects. Defaults to :value:`buildings`
  for :value:`ForceShield`, to :value:`all` otherwise.
:tagdef:`[SuperWeapon]SW.RequiresTarget=enum`
  Specifies which types the protection can be fired upon. Defaults to
  :value:`buildings` for :value:`ForceShield`, to :value:`all` otherwise.
:tagdef:`[SuperWeapon]SW.RequiresHouse=enum`
  Defaults to :value:`team` for :value:`ForceShield`, to :value:`none`
  otherwise.


Iron Curtain and Force Shield specific tags:

:tagdef:`[SuperWeapon]Protect.Duration=integer - frames`
  The length the protection effect endures. Defaults to
  :tag:`[General]ForceShieldDuration` for :value:`ForceShield`, to
  :tag:`[CombatDamage]IronCurtainDuration` otherwise.
:tagdef:`[SuperWeapon]Protect.PowerOutage=integer - frames`
  The length the owning player will expericence a power outage after firing this
  super weapon. Defaults to :tag:`[General]ForceShieldBlackoutDuration` for
  :value:`ForceShield`, to :value:`0` otherwise.
:tagdef:`[SuperWeapon]Protect.PlayFadeSoundTime=integer - frames`
  This many frames before the protection effect ends the
  :tag:`[SuperWeapon]SpecialSound` is played. Must be lower than
  :tag:`Protect.Duration`. Defaults to
  :tag:`[General]ForceShieldPlayFadeSoundTime` for :value:`ForceShield`, to
  :value:`0` otherwise.


.. versionadded:: 0.2



:captiontag:`Type=GeneticConverter`
+++++++++++++++++++++++++++++++++++

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  The area the Genetic Mutator affects. Ignored if :tag:`Mutate.Explosion=yes`.
  Defaults to :value:`3,3`.
:tagdef:`[SuperWeapon]SW.Damage=integer`
  The damage the Genetic Mutator delivers if :tag:`Mutate.Explosion=yes`.
  Defaults to :value:`10000`.
:tagdef:`[SuperWeapon]SW.Warhead=Warhead`
  The warhead used to deal the damage. Defaults to
  :tag:`[SpecialWeapons]MutateExplosionWarhead` if :tag:`Mutate.Explosion=yes`,
  to :tag:`[SpecialWeapons]MutateWarhead` otherwise.
:tagdef:`[SuperWeapon]SW.Sound=Sound`
  Defaults to :tag:`[AudioVisual]GeneticMutatorActivateSound`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`GeneticMutator`.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum`
  Specifies the houses affected by the mutation, if :tag:`Mutate.Explosion=no`.
  Defaults to :value:`all`.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum`
  Specifies whether the mutation effect should be limited to :value:`land` or
  :value:`water` targets. You cannot define any unit type here and they will be
  ignored. Ignored if :tag:`Mutate.Explosion=yes`. Defaults to :value:`all`.


Genetic Mutator specific tags:

:tagdef:`[SuperWeapon]Mutate.Explosion=boolean`
  Switches between two modes. If :value:`yes`, the Genetic Mutator will cause an
  explosion using :tag:`SW.Warhad` and :tag:`SW.Damage` without respecting any
  other Genetic Mutator specific tags. Otherwise all infantry units in range are
  killed using :tag:`SW.Warhead`, verses and immunities are ignored. Defaults to
  :tag:`[General]MutateExplosion`.
:tagdef:`[SuperWeapon]Mutate.IgnoreCyborg=boolean`
  Whether the Genetic Mutator will not affect infantry with :tag:`Cyborg=yes`
  set. Ignored if :tag:`Mutate.Explosion=yes`. Defaults to :value:`no`.
:tagdef:`[SuperWeapon]Mutate.IgnoreNotHuman=boolean`
  Whether the Genetic Mutator will not affect infantry with :tag:`NotHuman=yes`
  set. Ignored if :tag:`Mutate.Explosion=yes`. Defaults to :value:`no`.
:tagdef:`[SuperWeapon]Mutate.KillNatural=boolean`
  Whether the Genetic Mutator will just kill infantry with :tag:`Natural=yes`
  set opposed to affecting it using :tag:`SW.Warhead`. Ignored if
  :tag:`Mutate.Explosion=yes`. Defaults to :value:`yes`.


.. versionadded:: 0.2



:captiontag:`Type=ParaDrop` and :captiontag:`Type=AmerParaDrop`
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Default values for general tags:

:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`ParaDrop`.


The original flags that control the units provided by the generic paradrop super
weapons (:tag:`AllyParaDropInf`, :tag:`SovParaDropInf` and
:tag:`YuriParaDropInf`) and the American paradrop (:tag:`AmerParaDropInf`) only
accept :type:`InfantryTypes`. If you try to include a :type:`VehicleType` via
these lists then the game will create a new :type:`InfantryType` instead - with
the same parameters as the existing :type:`VehicleType` - ultimately resulting
in an invisible :type:`InfantryType` being delivered in the paradrop.

With :game:`Ares`, there are new country-specific flags that override the old
flags and enhance the way paradrops are delivered. :tag:`ParaDrop.Types` will
accept :type:`VehicleTypes` as well as :type:`InfantryTypes`. You can send
multiple airplanes of user-defined type.

Each plane consists of the following properties:

:tagdef:`[SuperWeapon]ParaDrop.Types=list of InfantryTypes and/or VehicleTypes`
  The units that will be paradropped by this super weapon. For
  :tag:`Type=AmerParaDrop` super weapons, this defaults to
  :tag:`AmerParaDropInf=`.

  .. note:: The original flags used to control the paradrop units only accept
    \ :type:`InfantryTypes`. To include :type:`VehicleTypes` in a paradrop you
    must use the new :tag:`ParaDrop.Types` and :tag:`ParaDrop.Num` flags.

:tagdef:`[SuperWeapon]ParaDrop.Num=list of integers`
  The quantity of each corresponding unit (listed against :tag:`ParaDrop.Types`)
  that will be paradropped. For :tag:`Type=AmerParaDrop` super weapons, this
  defaults to :tag:`AmerParaDropNum=`.
:tagdef:`[SuperWeapon]ParaDrop.Aircraft=AircraftType`
  The type of aircraft that will deliver the units. Defaults to the
  corresponding country's :tag:`ParaDrop.Aircraft=`.
:tagdef:`[SuperWeapon]ParaDrop.Count=integer - number of planes`
  This controls how many planes should be send to drop paratroopers. Defaults to
  :value:`1`.


You can define every plane for each country, side or the super weapon
separately. The syntax is as follows:

:tagdef:`[Superweapon]Paradrop.ID.PlaneX.*=`
  *ID* is name of the country or side. *X* is a positive integer, with no
  leading zeros, starting with *2* up to `Count`. To customize the first plane
  (which will also act as the default plane), do not use the *PlaneX* segment.
  If you want to set the default properties for all sides, do not use the *ID*
  segment. The :tag:`Count` tags can't have a *PlaneX* segment.

The Airplane and its contents will be read separately, thus it is possible to
only define :tag:`Aircraft`; :tag:`Types` and :tag:`Nums` will use the default
value by going though the list until the tags are defined. This also works vice
versa.

:tag:`Types` and :tag:`Nums` have to be defined together; it is not possible to
change the number of units without restating the types.

Values are read in this order, top down. The first value found is used.

#. :tag:`[Superweapon]Paradrop.Country.PlaneX.*=` (the SW's country-specific
   plane number X)
#. :tag:`[Superweapon]Paradrop.Side.PlaneX.*=` (the SW's side-specific plane
   number X)
#. :tag:`[Superweapon]Paradrop.PlaneX.*=` (the SW's default plane number X)
#. :tag:`[Superweapon]Paradrop.Country.*=` (the SW's country-specific default
   plane)
#. :tag:`[Superweapon]Paradrop.Side.*=` (the SW's side-specific default plane)
#. :tag:`[Superweapon]Paradrop.*=` (the SW's default plane)
#. :tag:`[Country]Paradrop.*=` (the country-specific default plane)
#. :tag:`[Side]Paradrop.*=` (the side-specific default plane)
#. :tag:`[General]*=` (the Rules' default plane)

Examples:

+ :tag:`[Superweapon]Paradrop.Russia.Plane3.Types=BORIS` (and proper
  :tag:`Nums`) would replace the contents of the third plane for the country
  :tag:`Russia`.

+ :tag:`[Superweapon]Paradrop.Nod.Aircraft=SPLANE` would replace the aircraft
  for all Soviet side countries.

.. quickstart:: \ To give all countries the same items, use
  \ :tag:`[Superweapon]Paradrop.Count=`, :tag:`[Superweapon]Paradrop.Aircraft=`,
  \ :tag:`[Superweapon]Paradrop.Types=`, and :tag:`[Superweapon]Paradrop.Num=`.
  This creates a clone of the American Paradrop.

You can create unlimited new paradrop superweapons with different properties.
:tag:`Type=ParaDrop` and :tag:`Type=AmerParaDrop` are treated equally, but they
differ by the default values. The AI will use both types as in the unmodified
game.

.. versionadded:: 0.2



:captiontag:`Type=SpyPlane`
+++++++++++++++++++++++++++

Default values for general tags:

:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`ParaDrop`.


Spy Plane specific tags:

:tagdef:`[SuperWeapon]SpyPlane.Type=AircraftType`
  The :type:`AircraftType` that will be sent as a spy plane. Defaults to
  :value:`SPYP`.
:tagdef:`[SuperWeapon]SpyPlane.Count=integer`
  The number of spy planes to be sent out. Defaults to :value:`1`.
:tagdef:`[SuperWeapon]SpyPlane.Mission=mission`
  The mission that the aircraft will be sent on (:value:`Guard`,
  :value:`Attack`, :value:`Move`, etc). Defaults to :value:`SpyPlane_Approach`.

.. index:: Super Weapons; SpyPlane can now specify which AircraftType, how many,
  and what mission to perform.


.. versionadded:: 0.1



:captiontag:`Type=PsychicReveal`
++++++++++++++++++++++++++++++++

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Range revealed by this super weapon. Defaults to
  :tag:`[CombatDamage]PsychicRevealRadius`. The default value is capped at 10,
  mimicking the original implementation using Cell Spread. To disable this
  limitation, set :tag:`SW.Range` explicitly.
:tagdef:`[SuperWeapon]SW.Sound=Sound`
  Defaults to :tag:`[AudioVisual]PsychicRevealActivateSound`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`ParaDrop`.


.. versionadded:: 0.2



New Super Weapon Types
``````````````````````



:captiontag:`Type=SonarPulse`
+++++++++++++++++++++++++++++

The Sonar Pulse is a variation of the original Sonar Pulse known from
Red Alert it will cause any cloaked units in range or on the entire
map to temporarily decloak. New super weapon type: SonarPulse (briefly
reveals cloaked units).

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  The radius, in cells, that the decloak effect will be applied. Use negative
  values to reveal all units on the map. When using full-map sonar you don't
  have to select a target location, instead the super weapon will be fired when
  you click its cameo icon. Defaults to :value:`10`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`Stealth`.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum`
  Specifies the houses affected by the sonar reveal. Defaults to
  :value:`enemies`.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum`
  Specifies which types the sonar affects. Defaults to :value:`water`, all unit
  types situated on water cells.


Sonar Pulse specific tags:

:tagdef:`[SuperWeapon]SonarPulse.Delay=integer - frames`
  The duration that the decloak effect will last. Defaults to :value:`60`.


.. note:: If the affected unit gained its cloaking ability via
  \ :tag:`VeteranAbilities` or :tag:`EliteAbilities` then it will only decloak
  for a moment, as opposed to the full duration specified by the super weapon.

.. versionadded:: 0.1



:captiontag:`Type=GenericWarhead`
+++++++++++++++++++++++++++++++++

The Generic Warhead super weapon will detonate the specified warhead at the
target cell.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Damage=integer`
  The amount of damage that will be dealt by the warhead.
:tagdef:`[SuperWeapon]SW.Warhead=warhead`
  The warhead that will be detonated when in the target cell when the super
  weapon is fired. Note the warhead is detonated in a cell, not on a unit, so
  chances are you will want to set a :tag:`CellSpread` on the warhead to make
  sure the desired targets (especially :type:`InfantryTypes`) are affected.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`Offensive`.

Don't forget that the :type:`BuildingType` will need :tag:`DamageSelf=yes` set
(just like the Soviet Nuclear Missile Silo) if you want the warhead to be
capable of damaging the firing building.

.. index:: Super Weapons; New super weapon type: GenericWarhead (detonate any
  warhead at target cell).

.. versionadded:: 0.1



:captiontag:`Type=UnitDelivery`
+++++++++++++++++++++++++++++++

The Unit Delivery super weapon will create the specified unit(s) in the target
cell. This uses the CellSpread model to place the units.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`ParaDrop`.


Unit Delivery specific tags:

:tagdef:`[SuperWeapon]Deliver.Types=list of TechnoTypes`
  The list of units that will be delivered. This works for infantry, vehicles,
  aircraft and buildings.
:tagdef:`[SuperWeapon]Deliver.Buildups=boolean`
  Whether or not buildings delivered by this super weapon should play their
  buildup animation prior to becoming available. Defaults to :value:`no`.


All objects are placed on the ground, including aircraft. Flying units that
never land (e.g. the Rocketeer and Kirovs) will take off. If a cell is occupied,
the super weapon will retry on the next cell and so on, until the object gets
placed. Once the first unit is placed, this process starts again for the next
item in the list. Infantry squads are grouped in a single cell. The search will
skip an item if it has not been placed after testing 100 cells.

You can mix in naval units and they will be placed where they can normally
exist.

If you have more than one building, the resulting placement might look
odd.

The actual delivery of the units happens all at once, on the 20th frame after
firing the super weapon. This delayed-effect logic will most likely be
customizable in future and so, in future, the delay for this super weapon may
default to a different amount.

.. index:: Super Weapons; New super weapon type: UnitDelivery (create unit(s) at
  target cell).

.. versionadded:: 0.1


.. _firestorm:

:captiontag:`Type=Firestorm`
++++++++++++++++++++++++++++

This superweapon is a recreation of the :game:`Tiberian Sun` Firestorm
superweapon.

When activated, all structures owned by the firing player that have
:tag:`Firestorm.Wall=yes` set will emit an energy field, blocking all hostile
projectiles (except those with :tag:`SubjectToFirestorm=no` set) from passing
through. The energy field also destroys any friend or foe unlucky (or stupid)
enough to come into direct contact with active cells.

:type:`BuildingTypes` with :tag:`Firestorm.Wall=yes` set will act as a section
of the Firestorm Wall and auto-connect to other nearby pieces (check the
original building's SHP from :game:`Tiberian Sun` to see how the art is
controlled).

This super weapon uses the old Charge/Drain logic: once activated, the effect
will persist for a duration determined by :tag:`SW.ChargeToDrainRatio`, after
which it will automatically shut down and the superweapon will restart its
charging process. Whilst the effect is active you can click the super weapon
button again to manually deactivate it, thus allowing the recharge process to
begin earlier and finish faster. See :ref:`Charge/Drain <charge-drain-sw>`.
Refer to `ModEnc <http://modenc.renegadeprojects.com/ChargeToDrainRatio>`_ for
more information about Charge/Drain logic.

In :game:`Tiberian Sun`, the Charge/Drain feature was disableable through an
INI flag (:tag:`[SuperWeapon]UseChargeDrain=no`) however: :game:`Ares` forces
this logic to be used regardless of the value of that flag. :game:`Ares` also
forces this super weapon to ignore its assigned :tag:`Action`, if any, as this
is required to make it activate from a single click of the sidebar icon.

The AI will not use this super weapon.

.. note:: The animations used by this logic are temporarily hard-coded to
  \ :value:`FSIDLE`, :value:`FSGRND` and :value:`FSAIR`, as was used in
  \ :game:`Tiberian Sun`.

.. note:: The AI has a lot of problems with targets behind an active Firestorm
  Wall, although this should not be a major problem due to the relatively small
  amount of game time that the Wall is active for.

.. index:: Super Weapons; Firestorm Wall

.. versionadded:: 0.1

Targeting
`````````

.. index:: Super Weapons; Customize valid targets.


General Settings
----------------

These settings allow to enable AI targeting even for human players.

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

.. versionadded:: 0.2


Manual Target Selection
-----------------------

These settings only apply to human players.

:tagdef:`[SuperWeapon]SW.FireIntoShroud=boolean`
  Whether or not this super weapon is allowed to fire into an unexplored area of
  the map. Default is :value:`yes`.

:tagdef:`[SuperWeapon]SW.RequiresTarget=enum none|land|water|empty|infantry|units|buildings`
  Which items this super weapon can fire upon. Hovering above an allowed item
  will show the :tag:`Cursor`, otherwise the player gets the :tag:`NoCursor` and
  it is not possible to launch the super weapon. For an example see
  :tag:`SW.AffectsTarget=`.
  
  .. note:: Please be aware of the problems that can arise if this and
    \ :tag:`SW.AffectsTarget=` are set to mutually exclusive values not allowing
    the super weapon to affect anything.

:tagdef:`[SuperWeapon]SW.RequiresHouse=enum none|owner|allies|team|enemies|all`
  Which house's items this super weapon can fire upon.

.. index:: Super Weapons; FireIntoShroud optional.

.. versionadded:: 0.2


Automatic Target Selection
--------------------------

Define the way the AI selects eligible targets to fire the super weapon at.

:tagdef:`[SuperWeapon]SW.AITargeting=enum SW Targeting Type`
  Select one of the following values to define how the AI will use this super
  weapon:

+ :value:`None`: The AI will not use this super weapon and it cannot auto-fire.
+ :value:`LightningStorm`: Targets offensively, but waits until a currently
  striking Lightning Storm subsides. Supports map action 135.
+ :value:`Nuke`: Targets offensively, or strikes the waypoint set by map
  triggers. Supports map action 135.
+ :value:`PsychicDominator`: Targets the largest group of enemy units. Supports
  map action 135.
+ :value:`GeneticMutator`: Targets the largest group of enemy infantry (in a 3x3
  area). Supports map action 135.
+ :value:`ParaDrop`: Targets the least defended cell near the enemy base.
  Supports map action 135.
+ :value:`ForceShield`: Targets the position an enemy super weapon is about to
  hit to protect against it. Supports map action 140.
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

.. versionadded:: 0.2

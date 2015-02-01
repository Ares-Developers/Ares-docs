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

+ :value:`None`

  Does not fire. Effectively disables this super weapon for the AI.

+ :value:`Nuke`

  Selects a valid target using the Ion Cannon rules or picks a target by
  preferred type. Ignores cloaked targets.

+ :value:`LightningStorm`

  Selects a valid target using the Ion Cannon rules or picks a target by
  preferred type. Ignores cloaked targets. Cannot fire when a Lightning Storm is
  currently active.

+ :value:`PsychicDominator`

  Selects the valid target that has the most enemy units in Cell Spread range 3
  nearby that can be permanently mind-controlled. Does not fire if a preferred
  target cell is set. Ignores cloaked targets.

+ :value:`GeneticMutator`

  Selects the valid target that has the most enemy infantry units in Cell Spread
  range 1 nearby. Does not fire if a preferred target cell is set. Ignores
  cloaked targets.

+ :value:`ForceShield`

  Fires at the position the last super weapon with :tag:`AIDefendAgainst=yes`
  was fired at. This honors the :tag:`AISuperDefense` tags, and not all super
  weapons might be defended against.

+ :value:`ParaDrop`

  Searches for a free area of 5 by 5 cells close to the favorite enemy player's
  base center. If the owner has not settled for a favorite enemy yet, tries to
  find a location around the owning player's base center.

+ :value:`Offensive`

  Selects a valid target using the Ion Cannon rules. Ignores cloaked targets.

+ :value:`MultiMissile`

  Selects a valid target by looking at the summed :tag:`ThreatPosed` values of
  the area around them. For cloaked targets, a random value between 0 and 100 is
  used.

+ :value:`HunterSeeker`

  Fires at no target, but only if the owning player settled for a favorite
  enemy. This is only useful with certain super weapons, or when a super weapon
  has a full map effect.

+ :value:`NoTarget`

  Fires at no target. This is only useful with certain super weapons, or when a
  super weapon has a full map effect.

+ :value:`Stealth`

  Selects a valid target using the Ion Cannon rules. Only considers cloaked
  targets.

+ :value:`Self`

  Selects a building owned by the firing player which provides this super weapon
  and satisfies power requirements. The target is the center of the building.

+ :value:`Base`

  Fires at what the game considers the firing player's base center.

+ :value:`EnemyBase`

  Fires at what the game considers the base center of the firing player's
  favorite enemy.


:tagdef:`[SuperWeapon]SW.AIRequiresTarget=enum none|land|water|empty|infantry|units|buildings|all`
  Specifies which targets will be considered eligible by AI players or human
  owned automatically fired super weapons. The default value depends on the
  :tag:`SW.AITargeting` setting. See the table below.

:tagdef:`[SuperWeapon]SW.AIRequiresHouse=enum owner|allies|team|enemies|others|all`
  Specifies which houses will be considered eligible by AI players or human
  owned automatically fired super weapons. The default value depends on the
  :tag:`SW.AITargeting` setting. See the table below.

.. versionadded:: 0.2

.. versionchanged:: 0.9


Mechanisms
----------

There are several mechanisms to select a target, but three of them are notable,
because they are recurring.

The **Ion Cannon targeting** rules assigns each valid object a value, which is
determined by the :tag:`[General]AIIonCannon...` tags. A target is picked
randomly from all objects with the highest score.

The **base center** is determined by the game and updated whenever a player
builds or loses buildings. The base center can be manually set and cleared using
map actions 137 and 138 respectively.

The **preferred target by type** is set by map action 35. The game looks at the
first team on them map owned by the firing player and has the team leader
acquire a target of the preferred type. A value of :value:`1` means to use the
special firing behavior, which usually is Ion Cannon targeting or base center
selection. 

.. note:: Currently, :game:`Ares` does not support preferred types other than
  \ :value:`1`. The super weapons might not check ranges, designators, and
  inhibitors, and fire regardless of any restriction.


Defaults
--------

The following table lists the defaults for the AI targeting tags depending on
the mode, as well as some general properties.

**Requires Enemy** means that this targeting mode will only select a target
automatically if the house has settled for a favorite enemy player. This is
usually determined when a player is attacked. Without a favorite enemy, the
super weapon will not fire.

The **Preference** is overriding the actual targeting. Offensive targets are set
using the map action 135. Defensive targets are set using map action 140. As
long as these overrides are set, the super weapons will prefer these targets.
Super weapons might also hold and stop firing as long as an override is set.
They will resume once the override is cleared using the corresponding map
action.

Most targeting modes support the new **extra** features added by :game:`Ares`.
That is maximum and minimum ranges, designators and inhibitors. Note that if a
preferred target type is set using map action 35, they are not checked.

+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :tag:`SW.AITargeting`     | :tag:`SW.AIRequiresTarget`        | :tag:`SW.AIRequiresHouse` | Requires Enemy         | Preference             | Extras    |
+===========================+===================================+===========================+========================+========================+===========+
| :value:`None`             | N/A                               | N/A                       | N/A                    | N/A                    | N/A       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`Nuke`             | :value:`infantry,units,buildings` | :value:`enemies`          | yes                    | offensive              | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`LightningStorm`   | :value:`infantry,units,buildings` | :value:`enemies`          | yes                    | offensive              | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`PsychicDominator` | :value:`infantry,units`           | :value:`all`              | yes                    | hold if offensive      | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`GeneticMutator`   | :value:`infantry`                 | :value:`all`              | no                     | hold if offensive      | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`ForceShield`      | do not use                        | do not use                | no                     | defensive              | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`ParaDrop`         | do not use                        | do not use                | no                     | offensive, base center | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`Offensive`        | :value:`infantry,units,buildings` | :value:`enemies`          | yes                    | nothing                | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`MultiMissile`     | :value:`buildings`                | :value:`none`             | yes                    | offensive              | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`HunterSeeker`     | N/A                               | N/A                       | yes                    | nothing                | no        |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`NoTarget`         | N/A                               | N/A                       | no                     | nothing                | no        |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`Stealth`          | :value:`infantry,units,buildings` | :value:`enemies`          | no                     | nothing                | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`Self`             | :value:`none`\ 1)                 | do not use                | no                     | nothing                | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`Base`             | do not use                        | do not use                | no                     | base center            | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+
| :value:`EnemyBase`        | do not use                        | do not use                | yes                    | base center            | yes       |
+---------------------------+-----------------------------------+---------------------------+------------------------+------------------------+-----------+

If you define the :tag:`SW.AIRequiresTarget` or :tag:`SW.AIRequiresHouse` when
the table says *do not use*, you might render the super weapon unable to fire.

\ 1) :value:`Self` always only checks buildings owned by the owning player. You
can only use :value:`land`, :value:`water`, and :value:`none` here. All other
values are invalid.

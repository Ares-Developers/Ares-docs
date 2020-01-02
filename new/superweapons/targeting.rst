Targeting
`````````

.. index:: Super Weapons; Customize valid targets.


.. index:: Super Weapons; Auto-firing using AI rules

General Settings
----------------

These settings allow enabling AI targeting even for human players.

:tagdef:`[SuperWeapon]SW.UseAITargeting=boolean`
  Whether AI targeting will decide the target used when firing this super
  weapon. If :value:`yes`, clicking the cameo will not allow manual target
  selection and instead fire the super weapon at an automatically determined
  location. Defaults to :value:`no`.

  All applicable AI targeting constraints have to be satisfied for the super
  weapon to fire and actually discharge. If the constraints are not satisfied,
  the cameo will be darkened. If the player tries to fire the super weapon
  anyhow, the message :tag:`Message.CannotFire` is displayed.

:tagdef:`[SuperWeapon]SW.AutoFire=boolean`
  Sets whether this super weapon will be launched automatically once ready even
  for human players. If set to :value:`yes`, the AI targeting options are used
  to infer the target cell. Defaults to :value:`no`.

:tagdef:`[SuperWeapon]SW.ManualFire=boolean`
  Sets whether this super weapon can be manually fired by the owning player. If
  set to :value:`no`, the player will not be able to get a selection cursor for
  this super weapon when clicking the cameo. This setting is ignored if
  :tag:`SW.AutoFire=no` is set, because the player would have no way to fire
  this super weapon. Defaults to :value:`yes`.

  .. note:: You can use this on auto-firing super weapons where the targeting
    mode might prevent it from being fired (like the Lightning Storm or Psychic
    Dominator, if another super weapon of this type is currently active).

.. versionadded:: 0.2
.. versionchanged:: 3.0


.. index::
  Super Weapons; Fire into shroud made optional

Manual Target Selection
-----------------------

These settings only apply to human players.

:tagdef:`[SuperWeapon]SW.FireIntoShroud=boolean`
  Whether or not this super weapon is allowed to fire into an unexplored area of
  the map. Default is :value:`yes`.

:tagdef:`[SuperWeapon]SW.RequiresTarget=enumeration none|land|water|empty|infantry|units|buildings`
  Which items this super weapon can fire at. Hovering above an allowed item will
  show the :tag:`Cursor`, otherwise the player gets the :tag:`NoCursor` and it
  is not possible to launch the super weapon. For an example see
  :tag:`SW.AffectsTarget=`.
  
  .. note:: Please be aware of the problems that can arise if this and
    \ :tag:`SW.AffectsTarget=` are set to mutually exclusive values not allowing
    the super weapon to affect anything.

:tagdef:`[SuperWeapon]SW.RequiresHouse=enumeration none|owner|allies|team|enemies|all`
  Which house's items this super weapon can fire at.

.. versionadded:: 0.2


.. index::
  Super Weapons; Automatic targeting rules
  Super Weapons; List of AI Targeting Modes
  AI; Super weapon target selection

Automatic Target Selection
--------------------------

Define the way the AI selects eligible targets to fire the super weapon at.

:tagdef:`[SuperWeapon]SW.AITargeting=enumeration SW Targeting Type`
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

+ :value:`IronCurtain`

  Will not fire automatically. Instead, will wait for a team script requesting
  an Iron Curtain with matching :tag:`SW.Group`.

+ :value:`ForceShield`

  Fires at the position the last super weapon with :tag:`AIDefendAgainst=yes`
  was fired at. This honors the :tag:`AISuperDefense` tags, and not all super
  weapons might be defended against.

+ :value:`ParaDrop`

  Searches for a free area of 5 by 5 cells close to the favorite enemy player's
  base center. If the owner has not settled for a favorite enemy yet, tries to
  find a location around the owning player's base center.

+ :value:`DropPod`

  Fires at a randomly chosen land cell in one of the four outer sectors around
  the owning player's base center.

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

+ :value:`Attack`

  Fires like :value:`NoTarget` when the last attack on a building was recent.

+ :value:`LowPower`

  Fires to the same cell as :value:`NoTarget` when the owning house has
  insufficient power.

+ :value:`LowPowerAttack`

  Fires like :value:`LowPower`, but only if the last attack on a building was
  recent. This can be used to activate auxiliary power or to force-overcharge
  base defenses.

+ :value:`LightningRandom`

  Targets a random cell no matter its contents, and is not otherwise constrained
  except for checking Designators and Inhibitors.


:tagdef:`[SuperWeapon]SW.AIRequiresTarget=enumeration none|land|water|empty|infantry|units|buildings|all`
  Specifies which targets will be considered eligible by AI players or human
  owned automatically fired super weapons. The default value depends on the
  :tag:`SW.AITargeting` setting. See the table below.

:tagdef:`[SuperWeapon]SW.AIRequiresHouse=enumeration owner|allies|team|enemies|others|all`
  Specifies which houses will be considered eligible by AI players or human
  owned automatically fired super weapons. The default value depends on the
  :tag:`SW.AITargeting` setting. See the table below.

:tagdef:`[SuperWeapon]SW.AITargeting.Constraints=enumeration SW Targeting Constraints`
  A comma-separated list of constraints that all have to be satisfied for the
  super weapon to fire. Defaults depend on the :tag:`Type=`.

+ :value:`None`

  No constraint.

+ :value:`Enemy`

  This targeting mode will only select a target automatically if the house has
  settled for a favorite enemy player. This is usually determined when a player
  is attacked. Without a favorite enemy, the super weapon will not fire.

+ :value:`Offensive_Cell_Set`

  Requires the offensive cell to be set by Map Action 135. In combination with
  the :value:`offensive` preference, can be used to create user-triggered super
  weapons at a location the mapper decides.

+ :value:`Offensive_Cell_Clear`

  Requires the offensive cell to be not set by Map Action 135.

+ :value:`Defensive_Cell_Set`

  Requires the defensive cell to be set by Map Action 140. In combination with
  the :value:`defensive` preference, can be used to create user-triggered super
  weapons at a location the mapper decides.

+ :value:`Defensive_Cell_Clear`

  Requires the defensive cell to be not set by Map Action 140.

+ :value:`LightningStorm_Inactive`

  Satisfied if there currently is no Lightning Storm manifesting or active. This
  constraint does not apply to human players manually firing the super weapon.

+ :value:`Dominator_Inactive`

  Satisfied if there currently is no Psychic Dominator active. This constraint
  does not apply to human players manually firing the super weapon.

+ :value:`Attacked`

  Satisfied if the firing house has been attacked recently. This constraint does
  not apply to human players manually firing the super weapon.

+ :value:`LowPower`

  Satisfied if the firing house currently has low power. This constraint does
  not apply to human players manually firing the super weapon.


:tagdef:`[SuperWeapon]SW.AITargeting.Preference=enumeration SW Targeting Preference`
  The preference overrides the actual targeting. As long as these overrides are
  set, the super weapons will prefer these set targets. Defaults depend on the
  :tag:`Type=`.

+ :value:`None`

  No preference.

+ :value:`Offensive`

  Use the the offensive cell if set by Map Action 135. Use Map Action 136 to
  clear the offensive cell.

+ :value:`Defensive`

  Use the the defensive cell if set by Map Action 140. Use Map Action 141 to
  clear the defensive cell.

.. versionadded:: 0.2
.. versionchanged:: 3.0


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
first team on the map owned by the firing player and has the team leader acquire
a target of the preferred type. A value of :value:`1` means to use the special
firing behavior, which usually is Ion Cannon targeting or base center selection. 

.. note:: Currently, :game:`Ares` does not support preferred types other than
  \ :value:`1`. The super weapons might not check ranges, designators, and
  inhibitors, and fire regardless of any restriction.


Defaults
--------

The following table lists the defaults for the AI targeting tags depending on
:tag:`SW.AITargeting`, as well as some general properties that affect targeting.

Note that the defaults used depend on the super weapon's :tag:`Type`, and the
type always takes precedence. See the specific super weapon type documentation
for the actual values. If no specific value is given, the value from this table
is used.

Most targeting modes support the new **extra** features added by :game:`Ares`.
That is maximum and minimum ranges, designators and inhibitors. Note that if a
preferred target type is set using map action 35, they are not checked.

+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :tag:`SW.AITargeting`     | :tag:`SW.AIRequiresTarget`        | :tag:`SW.AIRequiresHouse` | :tag:`SW.AITargeting.Constraints`                      | :tag:`SW.AITargeting.Preference`| Extras    |
+===========================+===================================+===========================+========================================================+=================================+===========+
| :value:`None`             | N/A                               | N/A                       | :value:`none`                                          | :value:`none`                   | N/A       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`Nuke`             | :value:`infantry,units,buildings` | :value:`enemies`          | :value:`enemy`                                         | :value:`offensive`              | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`LightningStorm`   | :value:`infantry,units,buildings` | :value:`enemies`          | :value:`enemy,lightningstorm_inactive`                 | :value:`offensive`              | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`PsychicDominator` | :value:`infantry,units`           | :value:`all`              | :value:`enemy,dominator_inactive,offensive_cell_clear` | :value:`none`                   | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`GeneticMutator`   | :value:`infantry`                 | :value:`all`              | :value:`offensive_cell_clear`                          | :value:`none`                   | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`IronCurtain`      | do not use                        | do not use                | :value:`none`                                          | :value:`none`                   | no        |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`ForceShield`      | do not use                        | do not use                | :value:`none`                                          | :value:`defensive`              | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`ParaDrop`         | do not use                        | do not use                | :value:`none`                                          | :value:`offensive`              | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`DropPod`          | do not use                        | do not use                | :value:`enemy`                                         | :value:`none`                   | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`Offensive`        | :value:`infantry,units,buildings` | :value:`enemies`          | :value:`enemy`                                         | :value:`none`                   | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`MultiMissile`     | :value:`buildings`                | :value:`none`             | :value:`enemy`                                         | :value:`offensive`              | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`HunterSeeker`     | N/A                               | N/A                       | :value:`enemy`                                         | N/A                             | no        |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`NoTarget`         | N/A                               | N/A                       | :value:`none`                                          | N/A                             | no        |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`Stealth`          | :value:`infantry,units,buildings` | :value:`enemies`          | :value:`none`                                          | :value:`none`                   | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`Self`             | :value:`none`\ 1)                 | do not use                | :value:`none`                                          | :value:`none`                   | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`Base`             | do not use                        | do not use                | :value:`none`                                          | :value:`none`                   | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`EnemyBase`        | do not use                        | do not use                | :value:`enemy`                                         | :value:`none`                   | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+
| :value:`LightningRandom`  | N/A                               | N/A                       | :value:`none`                                          | :value:`none`                   | yes       |
+---------------------------+-----------------------------------+---------------------------+--------------------------------------------------------+---------------------------------+-----------+

If you define the :tag:`SW.AIRequiresTarget` or :tag:`SW.AIRequiresHouse` when
the table says *do not use*, you might render the super weapon unable to fire.

\ 1) :value:`Self` always only checks buildings owned by the owning player. You
can only use :value:`land`, :value:`water`, and :value:`none` here. All other
values are invalid.

.. warning:: If a targeting mode is constrained to require (:value:`enemy`), the
  targeting mode might not work if this constraint is not defined. For example,
  if the mode by design only considers the buildings owned by the favorite
  enemy, there's nothing to chose from, thus no target can be picked.

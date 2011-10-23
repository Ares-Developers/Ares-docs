Warheads
~~~~~~~~



Iron Curtain Effect
```````````````````

The Iron Curtain effect can now be given to or removed from units and
buildings using new Ares warhead settings. Weapons can apply or remove
the Iron Curtain effect for a specified number of frames (stackable or
absolute).

:[Warhead]IronCurtain.Duration= (integer): If positive, endows the
  target unit with the Iron Curtain effect for the specified number of
  frames. If negative, the Iron Curtain effect duration will be reduced
  by this number of frames. Use `IronCurtain.Cap=` below to have the
  effect duration be cumulative rather than absolute.
  `IronCurtain.Duration` defaults to `0` (no Iron Curtain effect).
  IronCurtain.Duration= :[Warhead]IronCurtain.Cap= (integer): If this
  value is negative the `IronCurtain.Duration` is absolute and will not
  stack up if a target is fired upon multiple times. If this value is
  `0` the effect duration can stack up indefinitely. Otherwise the Iron
  Curtain effect can not stack up to durations longer than this value
  except for when a unit's duration already is higher and
  `IronCurtain.Duration` isn't negative (the duration will not be
  decreased, then). `IronCurtain.Cap` defaults to `-1` (non-stacking,
  absolute duration). IronCurtain.Cap=




To change the effect the Iron Curtain has on specific units:

:[TechnoType]IronCurtain.Modifier= (multiplier): If the Iron Curtain
  effect duration is positive it will be multiplied by this factor. Use
  `0%` to create a unit that can not be affected by the Iron Curtain.
  `IronCurtain.Modifier` defaults to `100%`. IronCurtain.Modifier=


Quickstart: To have a unit protect a target for ten seconds, set
[Warhead]IronCurtain.Duration=150 . To allow the Iron Curtain duration
to stack up to one minute, set [Warhead]IronCurtain.Cap=900 . To
remove the Iron Curtain effect altogether, set
[Warhead]IronCurtain.Duration=-1 and [Warhead]IronCurtain.Cap=0
(remove one frame but have the resulting number of frames not exceed
0).

If a weapon deals conventional damage and applies the Iron Curtain at
the same time, the damage will be dealt first. InfantryTypes and
`Organic=yes` units will always get killed instantaneously.

This feature works with `CellSpread` to affect multiple targets.
`AffectsAllies` and `AffectsEnemies` are respected. A unit does not
get the Iron Curtain effect if `Verses` is equal to `0%`, otherwise
the target is endowed with the full effect.

.. versionadded:: 0.1



Permanent Mind-Control
``````````````````````

:[Warhead]MindControl.Permanent= (boolean): If the warhead has
  `MindControl.Permanent=yes` set as well as `MindControl=yes` set then
  the mind-control will be permanent. MindControl.Permanent=



.. versionadded:: 0.1

Permanent mind-control is handled in the same way as the Psychic
Dominator effect previously-mind-controlled units (even permanently)
are re-mind-controlled, and the mind-controller does not have a limit
on the number of units that it can permanently mind-control.

Unlike the Psychic Dominator, buildings are susceptible to permanent
mind-control if the warhead can target them. Permanent mind-control
weapons.

.. versionadded:: 0.1



Customizable WarpAway
`````````````````````

If `[Warhead]Temporal.WarpAway` is set, it specifies the animation to
be played when this warhead erases an object, instead of
`[General]WarpAway=`. Per-weapon WarpAway animation.
Temporal.WarpAway=

.. versionadded:: 0.1



Ion Cannon Ripple Effect
````````````````````````

:[Warhead]Ripple.Radius= (integer, scale unknown): This generates a
  visual shockwave when the warhead detonates, identical to the one
  produced by Tiberian Sun's Ion Cannon. It is recommended that you
  don't set Radius above 79. Note that this is a visual effect only. Ion
  Cannon ripple effect for weapons. Ripple.Radius=
NB: Below are listed some results of modifying the tag values.
  Ripple.Radius=1 - Forget it, nothing. 5 - Target cell, only voxel
  rippling 8 - Target cell, both voxel and SHP rippling. 10 - 1 cell
  radius 15 - 2 cell radius 20 - 3 cell radius 25 - 3 cell radius 28 - 3
  cell unit-rippling, 4 cell terrain rippling radius 30 and onwards - 3
  cell unit-rippling, 5 cell terrain-rippling radius


.. versionadded:: 0.1



Deployed Infantry Damage multiplier
```````````````````````````````````

:[Warhead]Deployed.Damage= (float - multiplier): A multiplier applied
  to `Damage` if the InfantryType receiving it is currently deployed.
  Deployed.Damage=


Note that this is not the same as the existing `ProneDamage=` flag;
deployed units are not considered to be prone. Defaults to 100%. Per-
warhead damage multiplier against deployed infantry.

.. versionadded:: 0.1



AffectsEnemies
``````````````

:[Warhead]AffectsEnemies= (boolean): Specifies whether or not this
  warhead can damage enemy units. This has no effect on the warhead's
  ability to target enemy units. A counterpart to the existing
  `AffectsAllies` flag. `AffectsEnemies=` flag added (counterpart for
  AffectsAllies=). AffectsEnemies=


.. versionadded:: 0.1



Non-Malicious Warheads
``````````````````````

:[Warhead]Malicious= (boolean): Specifies whether or not EVA should
  notify a ore miner's owner of an attack ( `EVA_OreMinerUnderAttack`).
  No other EVA messages are suppressed. For example, if a warhead's
  purpose is to spread ore dealing damage as a side effect only you can
  use `Malicious=no` to disable unreasonable EVA attack warnings for ore
  miners. Defaults to `yes`. `Malicious=` warhead flag suppresses EVA's
  *ore miner under attack* warnings. Malicious=


.. versionadded:: 0.2



InfDeathAnim
````````````

:[Warhead]InfDeathAnim= (string, animation ID): Specifies the
  animation to display when an InfantryType (with `NotHuman=no`) is
  killed by this warhead. Works in the same way as existing `InfDeath`
  animations except this flag allows you to specify an animation ID
  rather than an integer. Further more, the animation will be treated as
  the correct type (e.g. mutation or non-mutation) automatically, which
  means that you can now have any number of mutations that produce
  player-owned InfantryTypes. See MakeInfantryOwner for how to control
  which player will gain control of 'mutated' infantry. New InfDeaths
  (InfDeathAnim= any animation, auto-detect mutation). InfDeathAnim=


.. versionadded:: 0.1



PreImpactAnim
`````````````

In Yuri's Revenge the nuke uses a special animation called `NUKEBALL`
which was shown prior to displaying the actual mushroom explosion and
dealing damage. The game was hard-coded to use this only for warheads
with the ID `NUKE`. Ares enables this for arbitrary warheads.
`PreImpactAnim=` optional for every warhead, not just for `NUKE`.

:[Warhead]PreImpactAnim= (string, animation ID): Specifies the
  animation to display when a projectile which uses this warhead
  impacts. After the animation is over, the actual explosion is created
  and damage is dealt. The animation may not be looping. Defaults to
  `NUKEBALL` for `NUKE`, otherwise to `none`. PreImpactAnim=


.. versionadded:: 0.2



<<<SEPARATOR>>>

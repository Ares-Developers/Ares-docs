Warheads
~~~~~~~~



Iron Curtain Effect
```````````````````

The Iron Curtain effect can now be given to or removed from units and buildings
using new :game:`Ares` warhead settings.

.. index:: Warheads; Weapons can apply or remove the Iron Curtain effect for a
  specified number of frames (stackable or absolute).

:tagdef:`[Warhead]IronCurtain.Duration=integer - frames`
  If positive, endows the target unit with the Iron Curtain effect for the
  specified number of frames. If negative, the Iron Curtain effect duration will
  be reduced by this number of frames. Use :tag:`IronCurtain.Cap=` below to have
  the effect duration be cumulative rather than absolute.
  :tag:`IronCurtain.Duration` defaults to :value:`0` (no Iron Curtain effect).
:tagdef:`[Warhead]IronCurtain.Cap=integer`
  If this value is negative the :tag:`IronCurtain.Duration` is absolute and will
  not stack up if a target is fired upon multiple times. If this value is
  :value:`0` the effect duration can stack up indefinitely. Otherwise the Iron
  Curtain effect can not stack up to durations longer than this value except for
  when a unit's duration already is higher and :tag:`IronCurtain.Duration` isn't
  negative (the duration will not be decreased, then). :tag:`IronCurtain.Cap`
  defaults to :value:`-1` (non-stacking, absolute duration).


To change the effect the Iron Curtain has on specific units:

:tagdef:`[TechnoType]IronCurtain.Modifier=float - multiplier`
  If the Iron Curtain effect duration is positive it will be multiplied by this
  factor. Use :value:`0%` to create a unit that can not be affected by the Iron
  Curtain. :tag:`IronCurtain.Modifier` defaults to :value:`100%`.

.. quickstart:: To have a unit protect a target for ten seconds, set
  \ :tag:`[Warhead]IronCurtain.Duration=150`. To allow the Iron Curtain duration
  to stack up to one minute, set :tag:`[Warhead]IronCurtain.Cap=900`. To remove
  the Iron Curtain effect altogether, set
  :tag:`[Warhead]IronCurtain.Duration=-1` and
  :tag:`[Warhead]IronCurtain.Cap=0` (remove one frame but have the resulting
  number of frames not exceed 0).

If a weapon deals conventional damage and applies the Iron Curtain at the same
time, the damage will be dealt first. :type:`InfantryTypes` and
:tag:`Organic=yes` units will always get killed instantaneously.

This feature works with :tag:`CellSpread` to affect multiple targets.
:tag:`AffectsAllies` and :tag:`AffectsEnemies` are respected. A unit does not
get the Iron Curtain effect if :tag:`Verses` is equal to :value:`0%`, otherwise
the target is endowed with the full effect.

.. versionadded:: 0.1



Permanent Mind-Control
``````````````````````

:tagdef:`[Warhead]MindControl.Permanent=boolean`
  If the warhead has :tag:`MindControl.Permanent=yes` set as well as
  :tag:`MindControl=yes` set then the mind-control will be permanent.

.. versionadded:: 0.1

Permanent mind-control is handled in the same way as the Psychic Dominator
effect previously-mind-controlled units (even permanently) are
re-mind-controlled, and the mind-controller does not have a limit on the number
of units that it can permanently mind-control.

Unlike the Psychic Dominator, buildings are susceptible to permanent
mind-control if the warhead can target them. Permanent mind-control weapons.

.. versionadded:: 0.1



Customizable :captiontag:`WarpAway`
```````````````````````````````````

If :tag:`[Warhead]Temporal.WarpAway` is set, it specifies the animation to be
played when this warhead erases an object, instead of :tag:`[General]WarpAway=`.

.. index:: Warheads; Per-weapon WarpAway animation.

.. versionadded:: 0.1



Ion Cannon Ripple Effect
````````````````````````

:tagdef:`[Warhead]Ripple.Radius=integer, scale unknown`
  This generates a visual shockwave when the warhead detonates, identical to the
  one produced by :game:`Tiberian Sun`'s Ion Cannon. It is recommended that you
  don't set Radius above 79. Note that this is a visual effect only.

  Below are listed some results of modifying the tag values.

  + :tag:`Ripple.Radius=1` - Forget it, nothing.
  + :tag:`Ripple.Radius=5` - Target cell, only voxel rippling
  + :tag:`Ripple.Radius=8` - Target cell, both voxel and SHP rippling.
  + :tag:`Ripple.Radius=10` - 1 cell radius
  + :tag:`Ripple.Radius=15` - 2 cell radius
  + :tag:`Ripple.Radius=20` - 3 cell radius
  + :tag:`Ripple.Radius=25` - 3 cell radius
  + :tag:`Ripple.Radius=28` - 3 cell unit-rippling, 4 cell terrain rippling
    radius
  + :tag:`Ripple.Radius=30` and onwards - 3 cell unit-rippling, 5 cell
    terrain-rippling radius

.. index:: Warheads; Ion Cannon ripple effect for weapons.

.. versionadded:: 0.1



Deployed Infantry Damage multiplier
```````````````````````````````````

:tagdef:`[Warhead]Damage.Deployed=float - multiplier`
  A multiplier applied to :tag:`Damage` if the :type:`InfantryType` receiving it
  is currently deployed.


Note that this is not the same as the existing :tag:`ProneDamage=` flag;
deployed units are not considered to be prone. Defaults to :value:`100%`.

.. index:: Warheads; Per-warhead damage multiplier against deployed infantry.

.. versionadded:: 0.1



:captiontag:`AffectsEnemies`
````````````````````````````

:tagdef:`[Warhead]AffectsEnemies=boolean`
  Specifies whether or not this warhead can damage enemy units. This has no
  effect on the warhead's ability to target enemy units. A counterpart to the
  existing :tag:`AffectsAllies` flag.

.. index:: AffectsEnemies= flag added (counterpart for AffectsAllies=).

.. versionadded:: 0.1



Non-Malicious Warheads
``````````````````````

:tagdef:`[Warhead]Malicious=boolean`
  Specifies whether or not EVA should notify a ore miner's owner of an attack
  (:value:`EVA_OreMinerUnderAttack`). No other EVA messages are suppressed. For
  example, if a warhead's purpose is to spread ore dealing damage as a side
  effect only you can use :tag:`Malicious=no` to disable unreasonable EVA attack
  warnings for ore miners. Defaults to :value:`yes`.

.. index:: Warheads; Malicious= warhead flag suppresses EVA's *ore miner under
  attack* warnings.

.. versionadded:: 0.2



:captiontag:`InfDeathAnim`
``````````````````````````

:tagdef:`[Warhead]InfDeathAnim=string, animation ID`
  Specifies the animation to display when an :type:`InfantryType` (with
  :tag:`NotHuman=no`) is killed by this warhead. Works in the same way as
  existing :tag:`InfDeath` animations except this flag allows you to specify an
  animation ID rather than an integer. Further more, the animation will be
  treated as the correct type (e.g. mutation or non-mutation) automatically,
  which means that you can now have any number of mutations that produce
  player-owned :tag:`InfantryTypes`. See :doc:`MakeInfantryOwner
  </new/makeinfantryowner>` for how to control which player will gain control of
  'mutated' infantry.

  .. index:: Warheads; New InfDeaths (InfDeathAnim= any animation, auto-detect mutation).

.. versionadded:: 0.1

.. _preimpactanim:

:captiontag:`PreImpactAnim`
```````````````````````````

In :game:`Yuri's Revenge` the nuke uses a special animation called
:tag:`NUKEBALL` which was shown prior to displaying the actual mushroom
explosion and dealing damage. The game was hard-coded to use this only for
warheads with the ID :tag:`NUKE`. :game:`Ares` enables this for arbitrary
warheads.

.. index:: Warheads; PreImpactAnim= optional for every warhead, not just for NUKE.

:tagdef:`[Warhead]PreImpactAnim=string, animation ID`
  Specifies the animation to display when a projectile which uses this warhead
  impacts. After the animation is over, the actual explosion is created and
  damage is dealt. The animation may not be looping. Defaults to
  :value:`NUKEBALL` for :tag:`NUKE`, otherwise to :value:`none`.

.. versionadded:: 0.2

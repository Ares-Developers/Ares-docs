Iron Curtain
````````````

.. _wh-ironcurtain:

Iron Curtain Effect
-------------------

The Iron Curtain effect can now be given to or removed from units and buildings
using new :game:`Ares` warhead settings.

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
  Curtain effect can not stack up to durations longer than this value -- except
  for when a unit's duration already is higher and :tag:`IronCurtain.Duration`
  isn't negative (the duration will not be decreased, then).
  :tag:`IronCurtain.Cap` defaults to :value:`-1` (non-stacking, absolute duration).


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

.. index:: Warheads; Weapons can apply or remove the Iron Curtain effect for a
  specified number of frames (stackable or absolute).

.. versionadded:: 0.1


Iron Curtain Flash
------------------

With these two tags the combat lights created when protected objects are hit can
be turned off.

:tagdef:`[AudioVisual]IronCurtainFlash=boolean`
  Whether units and structures will by default emit a black or blue flash when
  hit while under the effect of an Iron Curtain or Force Shield respectively.
  Defaults to :value:`yes`.

:tagdef:`[Warhead]IronCurtain.Flash=boolean`
  Whether units and structures will emit a black or blue flash when hit with
  this warhead while under the effect of an Iron Curtain or Force Shield
  respectively. Defaults to :tag:`[AudioVisual]IronCurtainFlash`.

.. index:: Warheads; Disable the combat light flash on Iron Curtained objects

.. versionadded:: 0.D

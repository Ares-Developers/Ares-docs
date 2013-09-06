AttachEffect
~~~~~~~~~~~~

.. warning:: This documentation is preliminary. Please report factual errors.
  There is still time to change it, and to add examples for some interesting use
  cases.

The AttachEffect system was designed as a spiritual successor to
:game:`NPatch`'s Upgrade logic, but it was aimed to not be limited only to
superweapons. AttachEffect tags can be applied to both the Big Four (all
:type:`TechnoTypes`) and Warheads, unless stated otherwise.

.. note:: The state of AttachEffects on units does not update while in a
  transport, while under a temporal effect and so on. In this matter, they
  behave like IvanBombs.

.. quickstart:: To create a healing/repairing or residual damage effect, attach
  an animation with appropriate :tag:`Warhead` and :tag:`Damage` settings. This
  will affect the target unit for the entire duration of the AttachEffect,
  applying damage using the animation damage mechanism.

:tagdef:`[Section]AttachEffect.Animation=AnimationType`
  The optional animation to play on the affected unit. The animation is attached
  to the unit and moves along with it. Defaults to :value:`none`.

  The animation is removed when the unit is cloaked. The animation is recreated
  once the unit is uncloaked again. While cloaked, the AttachEffect is still
  applied, but the effects caused by the animation are not.

  .. note:: The animation always loops until the effect subsides.
    \ :tag:`LoopCount` is ignored.

:tagdef:`[Section]AttachEffect.Duration=integer`
  The duration of the effect in frames. Use :value:`-1` for infinite duration.
  Defaults to :value:`0`.

:tagdef:`[Section]AttachEffect.TemporalHidesAnim=boolean`
  Whether a :type:`TechnoType` with this type of AttachEffect applied on it
  should remove the animation while being warped out by a :tag:`Temporal=yes`
  weapon. Otherwise the animation stays active and unaffected by the temporal
  weapon. Defaults to :value:`no`.

:tagdef:`[Section]AttachEffect.SpeedMultiplier=float - multiplier`
  Speed bonus while the AttachEffect lasts. Defaults to :value:`1.0`.

:tagdef:`[Section]AttachEffect.ArmorMultiplier=float - multiplier`
  Armor bonus while the AttachEffect lasts. Defaults to :value:`1.0`.

:tagdef:`[Section]AttachEffect.FirepowerMultiplier=float - multiplier`
  Firepower bonus while the AttachEffect lasts. Defaults to :value:`1.0`.

:tagdef:`[Section]AttachEffect.Cloakable=boolean`
  Whether the unit gains cloaking ability while the AttachEffect lasts. Defaults
  to :value:`no`.

The following tags are valid on TechnoTypes only:

:tagdef:`[TechnoType]AttachEffect.Delay=integer`
  Defines how many frames after the previous effect subsides the AttachEffect is
  recreated on the unit itself. Negative values do not renew the effect.
  Defaults to :value:`0` (immediately).

The following tags are valid on Warheads only:

:tagdef:`[Warhead]AttachEffect.Cumulative=boolean`
  If set to :value:`yes`, an unlimited amount of this type of AttachEffect from
  this warhead can be applied to the target (it is stackable). If :value:`no`,
  only one instance of this type of the AttachEffect can be on a single unit and
  that one instance gets updated if it is to be applied again. Defaults to
  :value:`no`.

:tagdef:`[Warhead]AttachEffect.AnimResetOnReapply=boolean`
  If this type of AttachEffect is not stackable, enabling this flag resets the
  animation on every time of reapplying. Defaults to :value:`no`.

.. index:: Weapons; AttachEffect

.. versionadded:: 0.4

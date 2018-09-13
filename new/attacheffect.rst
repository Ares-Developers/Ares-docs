.. index:: Weapons; AttachEffect

AttachEffect
~~~~~~~~~~~~

The AttachEffect system was designed as a spiritual successor to
:game:`NPatch`'s Upgrade logic, but it was aimed to not be limited only to
superweapons. AttachEffect tags can be applied to both the Big Four (all
:type:`TechnoTypes`) and :type:`Warheads`, unless stated otherwise.

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

:tagdef:`[Section]AttachEffect.Duration=integer - frames`
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

  .. note:: Mind that this works fundamentally differently from the other
    effects, which are applied the instant they are needed (like a firepower for
    a bullet impacting) as long as the effect is active: the reload time is
    computed once when the reloading starts, but the modified reloading time may
    take longer than the attached effect lasts.

    For instance, a unit that was struck with an effect slowing down the ROF
    extremely might thus render the unit unable to fire way longer than the
    AttachEffect is active, because the reload timer will not speed up again
    when the effect expires.

:tagdef:`[Section]AttachEffect.ROFMultiplier=float - multiplier`
  Rate of fire bonus while the AttachEffect lasts. Defaults to :value:`1.0`.


:tagdef:`[Section]AttachEffect.Cloakable=boolean`
  Whether the unit gains cloaking ability while the AttachEffect lasts. Defaults
  to :value:`no`.

:tagdef:`[Section]AttachEffect.ForceDecloak=boolean`
  Whether affected units will be forced to decloak when the AttachEffect gets
  applied (useful for non-damaging anim-based AttachEffects). Defaults to
  :value:`no`.

:tagdef:`[Section]AttachEffect.DiscardOnEntry=boolean`
  Whether the AttachEffect will be removed when the affected unit is removed
  from the map (entering a building or another unit). Defaults to :value:`no`.

:tagdef:`[Section]AttachEffect.PenetratesIronCurtain=boolean`
  Whether the AttachEffect can attach to a unit or structure under the influence
  of an Iron Curtain or Force Shield. Defaults to :value:`no`.

The following tags are valid on TechnoTypes only:

:tagdef:`[TechnoType]AttachEffect.Delay=integer - frames`
  Defines how many frames after the previous effect subsides the AttachEffect is
  recreated on the unit itself. Negative values do not renew the effect.
  Defaults to :value:`0` (immediately).

:tagdef:`[TechnoType]AttachEffect.InitialDelay=integer - frames`
  Defines the delay before creating the AttachEffect for the very first time.
  Subsequent delays are defined by :tag:`AttachEffect.Delay`. Use :value:`0` to
  create effect immediately. Defaults to :value:`0`.

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

.. versionadded:: 0.4
.. versionchanged:: 2.0

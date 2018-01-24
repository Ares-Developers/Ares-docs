:captiontag:`Temporal`
``````````````````````

.. index::
  Warheads; WarpAway animation
  Temporals; WarpAway animation per warhead

Customizable :captiontag:`WarpAway`
-----------------------------------

:tagdef:`[Warhead]Temporal.WarpAway=animation`
  If set, specifies the animation to be played when this warhead erases an
  object. Defaults to :tag:`[General]WarpAway`.

.. versionadded:: 0.1


.. index::
  Warheads; Temporals consider health
  Temporals; Consider victim's health

Consider Health
---------------

:tagdef:`[Warhead]Temporal.HealthFactor=float - multiplier`
  How much the health of the victim is factored in into the remaining warp value
  of the target. Valid values range from :value:`0.0` to :value:`1.0` inclusive.
  :value:`0.0` means health plays no role. :tag:`1.0` means the remaining warp
  is reduced proportionally to the target's health, down to 0. Defaults to
  :value:`0.0`.

  .. note:: Another way to look at it is that the remaining warp value is
    linearly decreased from full for completely healthy targets down by this
    value for a target that has no health left.

.. versionadded:: 0.D

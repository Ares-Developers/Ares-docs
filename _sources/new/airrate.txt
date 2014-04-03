AirRate
~~~~~~~

When a unit is moving, :tag:`WalkRate` is used to control the unit's animation,
when it is idle, :tag:`IdleRate` is used. A unit counted as idle if it wasn't
moving, which also included taking off, landing and hovering, and thus
helicopter style units would not play their rotor animation even if they clearly
were in air. :game:`Ares` adds a new tag for this situation.

:tagdef:`[TechnoType]AirRate=integer - number of frames`
  If higher than :value:`0`, defines after how many frames the unit's animation
  is to be advanced to the next frame when the unit is in air. :tag:`AirRate`
  takes precedence over :tag:`WalkRate` and :tag:`IdleRate`. :value:`0` disables
  :tag:`AirRate`. Defaults to :value:`0`.

.. index:: HVA; Always play animation when unit in air.

.. versionadded:: 0.6

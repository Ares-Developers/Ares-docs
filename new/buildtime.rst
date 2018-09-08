.. index::
  Factories; Build time fully customizable per type

Build Time
~~~~~~~~~~

In :game:`Ares` it is possible to customize all settings related to the build
time of objects per type.

:tagdef:`[TechnoType]BuildTime.Speed=double - minutes`
  The time in minutes it takes to produce an object which costs 1000 credits.
  Defaults to :tag:`[General]BuildSpeed`.

  .. note:: If set, :tag:`WallBuildSpeedCoefficient` will not be applied to
    :tag:`Wall=yes` buildings any more, because :tag:`BuildTime.Speed` is taken
    as final value.
:tagdef:`[TechnoType]BuildTime.Cost=integer - credits`
  If set, the build time is calculated as if this item cost this much, instead
  of using actual :tag:`Cost`. Defaults to :tag:`Cost`.

If the player does not have enough power, the following settings apply. They
define a factor applied to the amount of power lacking and the range the
resulting modifier will be clamped in before being multipled with the build
time.

:tagdef:`[TechnoType]BuildTime.LowPowerPenalty=double - modifier`
  The penalty to apply to the build time in low power situations. Defaults to
  :tag:`[General]LowPowerPenaltyModifier`.

:tagdef:`[TechnoType]BuildTime.MinLowPower=double`
  The minimum production speed when power is low. The resulting low power
  modifier will not be lower than this. Defaults to
  :tag:`[General]MinLowPowerProductionSpeed`.

:tagdef:`[TechnoType]BuildTime.MaxLowPower=double`
  The maximum production speed when power is low. The resulting low power
  modifier will not be greater than this. Defaults to
  :tag:`[General]MaxLowPowerProductionSpeed`.

When a player has more than one factory of the same type, the following modifier
also applies.

:tagdef:`[TechnoType]BuildTime.MultipleFactory=double - multiplier`
  The factor multiplied by the build time per additional factory of the same
  type. Defaults to :tag:`[General]MultipleFactory`.

.. versionadded:: 2.0

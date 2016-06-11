Factory Plant Effect
~~~~~~~~~~~~~~~~~~~~

The cost reduction effect of :tag:`FactoryPlant` buildings like the Industrial
Plant can be modified per :type:`TechnoType`, using this multiplier.

:tagdef:`[TechnoType]FactoryPlant.Multiplier=double - multiplier`
  The effect of the respective :tag:`CostBonus` tag for this type is multiplied
  by this value to either increase, decrease, or nullify the effect. Fully
  supported values range from :value:`-1.0` to reverse the effect to
  :value:`1.0` to not affect the effect. :value:`0.0` nullifies the bonus.
  Defaults to :value:`1.0`.

  .. note:: Values beyond :value:`1.0` can potentially cause the cost to drop to
    zero, if the effect of the product of all cost bonuses is multiplied by a
    too large value. This is because the effect of this multiplier is linear.

An example: If the cost bonus is :value:`0.6` and the multiplier is
:value:`0.5`, then the final bonus will be :value:`0.8`. In other words: if a
bonus reduces the cost to 60% and the multiplier only grants half of that, the
final price will be at 80% of the original cost.

.. index:: Factory Plant; Modify the effect of Industrial Plants

.. versionadded:: 0.C

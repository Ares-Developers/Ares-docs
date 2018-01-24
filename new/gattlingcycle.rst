.. index::
  Weapons; Cycle Gattling weapons without losing target
  Gattling; Cycle weapons without losing target

Gattling Enhancements
~~~~~~~~~~~~~~~~~~~~~

The gattling weapon system in :game:`Yuri's Revenge` switches weapons the
longer it keeps firing. Once the highest stage is reached, it will  maintain
the last weapon until the target is destroyed or the unit is given another
order.

By the use of :tag:`FireOnce=yes` on the last weapon stage the gattling can be
made to switch back to the first stage and start spinning up again. This
workaround comes with side effects; the most notable is that the unit will lose
its target and thus may not fire at a single unit continuously.

:tagdef:`[TechnoType]Gattling.Cycle=boolean`
  When the last :tag:`Stage` or :tag:`EliteStage` is completed, the counter
  will wrap around and restart with the first stage without the firing unit
  losing target. Requires :tag:`IsGattling=yes`. Defaults to :value:`no`.

.. note:: The gattling firing effect depends on the stage and :tag:`RateUp` and
  \ :tag:`RateDown` values as well as the individual state of the firing unit.
  It is not possible to guarantee that a certain stage fires a fixed amount of
  times.

.. versionadded:: 0.3

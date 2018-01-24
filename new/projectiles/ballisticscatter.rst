.. index:: Projectiles; BallisticScatter

:captiontag:`BallisticScatter`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The global :tag:`[CombatDamage]BallisticScatter` is used for defining a range
depending on the projectile's properties, and then randomly picking a value from
this range as the final scatter distance for each projectile fired. :game:`Ares`
makes this global customizable as two separate tags that can be used to specify
the minimum and maximum distances for each :type:`Projectile` directly.

Both tags require :tag:`Inaccurate=yes` and :tag:`Arcing=yes`.

:tagdef:`[Projectile]BallisticScatter.Min=float - cell range`
  The minimum range in cells a projectile can scatter. Defaults to
  :tag:`[CombatDamage]BallisticScatter` :value:`/ 2` if :tag:`FlakScatter=no` or
  :tag:`Inviso=yes`, to :value:`0` otherwise.

:tagdef:`[Projectile]BallisticScatter.Max=float - cell range`
  The maximum range in cells a projectile can scatter. Defaults to
  :tag:`[CombatDamage]BallisticScatter`.

.. note:: \ :tag:`Inaccurate=yes` prevents projectiles to "snap" to their target
  on impact, and thus they will not deal damage to them because this does not
  count as a direct hit even if ballistic scatter is set to a low value. Using
  \ :tag:`CellSpread` fixes this.

.. note:: There is one more place :tag:`[CombatDamage]BallisticScatter` is used
  and that is not customizable yet. It scatters an extra amount from :value:`0`
  to :value:`2 *` :tag:`[CombatDamage]BallisticScatter` for projectiles with
  both :tag:`FlakScatter=yes` and :tag:`Inviso=yes` set.

.. versionadded:: 0.7

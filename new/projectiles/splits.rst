:captiontag:`Splits` and :captiontag:`Airburst`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :tag:`Splits` missile feature of :game:`Firestorm` fame has been ported over
to :game:`Yuri's Revenge`, with several changes and additions. The related
:tag:`Airburst` logic has been expanded.

.. versionadded:: 0.7


:captiontag:`Splits`
--------------------

The split weapon of the Cyborg Reaper from :game:`Firestorm` fired two missiles.
Each of them split in mid-air after gaining some altitude, releasing two new
projectiles each, which would either travel on to the initial target, aim for a
new target no more than two cells nearby, or impact on a random cell in a 7 by 7
area.

The actual split happens when an :tag:`Airburst=yes` projectile is above its
target, a :tag:`Ranged=yes` projectile exceeds its weapon's
:doc:`ProjectileRange </new/weapons/projectilerange>` or the projectile
detonates otherwise.

Refer to `Splits on ModEnc <http://modenc.renegadeprojects.com/Splits>`_ for a
more detailled description of the logic.

.. note:: The Splits logic has been de-hardcoded compared to :game:`Tiberian
  Sun`. The :tag:`AirburstWeapon`'s :tag:`Damage` is no longer multiplied by
  \ :value:`10`. Its :tag:`Speed` is used instead of the hardcoded :value:`19`,
  and its :tag:`Bright` setting is now also respected instead of just being
  disabled.

.. warning:: Even though speed is not hardcoded any more, you cannot use
  \ :tag:`Speed` values lower than :value:`19` on the :tag:`AirburstWeapon` or
  the logic will start to fail and behave erratically.

:tagdef:`[Projectile]Splits=boolean`
  Whether the projectile will split into a number of other projectiles defined
  by :tag:`Cluster` and :tag:`AirburstWeapon`. Can be combined with
  :tag:`Airburst`. Defaults to :value:`no`.

:tagdef:`[Projectile]RetargetAccuracy=float - percentage`
  The probability that a split cluster will aim for the same target the original
  projectile was shot at. The higher the value, the less likely it is for the
  split projectile to chose another target. Valid range is :value:`0.0` to
  :value:`1.0`. Defaults to :value:`0.0`.


:captiontag:`Airburst`
----------------------

The :tag:`Airburst` logic was used for the MultiMissile in :game:`Tiberian Sun`
to deal damage to randomly selected cells below the target area. In :game:`Red
Alert 2` the logic has been changed and it always bursts into nine clusters
covering an area of 3 by 3 cells.

:tagdef:`[Projectile]AirburstSpread=float - cell range`
  The range the airburst effect covers. Each cell in range will be targeted by
  the :tag:`AirburstWeapon`. Requires :tag:`Airburst=yes`. Cannot be combined
  with :tag:`Splits=yes`. Defaults to :value:`1.5`.


Common Settings
---------------

:tagdef:`[Projectile]AroundTarget=boolean`
  Whether a projectile with :tag:`Splits=yes` or :tag:`Airburst=yes` should use
  the area around the original target to look for new targets for each cluster.
  If enabled, the clusters will continue their way to the originally intended
  target. Otherwise, the clusters will search for new targets in the area where
  the projectile split up. Defaults to :tag:`Splits`.

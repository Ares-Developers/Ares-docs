.. index:: Tiberium; Full harvesters explode

Tiberium Explosive
``````````````````

Tiberium Explosive is the feature that harvester units detonate violently on
destruction. It is not to be confused with the similarly named Tiberium
Explosion.

The damage to deliver depends on :tag:`Power` of the contained tiberium bails.
This is like it was in :game:`Firestorm`. :game:`Tiberian Sun` also added the
harvester unit's strength, which has not been recreated.

:game:`Tiberian Sun` used :tag:`C4Warhead` to deliver the damage, with a
hardcoded spread of :value:`1.5`. :game:`Ares` requires the warhead to define
:tag:`CellSpread` itself.

Only positive damage is delivered. In case :tag:`TiberiumExplosiveWarhead` is
not set or the Harvester Truce feature is enabled, no damage is delivered.

:tagdef:`[CombatDamage]TiberiumExplosive=boolean`
  Whether tiberium inside of harvester units explodes using
  :tag:`TiberiumExplosiveWarhead` when destroyed. Defaults to :value:`no`.

:tagdef:`[CombatDamage]TiberiumExplosiveWarhead=warhead`
  The warhead to deliver the damage of explosive tiberium. Defaults to
  :value:`none`.

.. versionadded:: 0.5

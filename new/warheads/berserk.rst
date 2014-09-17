Berserk Reloading Time Modifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Units under the effect of Chaos Gas or other :tag:`Psychedelic=yes` warheads go
berserk, which reduces their willingness to obey orders as well as their
reloading time. This reloading time factor can be customized globally and for
each :type:`TechnoType`.

:tagdef:`[CombatDamage]BerserkROFMultiplier=float - multiplier`
  The multiplier applied to the reloading time when a unit is berserking.
  Smaller means shorter reloading and faster firing. Defaults to :value:`0.5`.

:tagdef:`[TechnoType]Berserk.ROFMultiplier=float - multiplier`
  The multiplier applied when this unit is berserking. Smaller means faster
  firing. Defaults to :tag:`[CombatDamage]BerserkROFMultiplier`.

.. index:: Berserk; Reloading time multiplier

.. versionadded:: 0.8

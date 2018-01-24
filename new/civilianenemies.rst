Civilian Enemies
~~~~~~~~~~~~~~~~

In :game:`Red Alert 2` the environment is pretty much friendly and factions do
not have to fear an attack of inhabitants of the territory they are fighting in.
The engine would not know how to deal with them, and this is what :game:`Ares`
changes.


.. index:: Civilians; Always treat as enemy

Treat Civilians as Enemies
--------------------------

:game:`Yuri's Revenge` makes a distinction between single player and multi
player games. In multiplay matches all objects belonging to a house with
:tag:`MultiplayPassive=yes` are considered neutral, with the exception of tech
and occupiable structures. In single player missions units are not considered
neutral if they are :tag:`Insignificant=no`.

:tagdef:`[TechnoType]CivilianEnemy=boolean`
  Whether this unit is considered an enemy when auto-acquiring a target.
  Enabling this prevents a unit of this type to be considered neutral in
  multiplayer matches. Defaults to :value:`no`.

.. versionadded:: 0.7


.. index:: Civilians; Recognize and repel civilian threats

Repelling Civilian Attacks
--------------------------

If civilians are not recognized as dangerous, only units or structures attacked
by such neutral units will retaliate against them. This way units like the
Visceroid or the Tiberium Fiend can bring down a house's buildings one by one.

This new tag makes the AI's or the player's unit smarter in defending against
such threats as civilians attacking a power plant will be repelled by all allies
in range, or alligators eating Engineers with armed bystanders just idling.

:tagdef:`[CombatDamage]AutoRepel=boolean`
  Whether AI players will consider civilian units attacking allied objects as
  enemy when auto-acquiring targets. This makes units nearby help protect
  against an offender. Otherwise, only the attacked unit retaliates. Defaults to
  :value:`no`.

:tagdef:`[CombatDamage]PlayerAutoRepel=boolean`
  Whether human players will consider civilian units attacking allied objects as
  enemy when auto-acquiring targets. This makes units nearby help protect
  against an offender. Otherwise, only the attacked unit retaliates. Defaults to
  :value:`no`.

.. versionadded:: 0.7

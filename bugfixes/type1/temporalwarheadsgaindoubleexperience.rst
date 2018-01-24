.. index::
  Temporal; Temporal warheads won't gain twice the experience anymore
  Bugs; Temporal warheads gained twice the experience

======================================================
:captiontag:`Temporal` Warheads Gain Double Experience
======================================================

Killing a unit using a weapon with a :tag:`Temporal=yes` warhead gained the
attacker twice the experience it deserved. This was because the temporal weapon
updated the killer's experience and then went on calling a game function that
did the same.

:game:`Ares` removes the temporal weapon's veterancy update, so this no longer
happens.

.. versionadded:: 0.2

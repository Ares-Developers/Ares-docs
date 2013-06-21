.. index:: Engineer, Crew; Crew with Engineer=yes causes infinite loop.
.. index:: Crew; Undefined crew causes crash.

==========================================================
Crew with :captiontag:`Engineer=yes` could freeze the game
==========================================================

Because of a bad algorithm selling a building could go into an infinite loop.
The game ensures to at most spawn one infantry unit having :tag:`Engineer=yes`
set by just generating a new crew member until it has :tag:`Engineer=no` set.
If there are only crew types (set in :tag:`AlliedCrew=`, :tag:`Technician=`,
:tag:`Engineer=` and others) with :tag:`Engineer=yes`, this will never succeed
and the game will freeze.

.. versionadded:: 0.3

============================================================================================
Crash with undefined :captiontag:`Engineer`, :captiontag:`Technician` and :captiontag:`Crew`
============================================================================================

When :tag:`Technician=`, :tag:`Engineer=`, :tag:`AlliedCrew=` and others
weren't defined, the game crashed when a building was sold or destroyed. This
was just because of oversights in both cases.

When selling, the flawed :tag:`[InfantryType]Engineer=yes` check happened
before the crew type was verified to be set at all.

When destroyed, the game checked whether the crew type was set, but then went
ahead and tried to write the name of the crew type to the debug log regardless
of the result.

.. versionadded:: 0.3

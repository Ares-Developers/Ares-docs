.. index:: Temporal; Temporal warheads no longer affect objects that are not Warpable.

==========================================================================
:captiontag:`Temporal` Warheads Still Affect Objects That Are Not Warpable
==========================================================================

Attacking a unit with a :tag:`Temporal=yes` warhead when it should not be
susceptible due to having :tag:`Warpable=no` set, could still experience some
negative effects. Units that were mind-controlled by the unwarpable unit would
be freed and aircraft-spawners would have those aircraft destroyed. Unwarpable
units are no longer affected in this manner.

.. versionadded:: 0.1

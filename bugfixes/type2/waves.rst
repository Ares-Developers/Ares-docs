.. index:: Weapons; Wave issues (IsLaser, IsBigLaser, IsSonic, IsMagBeam)

================================================
:captiontag:`IsMagBeam` Waves and Moving Targets
================================================

:tag:`IsMagBeam=yes` waves would not disconnect from their target if it moved
out of weapon's range of the firing unit. The unit would no longer fire, but the
beam would persist. If the wave dealt :tag:`AmbientDamage`, this would still be
applied though.

Magnetron waves are now always disconnected in :game:`Ares` if the target moves
out of range.

.. versionadded:: 0.B


================================================
:captiontag:`IsSonic` Waves and Hardcoded Ranges
================================================

:tag:`IsSonic=yes` waves were hardcoded to disappear if they were farther away
from their source than six diagonal cells, equalling a cell range of about 8.5.
If the weapon's range was longer than that, the sonic waves would dissolve
before reaching their target.

In :game:`Ares` this has been changed to use the weapon's actual range.

.. versionadded:: 0.B


=========================================================================
:captiontag:`IsLaser` and :captiontag:`IsBigLaser` on Lower Detail Levels
=========================================================================

:tag:`IsLaser` and :tag:`IsBigLaser` waves were always invisible if the detail
level wasn't set to high. This was unlike all other waves and was most likely a
leftover from :game:`Tiberian Sun`, where these kinds of waves were used to give
lasers drawn by the actual laser line drawing mechanism a more detailled glow.

Laser waves will now always draw, because they are a standalone feature in
:game:`Ares`.

.. versionadded:: 0.B

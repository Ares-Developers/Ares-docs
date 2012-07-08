.. index:: Sounds; Units pulled by a Magnetron will on longer play their move sound.

=========================================
Unit Sounds Played At Inappropriate Times
=========================================
When a unit was pulled by a Magnetron it would play its :tag:`MoveSound`, even
though it was not moving under its own power. Now, this sound will only be
played when the unit moves under its own power.

.. versionadded:: 0.1

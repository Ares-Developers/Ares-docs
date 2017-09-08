Flashing
````````

When a unit is hit by this warhead, it can be made to flash. This effect is used
to indicate a unit being repaired or healed (:value:`7` frames) or promoted. In
:game:`Red Alert`, flashing was also used when a unit was hit by a
:tag:`Charges=yes` weapon (:value:`4` frames).

.. note:: This is only supported on warheads doing damage, not for healing
  warheads.

:tagdef:`[Warhead]Flash.Duration=integer - frames`
  If positive, the victim hit by this warhead will flash for the specified
  amount of frames. Defaults to :value:`0`.

.. index:: Warheads; Flashing effect

.. versionadded:: 0.E

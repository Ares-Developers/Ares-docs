.. index:: ProduceCash; Unexpected ProduceCashDelay behavior

=======================================
:captiontag:`ProduceCashDelay` Problems
=======================================

:tag:`ProduceCashDelay` was handled differently than other timers, as it fired
one frame earlier than expected. This might have been done to distinguish from
buildings that don't produce cash, because their timer is always set to 0.

If the timer expired, it would not be reset. This did not only happen for cash
producing buildings, but also if a cash producing building was attacked by a
:tag:`Temporal=yes` weapon at the time the timer reached and passed 1 without
being reset. The consequence was that the building would stop producing cash
until captured by and recaptured from a :tag:`MultiplayPassive=yes` house.

Both issues have been fixed. The full :tag:`ProduceCashDelay` is now used and
the timer will be reset correctly.

Also, the delay never started if :tag:`ProduceCashStartup` was :value:`0`. In
:game:`Ares` it will start anyhow.

.. versionadded:: 0.B

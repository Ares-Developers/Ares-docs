.. index:: BuildLimit; Last unit with BuildLimit>1 could not be queued

===================================
:captiontag:`BuildLimit` and Queues
===================================

The vehicle or infantry currently in production was counted twice, and thus the
:tag:`BuildLimit` check triggered too early if a unit of the same type was
already in production. Once the build queue was empty again, the last unit could
be queued normally. This has been fixed.

.. versionadded:: 0.6

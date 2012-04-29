.. index:: Verses; Warhead verses special values (0%/1%/2%) should now apply their behavior consistently.

============================================
Warhead :captiontag:`Verses`' Special Values
============================================

The :tag:`Verses` flag (which is used on warheads to manipulate the damage dealt
versus different armor types) has three special-case values used to define
additional behavior:

:value:`0%`
  means no force fire, no retaliate, no passive acquire
:value:`1%`
  means no retaliate, no passive acquire
:value:`2%`
  means no passive acquire
  
However, a bug with the way the floating-point values are compared means that
these behaviors were not always applied consistently. :game:`Ares` fixes this
bug so the behavior should always be consistent now. The special behaviors can
also now be toggled independently of the :tag:`Verses` value (see
:doc:`/new/additionalarmortypesandverses`). 

.. versionadded:: 0.1

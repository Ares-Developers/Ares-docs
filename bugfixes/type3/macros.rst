.. index:: Performance; Damage presumably done by macros

=======================
Repeated Function Calls
=======================

Presumably caused by using preprocessor macros in the source code, some parts of
the game call the same functions twice. The macros to select the minimum or
maximum of two passed values are most notorious for this behavior. The effect is
that a function is unnecessarily called a second time, and if the called
function exhibits the same problem, it calls another function two times each.
:game:`Ares` fixes some of these function calls.

.. versionadded:: 3.0

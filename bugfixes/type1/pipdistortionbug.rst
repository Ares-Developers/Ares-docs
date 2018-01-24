.. index::
  Pips; Pip distortion bug resolved
  Glitches; Wrong pips being used unexpectedly

==================
Pip Distortion Bug
==================

Because of a broken lookup function, the values of :value:`Pip` and
:value:`OccupyPip` were corrupted whenever a section was present in an INI file
but these both tags were not defined in it. This made the game use the wrong pip
image for occupied buildings or transporters. :game:`Ares` fixes this.

See also :doc:`Pips </new/pips>`.

.. versionadded:: 0.4

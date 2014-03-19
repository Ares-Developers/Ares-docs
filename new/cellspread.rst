:captiontag:`CellSpread` Enhancements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:captiontag:`CellSpread` Hit Limit
----------------------------------

The :tag:`CellSpread` logic iterates all cells in range, and affects all objects
on these cells. If an object occupies more than one cell like buildings with a
foundation larger than 1x1, it could be encountered multiple times and thus
would take multiple hits (potentially one for each cell of its foundation).

The following tag limits the number of times the same object can be hit by the
same cause. If an object is hit more often than allowed, the hits closest to the
impact site are used, all others are discarded.

:tagdef:`[Warhead]CellSpread.MaxAffect=integer`
  The number of times an object can be affected at most when hit by a warhead
  using :tag:`CellSpread`. Set this to :value:`1` to make the same object not be
  hit not more than once. Defaults to :value:`-1` (infinite).

.. index:: Warheads; Limit how often CellSpread hits the same object.

.. versionadded:: 0.6

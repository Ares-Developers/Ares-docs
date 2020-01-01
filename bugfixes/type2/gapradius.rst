.. index:: Gap Generators; Radius can be greater than 127 cells

==================================================
Gap Generator Radius can be greater than 127 Cells
==================================================

Due to :game:`Yuri's Revenge` using a too small data type, the radius for the
Gap Generators could not be greater than 127 cells. :game:`Ares` reimplemented
the tags and now :tag:`GapRadiusInCells=` and :tag:`SuperGapRadiusInCells=`
support greater values.

.. note:: Use this new freedom with caution. Including too many cells can cause
  lag.

.. versionadded:: 3.0

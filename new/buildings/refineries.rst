.. index:: Buildings; Unloading settings for Refineries

Refineries
==========

The following tags have to be defined on the Refinery's image in
:file:`artmd.ini`.

:tagdef:`[BuildingImage]DockUnloadCell=2 integers - cell offset`
  The cell a harvester will dock on when unloading on this refinery. The cell is
  required to be passable. Defaults to :value:`3,1`.

:tagdef:`[BuildingImage]DockUnloadFacing=integer - facing32`
  The facing a harvester will turn to when docking on this refinery. Defaults to
  :value:`8` (east).

.. versionadded:: 3.0

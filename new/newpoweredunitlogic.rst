.. index::
  Powered Unit; Multiple powered units like the Robot Tank
  TechnoTypes; Alternative to PowersUnit

New Powered Unit Logic
~~~~~~~~~~~~~~~~~~~~~~

In original :game:`Yuri's Revenge`, the :tag:`PowersUnit=` tag logic dictated
that there could only be one powered :type:`UnitType`, and one building
providing power, per side. :game:`Ares` extends this with :tag:`PoweredBy=`,
which allows each side to have multiple buildings power multiple units.

:tagdef:`[UnitType]PoweredBy=list of BuildingType`
  Allows multiple powered units to exist, as well as allowing multiple buildings
  to provide power. Defaults to :value:`none`.

.. note:: \ :tag:`PoweredBy=` can use multiple buildings, but be advised, using
  a comma to separate multiple buildings will be parsed as "or" rather than
  "and". There is no "and" capacity.

.. versionadded:: 0.2

New Powered Unit Logic
~~~~~~~~~~~~~~~~~~~~~~

In original :game:`Yuri's Revenge`, the :tag:`PowersUnit=` tag logic dictated
that there could only be one powered :type:`UnitType`, and one building
providing power, per side. :game:`Ares` extends this with :tag:`PoweredBy=`,
which allows each side to have multiple buildings power multiple units.

:tagdef:`[UnitType]PoweredBy=BuildingType`
  Allows multiple powered units to exist, as well as allowing multiple buildings
  to provide power. Defaults to :value:`none`.

.. note:: Be advised, if a powered unit is being built when the building that
  powers this unit is destroyed, the immobile unit will jam up that war factory
  until destruction or a building from :tag:`PoweredBy=` is rebuilt.

.. note:: \ :tag:`PowersUnit=` is usable but obsolete in Ares. Therefore
  features using :tag:`PowersUnit=` won't be supported by the BugTracker or
  RenProj in general.

.. note:: \ :tag:`PoweredBy=` can use multiple buildings, but be advised, using
  a comma to separate multiple buildings will be parsed as "or" rather than
  "and". There is no "and" capacity.

.. versionadded:: 0.2

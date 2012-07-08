:captiontag:`AlternateTheaterArt`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Navy Seal has :tag:`AlternateArcticArt=yes` set, which causes the game to
use the image file :file:`seala.shp` on arctic maps, instead of
:file:`seal.shp`. This logic works for any :type:`InfantryType`, however this
only works for the arctic theater and only for :tag:`InfantryTypes`.

:tagdef:`[TechnoType]AlternateTheaterArt=boolean`
  Specifies whether or not this SHP-based unit can have alternate art depending
  on the theater of the current map. For example, setting :tag:`Image=JUNK` and
  :tag:`AlternateTheaterArt=yes` on a unit will make the unit load
  :file:`artmd.ini` section :tag:`[JUNKA]` on arctic, :tag:`[JUNKD]` on desert,
  and so on according to theater. If any of those sections do not exist then the
  unit will fall back to :tag:`[JUNK]`. So quite similar to
  :tag:`AlternateArcticArt`, just automatic and smarter. Defaults to
  :value:`no`.

.. note:: This only works for SHP-based units. Voxels do not use this system and
  cannot have theater-specific art (you'd have to use
  \ :tag:`Prerequisite.RequiredTheaters` to achieve that).

.. index:: Art; AlternateTheaterArt for InfantryTypes supports all theaters.

.. versionadded:: 0.2

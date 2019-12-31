Mouse Cursors
~~~~~~~~~~~~~

.. index:: Mouse Cursors; Defining a cursor

Defining Cursors
================

New cursors can be added and default cursors can be changed using the new
:tag:`[MouseCursors]` section, which centralizes cursor definitions in one
place. Each cursor has a name, which can then be used as valid value for tags
asking for a mouse cursor. Cursors are defined in a single line with
comma-separated values as follows:

:tagdef:`[MouseCursors]Name=cursor definition`
  :tag:`Name` can be up to 31 characters long. Enter the values in the given
  order, separated by commas:
  :value:`Frame,Count,Interval,MiniFrame,MiniCount,HotSpotX,HotSpotY`. If fewer
  items are defined, the remaining values are defaulted.

  :value:`Frame` is the starting frame of the cursor from :file:`mouse.sha`. The
  first frame is :value:`0`. Defaults to :value:`0`.

  :value:`Count` is the number of frames in the animated cursor. Defaults to
  :value:`1`.

  :value:`Interval` is the rate to animate the cursor. Defaults to :value:`0`.

  :value:`MiniFrame` is like :value:`Frame`, except this is for the mouse cursor
  when positioned on the minimap. Set this to :value:`-1` to disable the minimap
  cursor and to only allow players to click on the battlefield. Defaults to
  :value:`-1`.

  :value:`MiniCount` is like :value:`Count`, except this is for the mouse cursor
  when positioned on the minimap. Defaults to :value:`-1`.

  :value:`HotSpot` specifies the point from which the click event will handled.
  :value:`HotSpotX` should be one of :value:`Left`, :value:`Center` or
  :value:`Right`. :value:`HotSpotY` should be one of :value:`Top`,
  :value:`Middle` or :value:`Bottom`. For example, :value:`Left,Top` will treat
  the top-left corner of the cursor as the tip. Default is
  :value:`Left,Top`.

  .. note:: You cannot directly use the same definitions as used with other
    patches for :game:`Yuri's Revenge`, because :game:`Ares` uses descriptive
    names instead of numbers for the HotSpotX,HotSpotY parts. To convert the
    values, replace :value:`0` by either :value:`Left` or :value:`Top`,
    \ :value:`12345` by either :value:`Center` or :value:`Middle`, and
    \ :value:`54321` by either :value:`Right` or :value:`Bottom`.

.. versionadded:: 0.D


.. index::
  Mouse Cursors; List of default cursors
  Mouse Cursors; New intrinsic named cursors

Default Cursors
===============

The original game's cursors are defined implicitly, that is, they exist and are
available even without them being explicitly defined. See the :download:`list of
default cursors </extras/MouseCursors.txt>`.

:game:`Ares` adds several new named cursors by default, which are used for
special purposes like newly added features, or to distinguish different unit
actions. These cursors can be overridden to give these functions a separate
cursor without also changing the original cursors.

+ :value:`TogglePower`: used for the Toggle Power feature when toggling power
  is possible on a building. Defaults to :value:`Power`.
+ :value:`NoTogglePower`: used for the Toggle Power feature when toggling power
  is not allowed. Defaults to :value:`Disallowed`.
+ :value:`EngineerDamage`: the cursor when an Engineer will not capture a
  building due to MultiEngineer being enabled. Defaults to :value:`Detonate`.
+ :value:`InfantryHeal`: the repair cursor on allied infantry. Defaults to
  :value:`355,1,0,-1,-1,Center,Middle`.
+ :value:`UnitRepair`: the repair cursor on allied units. Defaults to
  :value:`Repair`.
+ :value:`Tote`: used for picking up Carryall cargo. Defaults to the blue move
  cursor.
+ :value:`TakeVehicle`: used for VehicleThief and CanDrive on capturable
  vehicles. Defaults to the :value:`Enter`.
+ :value:`Sabotage`: used for Saboteur infantry on valid target buildings.
  Defaults to the :value:`Enter`.
+ :value:`RepairTrench`: used for Engineers on trench buildings to rebuild.
  Defaults to the :value:`Repair`.

.. note:: The default cursors might change. :game:`Ares` might add more special
  cursors to differentiate actions in a later version, change the defaults of
  the new cursors, or enable animations on default cursors.

.. warning:: Changing the cursor called :value:`Default` is not supported.

.. versionadded:: 0.D


Migrating from Previous Versions
================================

Ares versions prior to 0.D supported seven tags to define a mouse cursor: one
base tag and six additional tags to define each of the parts of a cursor
definition separately.

To migrate to the new :tag:`[MouseCursors]` section, first merge the separate
tags like :tag:`Cursor.Frame=355`, :tag:`Cursor.Count=1`, ... into a one-line
definition like :tag:`Cursor=355,1,...`.

If you have such a one line cursor definition, copy it into the new
:tag:`[MouseCursors]` section and give it a new, unique name like :tag:`Medic`.
Use this unique name instead of the original :tag:`Cursor=355,1,...`  line, that
is, make it :tag:`Cursor=Medic`.

If you are using the same cursor definitions in several places, there is no need
to give each a new name. You can reuse existing cursors.

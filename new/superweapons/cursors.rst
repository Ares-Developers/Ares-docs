.. _sw-cursors:

Cursors
```````

:game:`Ares` allows you to specify custom mouse cursors for the super weapon,
using the following flags:

:tagdef:`[SuperWeapon]Cursor.Frame=integer`
  Starting frame of the cursor from \ :file:`mouse.sha`. Defaults to the Attack
  cursor.
:tagdef:`[SuperWeapon]Cursor.Count=integer`
  Number of frames in the animated cursor.
:tagdef:`[SuperWeapon]Cursor.Interval=integer`
  How often to animate the cursor? Default is :value:`5`.
:tagdef:`[SuperWeapon]Cursor.MiniFrame=integer`
  Same as :tag:`Cursor.Frame`, except this is for the mouse cursor when
  positioned on the minimap. Set this to :value:`-1` to disable the minimap
  cursor and to only allow players to click on the battlefield.
:tagdef:`[SuperWeapon]Cursor.MiniCount=integer`
  Same as :tag:`Cursor.Count`, except this is for the mouse cursor when
  positioned on the minimap.
:tagdef:`[SuperWeapon]Cursor.HotSpot=HotSpot X, HotSpot Y`
  Specifies the coordinates on the cursor that are considered to be the 'tip'
  that is, the point from which the click event will handled. HotSpot X should
  be one of :value:`Left`, :value:`Center` or :value:`Right`. HotSpot Y should
  be one of :value:`Top`, :value:`Middle` or :value:`Bottom`. For example,
  :tag:`Cursor.HotSpot=Left,Top` will treat the top-left corner of the cursor as
  the tip. Default is :value:`Center,Middle`.


All of the above :tag:`Cursor.*` flags have a corresponding :tag:`NoCursor.*`
flag, which allows you to specify the cursor that will be displayed when the
mouse pointer is positioned over a point where the super weapon cannot be fired
(e.g. the Force Shield cannot be fired over empty ground, so will display an
alternate cursor to indicate this).

The :tag:`NoCursor.*` flags default to the same value as their :tag:`Cursor.*`
counterparts.

.. index:: Super Weapons; Custom SW Cursors.

.. versionadded:: 0.1

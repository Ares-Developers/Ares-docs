Mouse Cursors
~~~~~~~~~~~~~

For several features :game:`Ares` allows to customize mouse cursors. Mouse
cursors can be defined in two ways: As a set of six separate tags, or using a
single tag and comma separated values.

In the following list, :tag:`[Section]BaseTag` represents the cursor's base
name. Replace this with the actual name. The default values depend on the base.

:tagdef:`[Section]BaseTag.Frame=integer`
  Starting frame of the cursor from :file:`mouse.sha`. The first frame is
  :value:`0`.

:tagdef:`[Section]BaseTag.Count=integer`
  Number of frames in the animated cursor.

:tagdef:`[Section]BaseTag.Interval=integer`
  The rate to animate the cursor. Default is :value:`5`.

:tagdef:`[Section]BaseTag.MiniFrame=integer`
  Same as :tag:`BaseTag.Frame`, except this is for the mouse cursor when
  positioned on the minimap. Set this to :value:`-1` to disable the minimap
  cursor and to only allow players to click on the battlefield.

:tagdef:`[Section]BaseTag.MiniCount=integer`
  Same as :tag:`BaseTag.Count`, except this is for the mouse cursor when
  positioned on the minimap.

:tagdef:`[Section]BaseTag.HotSpot=HotSpotX,HotSpotY`
  Specifies the coordinates on the cursor that are considered to be the 'tip'
  that is, the point from which the click event will handled. HotSpotX should
  be one of :value:`Left`, :value:`Center` or :value:`Right`. HotSpotY should
  be one of :value:`Top`, :value:`Middle` or :value:`Bottom`. For example,
  :tag:`BaseTag.HotSpot=Left,Top` will treat the top-left corner of the cursor
  as the tip. Default is :value:`Center,Middle`.

All these tags can be defined by putting them into a single line, using the same
values as described above:

:tagdef:`[Section]BaseTag=cursor definition`
  Enter the values from above in the given order, separated by commas:
  :value:`Frame,Count,Interval,MiniFrame,MiniCount,HotSpotX,HotSpotY`.

  .. note:: You cannot directly use the same definitions as used with other
    patches for :game:`Yuri's Revenge`, because :game:`Ares` uses descriptive
    names instead of numbers for the HotSpotX,HotSpotY parts. To convert the
    values, replace :value:`0` by either :value:`Left` or :value:`Top`,
    \ :value:`12345` by either :value:`Center` or :value:`Middle`, and
    \ :value:`54321` by either :value:`Right` or :value:`Bottom`.

.. index:: Mouse Cursors; Defining a Cursor

.. versionadded:: 0.1
.. versionchanged:: 0.8

Cursors
```````

:game:`Ares` allows you to specify custom mouse cursors for the super weapon,
using the following flags. See :doc:`Mouse Cursors </new/cursors>` on how to
define them.

:tagdef:`[SuperWeapon]Cursor=cursor definition`
  Cursor to use when it is ok to fire the super weapon at the given location.
  Defaults to the Attack cursor, if not stated otherwise.

:tagdef:`[SuperWeapon]NoCursor=cursor definition`
  Cursor to use when the super weapon is not allowed to fire at the given
  location. This may be because the selected target is not of the required type
  or its owner is not allowed, or the target is out of range, or there is no
  designator nearby. Defaults to the Pointer cursor, if not stated otherwise.

.. index:: Super Weapons; Custom Cursors.

.. versionadded:: 0.1

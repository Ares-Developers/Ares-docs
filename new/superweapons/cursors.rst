Cursors
```````

:game:`Ares` allows you to specify custom mouse cursors for the super weapon,
using the following flags. See :doc:`Mouse Cursors </new/mousecursors>` on how
to define them.

:tagdef:`[SuperWeapon]Cursor=mouse cursor`
  Cursor to use when it is ok to fire the super weapon at the given location.
  Defaults to :value:`Attack`, if not stated otherwise.

:tagdef:`[SuperWeapon]NoCursor=mouse cursor`
  Cursor to use when the super weapon is not allowed to fire at the given
  location. This may be because the selected target is not of the required type
  or its owner is not allowed, or the target is out of range, or there is no
  designator nearby. Defaults to :value:`Disallowed`, if not stated otherwise.

.. index:: Super Weapons; Custom Cursors.

.. versionadded:: 0.1
.. versionchanged:: 0.D

.. index::
  Passengers; Allow only specific passenger types in transports
  Transports; Allow only specific passenger types

Specific Passengers
~~~~~~~~~~~~~~~~~~~

Additionally to the checks for :tag:`Size` and :tag:`SizeLimit`, it is possible
to allow passengers to enter depending on their type.

:tagdef:`[TechnoType]Passengers.Allowed=list of TechnoTypes`
  The list of allowed passenger types. If this contains at least one type, all
  other types are not allowed to enter this object. If you want to prevent all
  units from entering, set this to either a dummy unit or a
  :type:`BuildingType`.

:tagdef:`[TechnoType]Passengers.Disallowed=list of TechnoTypes`
  The list of types that are not allowed to enter this object.

.. versionadded:: 0.A
.. versionchanged:: 2.0


Ignoring Passenger Size
~~~~~~~~~~~~~~~~~~~~~~~

Transports can ignore the actual size of its passengers and use up one slot for
each only.

:tagdef:`[UnitType]Passengers.BySize=boolean`
  Whether passengers will take up as much space in the cargo hold as their
  :tag:`Size` instead of taking up only one seat no matter the size of the
  object. If :value:`no`, the transport can always contain up to
  :tag:`Passengers` units. Defaults to :value:`yes`.

  .. note:: :tag:`SizeLimit` is always respected. A too large unit will still
    not be able to enter.

.. versionadded:: 2.0

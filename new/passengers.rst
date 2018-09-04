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

.. index::
  Passengers; Pre-fill units like a Troop Crawler
  Transports; Pre-fill with passengers like a Troop Crawler
  Buildings; Pre-fill with occupants
  Universe; Pre-filled Troop Crawlers

Initial Payload (Troop Crawlers)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :game:`Generals` the Chinese have the Troop Crawler, a vehicle that comes
pre-filled with Red Guard infantry right from the factory. :game:`Ares` adds
this feature to :game:`Yuri's Revenge`.

Buildings must either have :tag:`CanBeOccupied=yes` or :tag:`InfantryAbsorb=yes`
set. Other buildings are not supported to have initial payload. Buildings are
only allowed to have :type:`InfantryType` payload.

Occupiable buildings will be filled with up to :tag:`MaxNumberOccupants`
infantry, other buildings and units will be filled with up to :tag:`Passengers`
units. It's the responsibility of the modder to check :tag:`Size` and
:tag:`SizeLimit`.

:type:`InfantryType`\ s cannot have initial payload.

:tagdef:`[TechnoType]InitialPayload.Types=list of TechnoTypes`
  The types of the initial payload this object is created with. Types can be
  mentioned more than once, or the corresponding :tag:`InitialPayload.Nums` can
  be used to repeat a type.

  :type:`BuildingType`\ s and :type:`AircraftType`\ s are not valid. Buildings
  are only allowed to have :type:`InfantryType` payload. Types themselves having
  initial payload are not supported, because this could create infinite loops.

:tagdef:`[TechnoType]InitialPayload.Nums=list of integers`
  The optional numbers of times each type from :tag:`InitialPayload.Types` will
  be added.

  If this list contains fewer items than the :tag:`InitialPayload.Types` list,
  the last number is used as count for all following types. If this tag is not
  set, all counts are assumed to be :value:`1`.

.. versionadded:: 0.A

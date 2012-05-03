Reverse Engineer logic
~~~~~~~~~~~~~~~~~~~~~~

In :game:`Red Alert 2`, the Cloning Vats reverse-engineered any infantry it was
sent into. :game:`Ares` not just reenables this logic but also enables
customization.

:tagdef:`[BuildingType]ReverseEngineersVictims=boolean`
  Enables the reverse-engineering logic. Defaults to :value:`no`.
:tagdef:`[BuildingType]SpyEffect.UndoReverseEngineer=boolean`
  Enables Spies to disable all reverse-engineered technology from that building.
  Defaults to :value:`no`.
:tagdef:`[InfantryOrVehicle]CanBeReversed=boolean`
  Allows the unit to be reverse-engineered. Defaults to :value:`yes`.

.. note:: Currently :tag:`Grinding=yes` is needed to the reverse-engineering
  building to have this logic working. Also, reverse-engineered units will
  ignore :tag:`Prerequisite`, :tag:`PrerequisiteLists`,
  \ :tag:`PrerequisiteOverride`, :tag:`StolenTech`, both old and new models,
  \ :tag:`TechLevel`, :tag:`RequiredHouses` and :tag:`ForbiddenHouses`, but
  obeying :tag:`BuildLimit`, :tag:`PrerequisiteTheaters`,
  \ :tag:`NegativePrerequisite`, :tag:`Factory` and :tag:`Naval` settings.

.. note:: While this logic appears to be working, there have also been some
  minor bugs related to this feature. Be advised.

When you are the owner of the reversing facility, reverse-engineering any
:type:`InfantryType` for the first time will play
:value:`EVA_ReverseEngineeredInfantry` and :value:`EVA_NewTechnologyAcquired`;
reverse-engineering any :type:`VehicleType` for the first time will play
:value:`EVA_ReverseEngineeredVehicle` and :value:`EVA_NewTechnologyAcquired`.
The undo-reversing spy effect will play :value:`EVA_TechnologyStolen`.

.. index:: Prerequisites; Reverse-Engineering logic.

.. versionadded:: 0.2

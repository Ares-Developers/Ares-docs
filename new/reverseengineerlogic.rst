Reverse Engineer logic
~~~~~~~~~~~~~~~~~~~~~~

In :game:`Red Alert 2`, the Cloning Vats reverse-engineered any infantry it was
sent into. :game:`Ares` not just reenables this logic but also enables
customization.

:[BuildingType]ReverseEngineersVictims= (boolean): Enables the
  reverse-engineering logic. Defaults to :value:`no`.
:[BuildingType]SpyEffect.UndoReverseEngineer= (boolean): Enables Spies to
  disable all reverse-engineered technology from that building. Defaults to
  :value:`no`.
:[InfantryType]/[VehicleType]CanBeReversed= (boolean): Allows the unit to be
  reverse-engineered. Defaults to :value:`yes`.

.. note:: Currently :tag:`Grinding=yes` is needed to the reverse-engineering
  building to have this logic working. Also, reverse-engineered units will
  ignore :tag:`Prerequisite`, :tag:`PrerequisiteLists`,
  \ :tag:`PrerequisiteOverride`, :tag:`StolenTech`, both old and new models,
  \ :tag:`TechLevel`, :tag:`RequiredHouses` and :tag:`ForbiddenHouses`, but
  obeying :tag:`BuildLimit`, :tag:`PrerequisiteTheaters`,
  \ :tag:`NegativePrerequisite`, :tag:`Factory` and :tag:`Naval` settings.

.. note:: While this logic appears to be working, there have also been some
  minor bugs related to this feature. Be advised.

.. index:: Prerequisites; Reverse-Engineering logic.

.. versionadded:: 0.2

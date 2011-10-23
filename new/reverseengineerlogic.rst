Reverse Engineer logic
~~~~~~~~~~~~~~~~~~~~~~

In Red Alert 2, the Cloning Vats reverse-engineered any infantry it
was sent into. Ares not just reenables this logic but also enables
customization.

:[BuildingType]ReverseEngineersVictims= ( boolean, defaults to no ):
  Enables the reverse-engineering logic.
:[BuildingType]SpyEffect.UndoReverseEngineer= ( boolean, defaults to
  no ): Enables Spies to disable all reverse-engineered technology from
  that building.
:[InfantryType]/[VehicleType]CanBeReversed= ( boolean, defaults to yes
  ): Allows the unit to be reverse-engineered.


NB: Currently `Grinding=yes` is needed to the reverse-engineering
building to have this logic working. Also, reverse-engineered units
will ignore `Prerequisite=`, `PrerequisiteLists`,
`PrerequisiteOverride`, `StolenTech`, both old and new models,
`TechLevel`, `RequiredHouses` and `ForbiddenHouses`, but obeying
`BuildLimit`, `PrerequisiteTheaters`, `NegativePrerequisite`,
`Factory=` and `Naval=` settings.

NB: While this logic appears to be working, there have also been some
minor bugs related to this feature. Be advised.
Reverse-Engineering logic. ReverseEngineersVictims=
SpyEffect.UndoReverseEngineer= CanBeReversed=
.. versionadded:: 0.2



<<<SEPARATOR>>>

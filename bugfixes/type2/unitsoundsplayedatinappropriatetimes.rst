Unit Sounds Played At Inappropriate Times
`````````````````````````````````````````

When an InfantryType with `MovementZone=AmphibiousDestroyer` was
carried between water and land inside an 'open topped' vehicle (e.g. a
Nighthawk converted into a flying Battle Fortress), their
`EnterWaterSound`/ `ExitWaterSound` would be played. Now, these sounds
will only be played when the InfantryType themselves physically
enters/leaves water.

.. versionadded:: 0.1



<<<SEPARATOR>>>

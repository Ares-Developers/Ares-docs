InfantryElectrocuted
~~~~~~~~~~~~~~~~~~~~

The animation displayed for a dying InfantryType when the warhead that
killed them had `InfDeath=5` used to be hard-coded to the second
animation from the `[Animations]` list. You can now specify
`[AudioVisual]InfantryElectrocuted=` instead. If
`InfantryElectrocuted` is not defined then the game will search for an
animation named "ELECTRO", before finally falling back to the second
animation like before. Animation for `InfDeath=5` can be overriden
using `InfantryElectrocuted=` (instead of using the second animation
from [Animations]). InfantryElectrocuted=

.. versionadded:: 0.1



<<<SEPARATOR>>>

SpyPlane.Count Decoupled From AllyParaDropNum
`````````````````````````````````````````````

If you set `AllyParaDropNum=` to a list of integers so as to send
multiple InfantryTypes in the paradrop (and thus multiple paradrop
planes) then the SpyPlane super weapon would also send the same number
of planes as there were elements in that list. In Ares, the number of
spy planes sent out is now specified by the super weapon's own
`SpyPlane.Count=` flag (which defaults to 1). SpyPlane.Count decoupled
from AllyParaDropNum.

.. versionadded:: 0.1



<<<SEPARATOR>>>

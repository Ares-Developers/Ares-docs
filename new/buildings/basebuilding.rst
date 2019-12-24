.. index:: Bases; Disable extending base space for the AI

Extending Base Space of the AI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AI's base space is extended by any building that is not considered a
vehicle, and unrestricted by :tag:`BaseNormal`, which only applies to human
players. :game:`Ares` adds an option to disable extending base space.

:tagdef:`[BuildingType]AIBaseNormal=boolean`
  Whether this building will extend the base space of the AI player. Defaults to
  :value:`no` if both :tag:`UndeploysInto=` is set and
  :tag:`ResourceGatherer=yes`, otherwise defaults to whether the building is
  considered a vehicle.

.. versionadded:: 3.0


.. index:: Bases; Prefer placing buildings in the AI's inner base

Prefer to build in the AI's Inner Base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Preferrably placing Stealth Generators in the center of the base rather than on
the perimeter was a side effect of :tag:`CloakGenerator=yes` in
:game:`Tiberian Sun`. This feature has been recreated and made optional.

:tagdef:`[BuildingType]AIInnerBase=boolean`
  Whether the AI prefers to place this building closer to the center of its
  base. Use this for buildings that are to be protected or that provide a ranged
  effect that works best if it covers large portions of the base. Defaults to
  :value:`yes` if :tag:`CloakGenerator=yes`, to :value:`no` otherwise.

  .. note:: The larger the building foundation, the more unlikely it will be for
    the AI to find a place to build it near the base center in late game, in
    which case the game will fall back to the original logic and find a place in
    the perimeter.

.. versionadded:: 3.0

Availability
````````````

The availability of super weapons can be restricted by other factors than having
a building providing the super weapon. The building almost behaves as if it does
not have this super weapon. For example, if a super weapon is not accessible,
EVA will not announce its detection once the building is placed.

This does not affect the way :tag:`DisableableFromShell` works. Only the super
weapon set as :tag:`SuperWeapon` is checked for this tag, and the building
becomes unbuildable even if the super weapon is unavailable.

Even if all super weapons a building provides are disabled by whatever
restriction, it will still play the Super animation.


.. index::
  Super Weapons; Availability by country
  Countries; Super Weapon availability

Require a Country
-----------------

Access to super weapons can be restricted by the owning player's country. If the
country is not one of the required houses or it is a forbidden house, the super
weapon will not become available and the cameo will never appear.

:tagdef:`[SuperWeapon]SW.RequiredHouses=list of HouseTypes`
  Specifies the houses that have access to this super weapon. All other houses
  are forbidden from using it, and it will not become available for them.
  Defaults to all houses.
:tagdef:`[SuperWeapon]SW.ForbiddenHouses=list of HouseTypes`
  Specifies the houses that can never obtain this super weapon. All other houses
  are not denied access to it, but they also have to satisfy the
  :tag:`SW.RequiredHouses` settings for it to become available. Defaults to
  :value:`none`.

.. versionadded:: 0.9


.. index:: Super Weapons; AuxBuilding and negative AuxBuilding

Auxiliary Buildings (:captiontag:`AuxBuilding`)
-----------------------------------------------

The :tag:`AuxBuilding` feature was used in :game:`Tiberian Sun` to make the
Chemical Missile super weapon work. The Missile Silo provided both the Multi
Missile and the Chemical Missile, but the latter also required the player to own
a Tiberium Waste Facility to become available. :game:`Ares` expands this logic.

Multiple auxiliary building types are supported, and access to super weapons can
be removed again. This allows for two buildings to provide a single super weapon
and also to replace normal super weapons with alternative versions.

:tagdef:`[SuperWeapon]SW.AuxBuildings=list of BuildingTypes`
  Specifies the auxiliary buildings without which this super weapon cannot
  become available. The player has to own at least one building of any of these
  types to get access to this super weapon. Defaults to :value:`none`.

  .. note:: Use this instead of the original :tag:`AuxBuilding` tag if you want
    to have multiple auxiliary buildings.

:tagdef:`[SuperWeapon]SW.NegBuildings=list of BuildingTypes`
  Specifies the negative auxiliary buildings whose presence will cause the super
  weapon to become unavailable. This super weapon can become available only if
  the player does not own any building of any of these types. Defaults to
  :value:`none`.

The original :tag:`AuxBuilding` tag now works well together with super weapons
provided by building upgrades. A super weapon on a building upgrade will only
become available if its :tag:`AuxBuilding` requirement is satisfied.

.. warning:: Building upgrades do not constitute valid prerequisites for super
  weapons and thus do not suffice :tag:`AuxBuilding`, :tag:`SW.AuxBuildings` or
  \ :tag:`SW.NegBuildings`.

.. warning:: Super weapons using auxiliary building logics to restrict their
  availability do not support building animations.

.. versionadded:: 0.9


.. index:: Super Weapons; Available only for human or AI players

Only for Human or AI Players
----------------------------

Super weapons can be restricted to be used by houses controlled by human or AI
players only. This allows to hide special super weapons the AI might use to gain
an advantage from human players.

:tagdef:`[SuperWeapon]SW.AllowPlayer=boolean`
  Whether this super weapon will be available to human players. Defaults to
  :value:`yes`.

:tagdef:`[SuperWeapon]SW.AllowAI=boolean`
  Whether this super weapon will be available to AI players. Defaults to
  :value:`yes`.

.. versionadded:: 3.0


.. index:: Super Weapons; Available only a number of times

Limited Number of Shots
-----------------------

Super weapons can become unavailable after having been fired a certain number of
times. The super weapon cameo will disappear after the super weapon became
unavailable.

:tagdef:`[SuperWeapon]SW.Shots=integer`
  How often this super weapon is allowed to fire before becoming unavailable.
  Use :value:`-1` to allow unlimited firing. Is not supported for Charge Drain
  super weapons. Defaults to :value:`-1`.

.. note:: Super weapons granted by crates or map actions will also count against
  this limit. This might change in the future.

.. versionadded:: 3.0


.. index:: Super Weapons; Available without building

Always Granted Without Building
-------------------------------

With :game:`Ares` it is possible to use super weapons that are not tied to a
building that provides them. Instead, the always granted super weapon will
become immediately.

This setting still respects :tag:`AuxBuilding`, :tag:`SW.AuxBuidings`,
:tag:`SW.NegBuildings`, :tag:`SW.ForbiddenHouses`, :tag:`SW.RequiredHouses`,
:tag:`SW.AllowPlayer` and :tag:`SW.AllowAI`.

:tagdef:`[SuperWeapon]SW.AlwaysGranted=boolean`
  Whether this super weapon is not provided by any particular building but is
  instead always available as long as the player has not been defeated. Defaults
  to :value:`no`.

.. versionadded:: 3.0


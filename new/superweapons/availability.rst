Availability
````````````

The availability of super weapons can be restricted by other factors than having
a building providing the super weapon. The building almost behaves as if it does
not have this super weapon. For example, if a super weapon is not accessible,
EVA will not announce its detection once the building is placed.

This does not affect the way :tag:`DisableableFromShell` works. Only the super
weapon set as :tag:`SuperWeapon` is checked for this tag, and the building
becomes unbuildable even if the super weapon is unavailable.


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

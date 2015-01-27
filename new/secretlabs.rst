Secret Labs
~~~~~~~~~~~

The original Secret Lab system had three separate global flags to control the
boons and did not allow for :type:`AircraftTypes` to be granted. Secret Lab
logic also had some flaws which have been resolved (see :doc:`Type 1 Fixes
</bugfixes/type1/index>`).

In :game:`Ares`, the boon is only picked after the building is first captured by
a :tag:`MultiplayPassive=no` country, or assigned to it if pre-placed on the
map. The boon ultimately offered is picked at random, but only boons that are
not presently buildable by the owner of the Secret Lab are eligible to be
selected.

This logic has been extended with the following 'per building' flags.
:tag:`SecretLab=yes` must be set on the building before it will be treated as a
Secret Lab and so allow these flags to be considered.

:tagdef:`[Building]SecretLab.PossibleBoons=list of TechnoTypes`
  Specifies all the buildings, vehicles, infantry and aircraft that this
  particular building could potentially award as a secret lab boon. Defaults to
  all items from :tag:`[General]SecretInfantry`, :tag:`[General]SecretUnits`
  and :tag:`[General]SecretBuildings`.
:tagdef:`[Building]SecretLab.GenerateOnCapture=boolean`
  Whether the Secret Lab shall re-pick the boon to be offered every time the
  building is captured by or assigned to a :tag:`MultiplayPassive=no` country.
  Otherwise, the boon is picked only once, the first time it is assigned to such
  country. Defaults to :value:`no`.

Each possible boon can specify the following flags. Both are only checked at the
time a boon is picked, so if :tag:`SecretLab.GenerateOnCapture=no`, then the
boon might still be obtained by a forbidden country, or denied a required
country if the Secret Lab is captured later on.

.. note:: This means that such Secret Labs may appear to disobey
  \ :tag:`SecretLab.RequiredHouses` and :tag:`SecretLab.ForbiddenHouses` when
  captured. This is not a bug.

:tagdef:`[Boon]SecretLab.RequiredHouses=list of countries`
  Specifies which countries are allowed to get this unit as a Secret Lab boon.
  Defaults to all houses.
:tagdef:`[Boon]SecretLab.ForbiddenHouses=list of countries`
  Specifies which countries are not allowed to get this unit as a Secret Lab
  boon. Defaults to none.

.. index:: BuildingTypes; Per-building secret lab boons.
.. index:: BuildingTypes; Secret Lab options.

.. versionadded:: 0.1
.. versionchanged:: 0.9

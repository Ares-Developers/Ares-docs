Secret Labs
~~~~~~~~~~~

Secret Lab logic had some flaws which have been resolved (see :doc:`Type 1 Fixes
</bugfixes/type1/index>`). In addition to those fixes, Secret Lab logic has been
extended with the following 'per building' flags. :tag:`SecretLab=yes` must be
set on the building before it will be treated as a Secret Lab and so allow these
flags to be considered.

:tagdef:`[Building]SecretLab.PossibleBoons=list of TechnoTypes`
  Specifies all the buildings, vehicles, infantry and aircraft that this
  particular building could potentially award as a secret lab boon. The original
  Secret Lab system had three separate flags to control this which were all
  global and did not allow for :type:`AircraftTypes`.
:tagdef:`[Building]SecretLab.GenerateOnCapture=boolean`
  The boon offered by a Secret Lab is picked when the building is first created
  (or on map load if it is pre-placed). If
  :tag:`SecretLab.GenerateOnCapture=yes` is set then every time the building is
  captured it will re-pick the boon to be offered. Defaults to :value:`no`.


Each possible boon can specify the following flags...

:tagdef:`[Boon]SecretLab.RequiredHouses=list of countries`
  Which countries are allowed to get this unit as a secret lab boon. This is
  only checked when the boon is picked so if
  :tag:`SecretLab.GenerateOnCapture=no` then the boon can still be obtained by a
  country not on the :tag:`SecretLab.RequiredHouses` list (if the original
  owner's country is on the list).
:tagdef:`[Boon]SecretLab.ForbiddenHouses=list of countries`
  Which countries are not allowed to get this unit as a secret lab boon. This is
  only checked when the boon is picked so if
  :tag:`SecretLab.GenerateOnCapture=no` then the boon can still be obtained by a
  country that is on the :tag:`SecretLab.RequiredHouses` list (if the original
  owner's country is not on the list).


The boon ultimately offered is picked at random, but only boons that are not
presently buildable by the owner of the Secret Lab (civilian in the case of
pre-placed buildings without :tag:`SecretLab.GenerateOnCapture=yes`) are
eligible to be picked.

.. note:: This means that such Secret Labs may appear to disobey
  \ :tag:`SecretLab.RequiredHouses` and :tag:`SecretLab.ForbiddenHouses` when
  captured. This is not a bug.

.. index:: BuildingTypes; Per-building secret lab boons.

.. versionadded:: 0.1

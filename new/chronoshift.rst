Chronoshift
~~~~~~~~~~~

These options specify what the Chronosphere should do with an object.

:tagdef:`[TechnoType]Chronoshift.Allow=boolean`
  Specifies whether this unit is allowed to be affected by the Chronosphere
  super weapon. Otherwise it will be ignored. Defaults to :value:`yes`.

:tagdef:`[BuildingType]Chronoshift.IsVehicle=boolean`
  Specifies whether this building is actually a deployed vehicle and should be
  chronoshifted by the Chronosphere super weapon if it affects units and
  :tag:`Chronosphere.ReconsiderBuildings=yes` is set. On the other hand this
  building will not be considered a building any more and thus will be ignored
  by a Chronosphere that doesn't affect units. Defaults to :value:`no`.

Units can be made immune to chronoshift-crushing:

:tagdef:`[TechnoType]Chronoshift.Crushable=boolean`
  If set to :value:`no`, this unit can no longer be crushed by chronoshifting
  units onto it. Instead, the chronoshifting unit will be destroyed. Does not
  apply to :type:`BuildingType`\ s. Defaults to :value:`yes`.

Globally disallow chronoshifting infantry to crush non-infantry:

:tagdef:`[General]ChronoInfantryCrush=boolean`
  If set to :value:`no`, infantry will die when being chronoshifted onto tanks
  instead of destroying the tanks. Defaults to :value:`yes`.

.. index:: Chronosphere; Per-unit Chronosphere options.

.. versionadded:: 0.2
.. versionchanged:: 0.E

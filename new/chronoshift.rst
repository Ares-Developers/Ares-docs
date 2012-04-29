Chronoshift
~~~~~~~~~~~

These options specify what the Chronosphere should do with an object.

:[TechnoType]Chronoshift.Allow= (boolean): Specifies whether this unit is
  allowed to be affected by the Chronosphere super weapon. Otherwise it will be
  ignored. Defaults to :value:`yes`.
:[BuildingType]Chronoshift.IsVehicle= (boolean): Specifies whether this building
  is actually a deployed vehicle and should be chronoshifted by the Chronosphere
  super weapon if it affects units and
  :tag:`Chronosphere.ReconsiderBuildings=yes` is set. On the other hand this
  building will not be considered a building any more and thus will be ignored
  by a Chronosphere that doesn't affect units. Defaults to :value:`no`.

.. index:: Chronosphere; Per-unit Chronosphere options.

.. versionadded:: 0.2

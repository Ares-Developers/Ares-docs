Chronoshift
~~~~~~~~~~~

These options specify what the Chronosphere should do with an object.
Per-unit Chronosphere options.

:[TechnoType]Chronoshift.Allow= (boolean): Specifies whether this unit
  is allowed to be affected by the Chronosphere super weapon. Otherwise
  it gets ignored. Defaults to `yes`. Chronoshift.Allow=
:[BuildingType]Chronoshift.IsVehicle= (boolean): Specifies whether
  this building is actually a deployed vehicle and should be
  chronoshifted by the Chronosphere super weapon if it affects units and
  `Chronosphere.ReconsiderBuildings=yes` is set. On the other hand this
  building will not be considered a building any more and thus will be
  ignored by a Chronosphere that doesn't affect units. Defaults to `no`.
  Chronoshift.IsVehicle=


.. versionadded:: 0.2

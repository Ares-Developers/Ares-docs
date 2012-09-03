Lightning Rods
~~~~~~~~~~~~~~

Lightning rods attract Lightning Storms and optionally modify their
damage. Rudimentary Lightning Rods.

:[BuildingType]LightningRod= (boolean): Specifies whether this
  building attracts lightning. If this building is the object to a cloud
  randomly created, the cloud will be created just above the building.
  Defaults to `no`. LightningRod=
:[BuildingType]LightningRod.Modifier= (float modifier): Buildings with
  `LightningRod=yes` set being hit by lightning get the damage
  multiplied by this value. Values less than 1.0 reduce damage, larger
  values increase the damage. Defaults to `1.0`. LightningRod.Modifier=


NB: This logic is likely to be expanded in future versions.

.. versionadded:: 0.2

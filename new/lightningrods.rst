Lightning Rods
~~~~~~~~~~~~~~

Lightning rods attract Lightning Storms and optionally modify their damage.

:[BuildingType]LightningRod= (boolean): Specifies whether this building attracts
  lightning. If this building is the closest object to a cloud created randomly,
  the cloud will be created just above the building. Defaults to :value:`no`.
:[BuildingType]LightningRod.Modifier= (float - modifier): Buildings with
  :tag:`LightningRod=yes` set being hit by lightning get the damage multiplied
  by this value. Values less than 1.0 reduce damage, larger values increase the
  damage. Defaults to :value:`1.0`.

.. note:: This logic is likely to be expanded in future versions.

.. index:: Buildings; Rudimentary Lightning Rods.

.. versionadded:: 0.2

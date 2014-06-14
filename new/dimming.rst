Dimming Deactivated Units
~~~~~~~~~~~~~~~~~~~~~~~~~

The level deactivated voxel :type:`VehicleTypes` are dimmed can be configured
here. The first applicable value is used, the other values will not be
considered. That is, if an unpowered unit is under EMP, :tag:`DeactivateDimEMP`
is used. This is purely cosmetic and the order may change in the future. A value
of :value:`1.0` disables the dimming effect. Supported range is :value:`0.0` to
:value:`1.0`, higher values will brighten the unit.

.. note:: Shp :type:`VehicleTypes`, as well as :type:`BuildingTypes`,
  \ :type:`AircraftTypes` and :type:`InfantryTypes` are not affected by dimming.

:tagdef:`[AudioVisual]DeactivateDimEMP=float - multiplier`
  The light level for voxel units under EMP. See :doc:`EMP logic
  </restored/emp>`. Defaults to :value:`0.8`.

:tagdef:`[AudioVisual]DeactivateDimOperator=float - multiplier`
  The light level for unoperated voxel units. See :doc:`Operator logic
  </new/operator>`. Defaults to :value:`0.65`.

:tagdef:`[AudioVisual]DeactivateDimPowered=float - multiplier`
  The light level for unpowered voxel units. See :doc:`PoweredBy logic
  </new/newpoweredunitlogic>`. Defaults to :value:`0.5`.

.. index:: Units; Dimming deactivated voxel VehicleTypes

.. versionadded:: 0.7

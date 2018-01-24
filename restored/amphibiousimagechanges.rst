.. index::
  Vehicles; Amphibious vehicles can change their image when moving between water/land
  Art; Amphibious vehicles can change their image when moving between water/land

========================
Amphibious Image Changes
========================
In :game:`Tiberian Sun`, the Amphibious APC would appear to sink into the water.
This was achieved by changing the imagery from :file:`apc.vxl` to
:file:`apcw.vxl`. With :game:`Ares`, you can now specify:

:tagdef:`[VehicleType]WaterImage=VehicleType`
  This allows the amphibious unit's image to change from :file:`XXXX.shp` or
  :file:`XXXX.vxl` (defined by :tag:`Image=`) to :file:`YYYY.shp` or
  :file:`YYYY.vxl` (defined by :tag:`[WaterImage]Image=`) when in water, similar
  to :tag:`UnloadingClass`.

  Please note that SHP units cannot have a voxel :tag:`WaterImage`, and vice
  versa. The :type:`VehicleType` has to be defined under :tag:`[VehicleTypes]`.

.. versionadded:: 0.1

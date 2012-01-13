.. index:: WaterImage= Amphibious vehicles can change their image when moving between water/land.

========================
Amphibious Image Changes
========================
In Tiberian Sun, the Amphibious APC would appear to sink into the
water. This was achieved by changing the imagery from :file:`apc.vxl` to
:file:`apcw.vxl`. With Ares, you can now specify:

``[VehicleType]`` |>| ``WaterImage= (VehicleType)``
	This allows the amphibious unit's image to change from :file:`XXXX.shp` or
	:file:`XXXX.vxl` (defined by ``Image=``) to :file:`YYYY.shp` or :file:`YYYY.vxl` (defined by
	``[WaterImage]`` |>| ``Image=``) when in water, similar to UnloadingClass.
	Please note that SHP units cannot have a voxel WaterImage, and vice
	versa. The VehicleType has to be defined under ``[VehicleTypes]``.

.. versionadded:: 0.1


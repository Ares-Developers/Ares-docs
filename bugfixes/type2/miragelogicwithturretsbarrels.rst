.. index:: Mirage disguise; Turrets and barrels will be disguised with the unit.

=================================
Mirage Logic with Turrets/Barrels
=================================

In Yuri's Revenge, using the Mirage disguise logic on a VehicleType
with ``Turret=yes`` would result in the vehicle's turret not being
disguised. Ares fixes this behaviour so that associated turrets and
barrels will be disguised along with the unit's body.

.. versionadded:: 0.2

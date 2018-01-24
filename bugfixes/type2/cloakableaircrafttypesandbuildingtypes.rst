.. index:: Cloak; AircraftTypes and BuildingTypes can now be cloakable

=========================================================
Cloakable :type:`AircraftTypes` and :type:`BuildingTypes`
=========================================================

Until now, :type:`AircraftTypes` and :type:`BuildingTypes` have ignored the
existence of :tag:`Cloakable=yes`. Now, if this tag is included on the entry of
a :type:`BuildingType` or :type:`AircraftType`, it will cloak.

.. note:: \ :type:`AircraftTypes` will decloak when told to attack, not once
  they are within firing range.

.. versionadded:: 0.2

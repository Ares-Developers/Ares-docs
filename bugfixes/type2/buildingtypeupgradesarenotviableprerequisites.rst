.. index:: Upgrades; Building upgrades can now be used as prerequisites.

==========================================================
:type:`BuildingType` Upgrades Are Not Viable Prerequisites
==========================================================

Before :game:`Ares`, upgrades did not appear to work as prerequisites if you had
the upgrade, you still didn't satisfy the prerequisite. In fact, only the most
recently constructed :type:`BuildingType` would be checked to see if it had the
upgrade. With :game:`Ares`, all upgrades on all :type:`BuildingTypes` are
eligible to satisfy any prerequisite logic that a normal :type:`BuildingType`
can.

In addition, upgrades can now satisfy a super weapon's :tag:`AuxBuilding`.

.. versionadded:: 0.1

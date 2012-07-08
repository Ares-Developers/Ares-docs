.. index:: Ammo; Infantry and buildings will now reload ammo properly.

===========================================================================
:type:`BuildingTypes` and :type:`InfantryTypes` Do Not Reload Ammo Properly
===========================================================================

See `ModEnc://Ammo <http://modenc.renegadeprojects.com/Ammo>`_ for exact details
of this problem. Put simply, ammo/reloading logic did not work properly on
:type:`BuildingTypes` or :type:`InfantryTypes` and was essentially useless on
those object types. :game:`Ares` fixes this logic such that these object types
will now reload their ammo properly. Note that :type:`AircraftTypes` are
hard-coded to require docking to reload.

.. note:: \ :tag:`Hospital=yes` and :tag:`Armory=yes` buildings still not reload
  ammo.

.. versionadded:: 0.1

.. index::
  Vehicles; Paradrop works correctly
  Paradrops; Vehicles are paradropped correctly

=======================
Vehicle Paradrop Offset
=======================

Passengers of :type:`AircraftTypes` get paradropped out if the
\ :type:`AircraftType` fires its weapon. The passengers would always use the
infantry sub-cell positions for where they would be spawned, even if the
passenger were not an :type:`InfantryType`. This ultimately meant that vehicles
would appear to fall part-way into the ground upon landing. This error no longer
happens in :game:`Ares`.

The same problem also used to occur with vehicles paradropped from aircraft
with :tag:`Carryall=yes` set.

.. versionadded:: 0.1

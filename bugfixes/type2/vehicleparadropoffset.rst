.. index:: Paradrops; Vehicles that are paradropped will now be centered correctly on the cell they land on rather than being offset.

=======================
Vehicle Paradrop Offset
=======================

Passengers of AircraftTypes get paradropped out if the AircraftType
fires its weapon. The passengers would always use the infantry sub-
cell positions for where they would be spawned, even if the passenger
were not an InfantryType. This ultimately meant that vehicles would
appear to fall part-way into the ground upon landing. This error no
longer happens in Ares.
(The same problem also used to occur with vehicles paradropped from
aircraft with ``Carryall=yes`` set.)

.. versionadded:: 0.1

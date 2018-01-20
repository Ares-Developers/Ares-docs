.. index:: EVA; "New construction options" no longer announced if player does not have the correct factory type for a unit or does not own a building through Owner.

========================
New Construction Options
========================

One cause of the NCO bug (where the EVA will announce "new construction options"
when, in fact, there aren't any) was the game's failure to check if the player
had the appropriate factory type to build the unit concerned (e.g. a
:type:`VehicleType` factory for :type:`VehicleTypes`). Such a check will now
take place, thus removing this cause of the NCO bug.

.. versionadded:: 0.1

Another cause of the NCO bug is when a house is not listed as a
buildable building's owner. Ares's prerequisite system does not check
for that, thereby eliminating this type of bug.

Owners still affect AI base planning.

.. versionadded:: 0.2
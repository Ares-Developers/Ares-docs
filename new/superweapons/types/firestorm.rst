.. _firestorm:

:captiontag:`Type=Firestorm`
````````````````````````````

This superweapon is a recreation of the :game:`Tiberian Sun` Firestorm
superweapon.

When activated, all structures owned by the firing player that have
:tag:`Firestorm.Wall=yes` set will emit an energy field, blocking all hostile
projectiles (except those with :tag:`SubjectToFirestorm=no` set) from passing
through. The energy field also destroys any friend or foe unlucky (or stupid)
enough to come into direct contact with active cells.

:type:`BuildingTypes` with :tag:`Firestorm.Wall=yes` set will act as a section
of the Firestorm Wall and auto-connect to other nearby pieces (check the
original building's SHP from :game:`Tiberian Sun` to see how the art is
controlled).

This super weapon uses the old Charge/Drain logic: once activated, the effect
will persist for a duration determined by :tag:`SW.ChargeToDrainRatio`, after
which it will automatically shut down and the superweapon will restart its
charging process. Whilst the effect is active you can click the super weapon
button again to manually deactivate it, thus allowing the recharge process to
begin earlier and finish faster. See :ref:`Charge/Drain <charge-drain-sw>`.
Refer to `ModEnc <http://modenc.renegadeprojects.com/ChargeToDrainRatio>`_ for
more information about Charge/Drain logic.

In :game:`Tiberian Sun`, the Charge/Drain feature was disableable through an
INI flag (:tag:`[SuperWeapon]UseChargeDrain=no`) however: :game:`Ares` forces
this logic to be used regardless of the value of that flag. :game:`Ares` also
forces this super weapon to ignore its assigned :tag:`Action`, if any, as this
is required to make it activate from a single click of the sidebar icon.

The AI will not use this super weapon.

.. note:: The animations used by this logic are temporarily hard-coded to
  \ :value:`FSIDLE`, :value:`FSGRND` and :value:`FSAIR`, as was used in
  \ :game:`Tiberian Sun`.

.. note:: The AI has a lot of problems with targets behind an active Firestorm
  Wall, although this should not be a major problem due to the relatively small
  amount of game time that the Wall is active for.

.. index:: Super Weapons; Firestorm Wall

.. versionadded:: 0.1

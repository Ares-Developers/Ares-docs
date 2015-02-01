.. index:: OpenTopped; OpenTopped Gunner vehicles support passengers with Temporal weapons

===================================================================================
:captiontag:`OpenTopped` :captiontag:`Gunner`\ s and :captiontag:`Temporal` weapons
===================================================================================

:tag:`Gunner=yes` vehicles use the passenger's temporal device to fire  if it is
equipped with a :tag:`Temporal=yes` weapon. This can be done safely, and the
device is replaced once the infantry exits the vehicle. If the :tag:`Gunner=yes`
vehicle is also :tag:`OpenTopped=yes`, the infantry with the :tag:`Temporal=yes`
weapon inside is still supposed to fire on its own, but because it doesn't have
the temporal device any more, the game crashes.

:game:`Ares` prevents infantry that has its temporal device taken away by the
:tag:`Gunner` logic from firing out of an :tag:`OpenTopped` vehicle.

.. versionadded:: 0.9

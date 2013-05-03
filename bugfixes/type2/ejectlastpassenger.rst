.. index:: Transports; Turret-changing and gattling transports will eject all passengers.

========================================
Passengers and :captiontag:`TurretCount`
========================================

If :tag:`TurretCount` is larger than zero, a transport vehicle would not eject
the last passenger when deployed. Deploying the unit a second time ejected the
remaining passenger. This affected :type:`VehicleTypes` with charge turrets
(:tag:`IsChargeTurret=yes`), units with Gattling weapon systems
(:tag:`IsGattling=yes`) and IFVs (:tag:`Gunner=yes`).

Only :tag:`Gunner=yes` vehicles will keep the last passenger now. They handle
passenger pips in a special way as the first pip is separated from the others,
and it makes sense for them not to eject the passenger which is considered the
"driver" and which also controls the weapon used by the transport vehicle.

.. versionadded:: 0.3

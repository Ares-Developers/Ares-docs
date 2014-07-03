Anti-Vehicle (:captiontag:`AV`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :game:`Firestorm`, the Limpet Mine could attach to :type:`VehicleTypes` only:
It would ignore infantry and aircraft. This was achieved by not allowing players
to command the mine to attack objects directly, and by using the newly
introduced :tag:`AV`, which auto-acquired only vehicles.

.. note:: This logic uses this definition of *vehicles*: :type:`VehicleTypes` on
  the ground that are :tag:`Naval=no` and :tag:`ConsideredAircraft=no`. This
  includes hovering units.

Opposed to :game:`Tiberian Sun`, this does not override :tag:`AG` and :tag:`AA`,
for acquiring a new target and it can be defined independently of the two. This
means both being able to automatically acquire ground units but not vehicles, as
well as not acquiring other ground units while still being able to acquire
vehicles.

With :tag:`AV=no`, :game:`Ares` also prohibits targeting vehicles and players
will not get an attack cursor on them. Vehicles in the air fall into the
responsibility of :tag:`AA`, and :tag:`AV` does not interfere with targeting.

:tagdef:`[Projectile]AV=boolean`
  Whether this projectile can be fired at :type:`VehicleTypes` on the ground
  that are not :tag:`ConsideredAircraft=yes`. Defaults to :tag:`AG` for
  passive-acquiring targets; for firing it is enabled if :tag:`LandTargeting` is
  set to a value not equal to :value:`1`.

.. versionadded:: 0.7

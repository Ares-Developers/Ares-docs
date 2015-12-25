Manual Control
~~~~~~~~~~~~~~

No Manual Target Selection
``````````````````````````

Like :tag:`EMPulseCannon`, this disallows players to manually select targets,
but it neither prevents the object from picking its own targets automatically,
nor to retaliate.

:tagdef:`[TechnoType]NoManualFire=boolean`
  Whether players may not select targets for this type of object manually. If
  enabled, units will have to rely on auto-targeting and retaliation rules.
  Defaults to :value:`no`.

.. index:: Behavior; Disallow manual target selection, Hide attack cursor

.. versionadded:: 0.A


No Manual Passenger Unload
``````````````````````````

This setting disallows players to manually eject the passengers. This is useful
for vehicles that are no real transports, like :doc:`Chrono Prisons
</new/chronoprisons>`.

By default, passengers might still be ejected when the vehicle is destroyed. To
change this, set the :doc:`Passenger Survivor Chance </new/survivors>`
accordingly.

:tagdef:`[VehicleType]NoManualUnload=boolean`
  Whether this vehicle is disallowed to eject its passengers. If enabled, the
  owning player will not get deploy or no-deploy cursors. Defaults to
  :value:`no`.

.. index:: Behavior; Disallow manual passenger unload, Hide unload cursor

.. versionadded:: 0.A

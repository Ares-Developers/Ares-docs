Manual Control
~~~~~~~~~~~~~~

.. index::
  Behavior; Disallow manual target selection
  TechnoTypes; Disable attack cursor

No Manual Target Selection
``````````````````````````

Like :tag:`EMPulseCannon`, this disallows players to manually select targets,
but it neither prevents the object from picking its own targets automatically,
nor to retaliate.

:tagdef:`[TechnoType]NoManualFire=boolean`
  Whether players may not select targets for this type of object manually. If
  enabled, units will have to rely on auto-targeting and retaliation rules.
  Defaults to :value:`no`.

.. versionadded:: 0.A


.. index::
  Behavior; Disallow manual passenger unload
  TechnoTypes; Disable unload cursor

No Manual Passenger Unload
``````````````````````````

This setting disallows players to manually eject the passengers. This is useful
for vehicles that are no real transports, like :doc:`Chrono Prisons
</new/chronoprisons>`.

By default, passengers might still be ejected when the vehicle is destroyed. To
change this, set the :doc:`Passenger Survivor Chance </new/survivors>`
accordingly.

:tagdef:`[TechnoType]NoManualUnload=boolean`
  Whether this vehicle or aircraft is disallowed to eject its passengers. If
  enabled, the owning player will not get deploy or no-deploy cursors. Defaults
  to :value:`no`.

.. versionadded:: 0.A
.. versionchanged:: 2.0


.. index::
  Behavior; Disallow units to get an enter cursor over a transport
  TechnoTypes; Prevent players to send units into transports

No Manual Enter Transport
`````````````````````````

This cosmetic setting allows to hide the fact that a unit is a transport by
removing the enter and no-enter cursors.

This does not prevent units from entering by other means, like scripts, though.
Also, the AI will not respect this setting. Use the :doc:`Specific Passengers
</new/passengers>` feature to prevent this.

:tagdef:`[TechnoType]NoManualEnter=boolean`
  Whether units will not get an enter or no-enter cursor when on this object. If
  :value:`yes`, the select cursor is used, as if this unit is not a transport.
  Defaults to :value:`no`.

.. versionadded:: 0.B


.. index::
  Behavior; Disable Medics' Guard Area cursor on self
  Infantry; Medics that can deploy

No Guard Area on Self
`````````````````````

Medics usually get a guard area cursor on themselves so players can set them to
guard mode by clicking. This prevents infantry with negative damage weapons to
have deploy ability. :game:`Ares` adds a tag to turn this feature off.

:tagdef:`[InfantryType]NoSelfGuardArea=boolean`
  Whether infantry units with negative damage weapons get the guard area cursor
  on themselves. If :value:`no`, the guard area cursor will not take precedence,
  allowing other cursors like the deploy cursor to be shown. Defaults to
  :value:`no`.

.. versionadded:: 0.B

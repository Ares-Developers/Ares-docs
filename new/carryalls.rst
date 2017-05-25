Carryalls
~~~~~~~~~

Carryalls were a feature of :game:`Tiberian Sun`. :type:`AircraftTypes` with
:tag:`Carryall=yes` could pick up :type:`UnitTypes` from the battlefield, carry
them around the map and place them anywhere. The carryall logic was not used in
:game:`Red Alert 2` and was not updated for naval units and other new features.
:game:`Ares` updates the logic and adds new options.

If a unit can be picked up, the cursor named :value:`Tote` is shown. See how to
customize this :doc:`Mouse Cursor </new/mousecursors>`.

:tagdef:`[AircraftType]Carryall.SizeLimit=integer`
  The maximum :tag:`Size=` that this carryall can lift. Use :value:`-1` to allow
  any size. Defaults to :value:`-1`.

:tagdef:`[UnitType]Carryall.Allowed=boolean`
  Can this unit be picked up by a carryall? If not set, :tag:`Organic=yes` and
  :tag:`NonVehicle=yes` units cannot be picked up. If specified,
  :tag:`Carryall.Allowed` overrules those considerations. Currently it is not
  possible to "unset" this tag to use the default again. You have to set it
  explicitly.
  
  .. note:: Units infected with a Parasite (Terror Drone/Squid) cannot be picked
    up.

.. note:: For the Carryall to work it must have :tag:`AirportBound=no` and no
  \ :tag:`Dock=` set, otherwise they will be unable to pick up units.

.. note:: By default, carryalls can pick up vessels, which are :type:`UnitTypes`
  with :tag:`Naval=yes` set, but they cannot be placed back on water again. If a
  ship is placed on ground, it will explode and take the carryall with it. To
  prevent this, set :tag:`Carryall.Allowed=no` on the ship.

.. index:: Aircraft; Carryall logic updated.

.. versionadded:: 0.2

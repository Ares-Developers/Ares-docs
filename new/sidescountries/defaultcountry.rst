Country Defaults
~~~~~~~~~~~~~~~~

AI and Base-Building
--------------------

:tagdef:`[Country]AI.PowerPlants=list of BuildingTypes`
  A list of buildings that the AI will treat as this country's power plants.
  Defaults to :tag:`[General]GDIPowerPlant` for the first side, to
  :tag:`[General]ThirdPowerPlant` for the third side, and to
  :tag:`[General]NodRegularPower` and :tag:`[General]NodAdvancedPower` for the
  second side and all other sides.

.. versionadded:: 0.1


Paradrop Defaults
-----------------

:tagdef:`[Country]ParaDrop.Types=list of InfantryTypes and/or VehicleTypes`
  The units that will be paradropped by :tag:`Type=ParaDrop` super weapons (such
  as the one normally provided by a Tech Airport) for this country. Defaults to
  the corresponding side's :tag:`ParaDrop.Types=`.

  .. note:: The original flags used to control the paradrop units only accept
    \ :type:`InfantryTypes`. To include :type:`VehicleTypes` in a paradrop you
    *have to* use the new :tag:`ParaDrop.Types` and :tag:`ParaDrop.Num` flags.
:tagdef:`[Country]ParaDrop.Num=list of integers`
  The quantity of each corresponding unit (listed against :tag:`ParaDrop.Types`)
  that will be paradropped. Defaults to the corresponding side's
  :tag:`ParaDrop.Num=`.
:tagdef:`[Country]ParaDrop.Aircraft=AircraftType`
  The aircraft type that will be used to deliver paradrops. Defaults to the
  corresponding side's :tag:`ParaDrop.Aircraft=`.
:tagdef:`[Country]Parachute.Anim=Animation`
  This country's default parachute used if not overridden by a
  :type:`TechnoType`. Defaults to the corresponding side's
  :tag:`Parachute.Anim=`.

.. versionadded:: 0.2


Others
------

:tagdef:`[Country]VeteranBuildings=list of BuildingTypes`
  All buildings in this list start as veteran for this country and, if
  available, veteran cameos are displayed in the sidebar.

.. versionadded:: 0.4

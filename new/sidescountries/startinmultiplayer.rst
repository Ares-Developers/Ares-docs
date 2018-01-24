Start in Multiplayer
~~~~~~~~~~~~~~~~~~~~

.. index::
  Countries; Starting infantry and vehicles for multiplayer games
  Multiplayer; Starting infantry and vehicles

Starting Units
--------------

:tagdef:`[Country]StartInMultiplayer.Types=list of InfantryTypes and/or VehicleTypes`
  The custom list of potential units to start with in multiplayer games. If not
  set, the game selects the types by using :tag:`AllowedToStartInMultiplayer`.
  Only :type:`InfantryTypes` and :type:`VehicleTypes` are supported. Use
  :value:`<none>` to disable starting units for this country.

  .. note::  It is now supported to have no starting infantry. The game will no
    longer crash.

.. versionadded:: 0.D


.. index:: Multiplayer; Cost for one "unit" for calculating starting units

Fixed Global Unit Cost
----------------------

By default, the game will determine the average cost of a unit by summing up and
averaging all costs of units that could be used as starting units (only
considering countries that are in the current match). The Unit Count setting is
multiplied by this.

:tagdef:`[General]StartInMultiplayerUnitCost=integer - credits`
  The fixed amount of credits for one average unit. If not set, the game will
  use the method described above. In this case, :game:`Ares` will now output the
  inferred average unit cost into the log file.

.. versionadded:: 0.D


.. index::
  Countries; Start multiplayer games with a Construction Yard
  Multiplayer; Start games with a Construction Yard
  Construction Yards; Start with one in multiplayer games

Pre-Deployed MCV
----------------

This allows for countries to not have an MCV at the beginning of the match, as
well as for game modes where the base locations are fixed. Also, the initial
Construction Yard could be made different from the ones obtainable later in the
game.

:tagdef:`[Country]StartInMultiplayer.WithConst=boolean`
  Whether this country shall start with the first buildable building from
  :tag:`BuildConst` instead of a unit from :tag:`BaseUnit` when starting a
  multiplayer match. Defaults to :value:`no`.

.. versionadded:: 0.D

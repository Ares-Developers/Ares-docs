Sides & Countries
~~~~~~~~~~~~~~~~~

In the original game the sides and countries were, for the most part,
hard-coded. You could not add to, remove or reorder the 10 countries or 3 sides.
:game:`Ares`, however, makes these tasks possible - you can now have up to 16
fully functional countries and sides, and you can customize these in numerous
ways...

.. note:: Certain flags work properly for up to 32 countries, and yet others
  fail after merely 16 - it is recommended to not have any more than 16
  playable countries and 32 total countries. Put the playable countries first in
  the list, followed by the other countries.

.. index:: Sides; New sides & countries (including numerous enhancements).



Countries
`````````

Countries are specified in the :tag:`[Countries]` list in :file:`rulesmd.ini`.
Any country with :tag:`Multiplay=yes` set will appear in the country selection
drop-down list and be eligible for random selection if the player chooses
'Random'. Countries can be excluded from the 'random country' option, or given
differing weights.

The :tag:`[Countries]` list can contain up to 32 countries, however taunts
will only work for 16 of these.

Each country can be customized using the following flags in the country's INI
section:

.. warning:: The following filename specifications (where raw C-style format
  specifiers like %s are required) are going to be changed into safer versions
  in the future. The replacement style has not been decided yet.

:tagdef:`[Country]File.Flag=filename, *including* the .pcx extension`
  The PCX file to use for the country's flag, in the format "filename.pcx".
:tagdef:`[Country]File.ObserverBackground=filename, *including* the .pcx or .shp extension`
  The SHP or PCX file to use for the country's background in observer mode, in
  the format "filename.shp" or "filename.pcx". The size should be 121x96. The
  SHP file will be drawn using :file:`observer.pal`.
:tagdef:`[Country]File.ObserverFlag=filename, *including* the .pcx or .shp extension`
  The SHP or PCX file to use for the country's flag in observer mode, in the
  format "filename.shp" or "filename.pcx".
:tagdef:`[Country]File.ObserverFlagAltPalette=boolean`
  If :value:`yes`, draw SHP file :tag:`File.ObserverFlag=` using
  :file:`yrii.pal`. Otherwise the SHP file will be drawn using
  :file:`observer.pal`.
:tagdef:`[Country]File.LoadScreen=filename, *including* the .shp extension`
  The SHP file to use for the country's loading screen, in the format
  "filename.shp".
:tagdef:`[Country]File.LoadScreenPAL=filename, *including* the .pal extension`
  The palette file to use for the country's loading screen, in the format
  "filename.pal".
:tagdef:`[Country]File.Taunt=filename, *including* the Taunts\ directory and .wav extension`
  Path of the files to use for the country's taunts, in the format
  "Taunts\\filename%02i.wav". The filename specified *must* include "`%02i`",
  which will be substituted for the taunt ID (01 through 08). For example,
  :tag:`File.Taunt=Taunts\\tauam%02i.wav` will make the game load taunts
  :file:`tauam01.wav` through :file:`tauam08.wav`.

  .. note:: Taunts will only be registered for up to 16 countries.
:tagdef:`[Country]LoadScreenText.Name=CSF label`
  Name of the country, displayed on the loading screen (where a map of the
  country is usually shown). For example,
  :tag:`LoadScreenText.Name=Name:Americans`.
:tagdef:`[Country]LoadScreenText.SpecialName=CSF label`
  Name of the country's special weapon, displayed on the loading screen. For
  example, :tag:`LoadScreenText.SpecialName=Name:apara`.
:tagdef:`[Country]LoadScreenText.Brief=CSF label`
  Description of the country and its special weapon, displayed on the loading
  screen. For example, :tag:`LoadScreenText.Brief=loadbrief:usa`.
:tagdef:`[Country]LoadScreenText.Color=Color scheme`
  Text on the multiplayer loading screens for this country will be drawn using
  this color from the :tag:`[Colors]` enumeration. For example,
  :tag:`LoadScreenText.Color=AlliedLoad`.
:tagdef:`[Country]MenuText.Status=CSF label`
  Brief description of the country, displayed in the status bar of the country
  selection screen when the player mouse-overs that country in the country
  selection drop-down list.
:tagdef:`[Country]RandomSelectionWeight=integer`
  Specifies how likely it is that this country will be randomly selected when a
  player chooses 'Random'. The probability of this country being picked is
  calculated by dividing this country's :tag:`RandomSelectionWeight` value by
  the sum of all :tag:`Multiplay=yes` countries' :tag:`RandomSelectionWeight`
  values. Defaults to :value:`1`.
:tagdef:`[Country]ListIndex=integer`
  Specifies which position this country should appear in the country dropdown
  list. If two or more countries use the same :tag:`ListIndex`, the order is
  defined by their appearance in the :tag:`[Countries]` enumeration. Countries
  with negative values will not appear in the dropdown list; you can use this to
  effectively hide countries without having to change the :tag:`[Countries]`
  list and thus without risking game crashes. To also prevent such countries
  from being selected randomly, set :tag:`RandomSelectionWeight=0`. Defaults to
  :value:`100`.
:tagdef:`[Country]AI.PowerPlants=list of BuildingTypes`
  A list of buildings that the AI will treat as this country's power plants.
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
:tagdef:`[Country]VeteranBuildings=list of BuildingTypes`
  All buildings in this list start as veteran for this country and, if
  available, veteran cameos are displayed in the sidebar.

.. versionadded:: 0.1



Sides
`````

Sides are specified in the :tag:`[Sides]` list in :file:`rulesmd.ini`.

There is no limit to the number of sides that can be defined. However, only 16
fully-working countries can be implemented (see above).

Each side can (and should) define its own values for the following flags in the
side's INI section:

:tagdef:`[Side]DefaultDisguise=InfantryType`
  Default :type:`InfantryType` that disguisable infantry will be disguised as
  when first created.
:tagdef:`[Side]Crew=InfantryType`
  The :type:`InfantryType` that is spawned as a survivor when objects (with
  :tag:`Crewed=yes` set) owned by this side are destroyed (or, in the case of
  buildings, sold).
:tagdef:`[Side]Engineer=InfantryType`
  The :type:`InfantryType` that has a chance to be spawned when buildings with
  :tag:`Factory=BuildingType` owned by this side are destroyed or sold. Defaults
  to :tag:`[General]Engineer`.
:tagdef:`[Side]Technician=InfantryType`
  The :type:`InfantryType` that has a chance to be spawned when armed objects
  owned by this side are destroyed or sold. Defaults to
  :tag:`[General]Technician`.
:tagdef:`[Side]SurvivorDivisor=integer`
  An object's refund amount is divided by this number to determine how many
  survivors will be spawned when this object is destroyed (or, in the case of
  buildings, sold).
:tagdef:`[Side]AI.BaseDefenses=list of BuildingTypes`
  List of base defense buildings that the AI can build.
:tagdef:`[Side]AI.BaseDefenseCounts=list of integers`
  The maximum amount of base defense building that the AI can build.
  (listed as AI difficulties: hard, medium, easy)  Defaults to
  :tag:`[General]AlliedBaseDefenseCounts` for GDI (Allied),
  :tag:`[General]SovietBaseDefenseCounts` for Nod (Soviet), and
  :tag:`[General]ThirdBaseDefenseCounts` for ThirdSide (Yuri).
:tagdef:`[Side]ParaDrop.Types=list of InfantryTypes and/or VehicleTypes`
  The units that will be paradropped by :tag:`Type=ParaDrop` super weapons (such
  as the one normally provided by a Tech Airport) for this side. Defaults to
  :tag:`[General]AllyParaDropInf` for GDI (Allied),
  :tag:`[General]SovParaDropInf` for Nod (Soviet), and
  :tag:`[General]YuriParaDropInf` for ThirdSide (Yuri).
  
  .. note:: The original flags used to control the paradrop units only accept
    \ :type:`InfantryTypes`. To include :type:`VehicleTypes` in a paradrop you
    *have to* use the new :tag:`ParaDrop.Types` and :tag:`ParaDrop.Num` flags.
:tagdef:`[Side]ParaDrop.Num=list of integers`
  The quantity of each corresponding unit (listed against :tag:`ParaDrop.Types`)
  that will be paradropped. Defaults to :tag:`[General]AllyParaDropNum` for GDI
  (Allied), :tag:`[General]SovParaDropNum` for Nod (Soviet), and
  :tag:`[General]YuriParaDropNum` for ThirdSide (Yuri).
:tagdef:`[Side]ParaDrop.Aircraft=AircraftType`
  The aircraft type that will be used to deliver paradrops. Defaults to
  :value:`PDPLANE`.
:tagdef:`[Side]Parachute.Anim=Animation`
  This side's default parachute used if not overridden by the country or a
  :type:`TechnoType`. Defaults to :value:`PARACH`.
:tagdef:`[Side]Sidebar.MixFileIndex=integer`
  The MIX file number to use for the sidebar (e.g. :value:`1` for the Allied
  sidec01.mix, :value:`2` for the Soviet sidec02.mix).
:tagdef:`[Side]Sidebar.YuriFileNames=boolean`
  Whether or not to use the Yuri sidebar file names (sidec02md.mix and the
  Yuri-specific files within that MIX).
:tagdef:`[Side]ToolTipColor=R,G,B`
  Interface text and border color for tool tips, the credits counter, and other
  UI elements. Defaults to :value:`255,255,0` for sides :value:`Nod` and
  :value:`ThirdSide`, otherwise to :value:`164,210,255`.
:tagdef:`[Side]MessageTextColor=Color scheme`
  The color scheme used for printing ingame messages triggered by map action 11.
  Defaults to the 6th color scheme for side :value:`Nod`, the 13th color scheme
  for side :value:`ThirdSide`, to 11th color scheme otherwise. In the unmodified
  game, the colors are :value:`DarkRed`, :value:`DarkSky` and :value:`DarkBlue`
  respectively.

.. _sides-evatag:

:tagdef:`[Side]EVA.Tag=EVA Type`
  Name of the EVA Type tag to load from :file:`evamd.ini` for this side's EVA
  announcer. Use :value:`none` to disable EVA. Defaults to :value:`Russian` for
  side :value:`Nod`, to :value:`Yuri` for side :value:`ThirdSide`, to
  :value:`Allied` otherwise.

  See :doc:`EVA Types </new/evatypes>` on how to define values that can be used
  here.

.. index:: Sides; Sides can specify their own unique UI.

.. versionadded:: 0.1

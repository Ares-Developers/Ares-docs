Sides & Countries
~~~~~~~~~~~~~~~~~

In the original game the sides and countries were, for the most part,
hard-coded. You could not add to, remove or reorder the 10 countries
or 3 sides. Ares, however, makes these tasks possible you can now have
up to 16 ? countries and 16 sides, and you can customize these in
numerous ways... New sides & countries (including numerous
enhancements).



Countries
`````````

Countries are specified in the `[Countries]` list in rulesmd.ini. Any
country with `Multiplay=yes` set will appear in the country selection
drop-down list and be eligible for random selection if the player
chooses 'Random'. Countries can be excluded from the 'random country'
option, or given differing weights.

The `[Countries]` list can contain up to 32 countries, however taunts
will only work for 16 of these.

Each country can be customized using the following flags in the
country's INI section:
NB: The following filename specifications (where raw C-style format
specifiers like %s are required) are going to be changed into safer
versions in the future. The replacement style has not been decided
yet.

:[Country]File.Flag= (filename, *including* the .pcx extension): The
  PCX file to use for the country's flag, in the format "filename.pcx".
  File.Flag=
:[Country]File.LoadScreen= (filename, *including* the .shp extension):
  The SHP file to use for the country's loading screen, in the format
  "filename%s.shp". The filename specified *must* include " `%s`", which
  will be substituted for the current screen width (640 or 800 pixels).
  For example, `File.LoadScreen=ls%susstates.shp` will make the game
  load ls800usstates.shp. File.LoadScreen=
:[Country]File.LoadScreenPAL= (filename, *including* the .pal
  extension): The palette file to use for the country's loading screen,
  in the format "filename.pal". File.LoadScreenPAL=
:[Country]File.Taunt= (filename, *including* the Taunts\ directory and
  .wav extension): Path of the files to use for the country's taunts, in
  the format "Taunts\filename%02i.wav". The filename specified *must*
  include " `%02i`", which will be substituted for the taunt ID (01
  through 08). For example, `File.Taunt=Taunts\tauam%02i.wav` will make
  the game load taunts `tauam01.wav` through `tauam08.wav`. NB: Taunts
  will only be registered for up to 16 countries. File.Taunt=
:[Country]LoadScreenText.Name= (CSF label): Name of the country,
  displayed on the loading screen (where a map of the country is usually
  shown). For example, `LoadScreenText.Name=Name:Americans`.
  LoadScreenText.Name=
:[Country]LoadScreenText.SpecialName= (CSF label): Name of the
  country's special weapon, displayed on the loading screen. For
  example, `LoadScreenText.SpecialName=Name:apara`.
  LoadScreenText.SpecialName=
:[Country]LoadScreenText.Brief= (CSF label): Description of the
  country and its special weapon, displayed on the loading screen. For
  example, `LoadScreenText.Brief=loadbrief:usa`. LoadScreenText.Brief=
:[Country]LoadScreenText.Color= (Color scheme): Text on the
  multiplayer loading screens for this country will be drawn using this
  color from the `[Colors]` enumeration. For example,
  `LoadScreenText.Color=AlliedLoad`. LoadScreenText.Color=
:[Country]MenuText.Status= (CSF label): Brief description of the
  country, displayed in the status bar of the country selection screen
  when the player mouse-overs that country in the country selection
  drop-down list. MenuText.Status=
:[Country]RandomSelectionWeight= (integer): Specifies how likely it is
  that this country will be randomly selected when a player chooses
  'Random'. The probability of this country being picked is calculated
  by dividing this country's `RandomSelectionWeight` value by the sum of
  all `Multiplay=yes` countries' RandomSelectionWeight values. Defaults
  to 1. RandomSelectionWeight=
:[Country]ListIndex= (integer): Specifies which position this country
  should appear in the country dropdown list. If two or more countries
  use the same `ListIndex`, the order is defined by their appearance in
  the `[Countries]` enumeration. Countries with negative values will not
  appear in the dropdown list; you can use this to effectively hide
  countries without having to change the `[Countries]` list and thus
  without risking game crashes. To also prevent such countries from
  being selected randomly, set `RandomSelectionWeight=0`. Defaults to
  100. ListIndex=
:[Country]AI.PowerPlants= (list of BuildingTypes): A list of buildings
  that the AI will treat as this country's power plants. AI.PowerPlants=
:[Country]ParaDrop.Types= (list of InfantryTypes and/or VehicleTypes):
  The units that will be paradropped by `Type=ParaDrop` super weapons
  (such as the one normally provided by a Tech Airport) for this
  country. Defaults to the corresponding side's `ParaDrop.Types=`. NB:
  The original flags used to control the paradrop units only accept
  InfantryTypes. To include VehicleTypes in a paradrop you must use the
  new ParaDrop.Types and ParaDrop.Num flags. ParaDrop.Types=
:[Country]ParaDrop.Num= (list of integers): The quantity of each
  corresponding unit (listed against ParaDrop.Types) that will be
  paradropped. Defaults to the corresponding side's `ParaDrop.Num=`.
  ParaDrop.Num=
:[Country]ParaDrop.Aircraft= (AircraftType): The aircraft type that
  will be used to deliver paradrops. Defaults to the corresponding
  side's `ParaDrop.Aircraft=`. ParaDrop.Aircraft=
:[Country]Parachute.Anim= (Animation): This country's default
  parachute used if not overridden by a TechnoType. Defaults to the
  corresponding side's `Parachute.Anim=`. Parachute.Anim=


.. versionadded:: 0.1



Sides
`````

Sides are specified in the `[Sides]` list in rulesmd.ini.

There is no limit to the number of sides that can be defined. However,
only 16 fully-working countries can be implemented (see above).

Each side can (and should) define its own values for the following
flags in the side's INI section:

:[Side]DefaultDisguise= (InfantryType): Default InfantryType that
  disguisable infantry will be disguised as when first created.
  DefaultDisguise=
:[Side]Crew= (InfantryType): The InfantryType that is spawned as a
  survivor when objects (with `Crewed=yes` set) owned by this side are
  destroyed (or, in the case of buildings, sold) Crew=
:[Side]SurvivorDivisor= (integer): An object's refund amount is
  divided by this number to determine how many survivors will be spawned
  when this object is destroyed (or, in the case of buildings, sold).
  SurvivorDivisor=
:[Side]AI.BaseDefenses= (list of BuildingTypes): List of base defense
  buildings that the AI can build. AI.BaseDefenses=
:[Side]AI.BaseDefenseCounts= (list of integers): The maximum number of
  each corresponding base defense building (listed against
  `AI.BaseDefenses`) that the AI can build. AI.BaseDefenseCounts=
:[Side]ParaDrop.Types= (list of InfantryTypes and/or VehicleTypes):
  The units that will be paradropped by `Type=ParaDrop` super weapons
  (such as the one normally provided by a Tech Airport) for this side.
  Defaults to `[General]AllyParaDropInf` for GDI (Allied),
  `[General]SovParaDropInf` for Nod (Soviet), and
  `[General]YuriParaDropInf` for ThirdSide (Yuri). NB: The original
  flags used to control the paradrop units only accept InfantryTypes. To
  include VehicleTypes in a paradrop you must use the new ParaDrop.Types
  and ParaDrop.Num flags. ParaDrop.Types=
:[Side]ParaDrop.Num= (list of integers): The quantity of each
  corresponding unit (listed against ParaDrop.Types) that will be
  paradropped. Defaults to `[General]AllyParaDropNum` for GDI (Allied),
  `[General]SovParaDropNum` for Nod (Soviet), and
  `[General]YuriParaDropNum` for ThirdSide (Yuri). ParaDrop.Num=
:[Side]ParaDrop.Aircraft= (AircraftType): The aircraft type that will
  be used to deliver paradrops. Defaults to `PDPLANE`.
  ParaDrop.Aircraft=
:[Side]Parachute.Anim= (Animation): This side's default parachute used
  if not overridden by the country or a TechnoType. Defaults to
  `PARACH`. Parachute.Anim=
:[Side]Sidebar.MixFileIndex= (integer): The MIX file number to use for
  the sidebar (e.g. 1 for the Allied sidec01.mix, 2 for the Soviet
  sidec02.mix) Sides can specify their own unique UI.
  Sidebar.MixFileIndex=
:[Side]Sidebar.YuriFileNames= (boolean): Whether or not to use the
  Yuri sidebar file names (sidec02md.mix and the Yuri-specific files
  within that MIX). Sidebar.YuriFileNames=
:[Side]EVA.Tag= (EVA event): Name of the INI tag to load from
  evamd.ini for this side's EVA (vocal interface assistant e.g. Eva for
  Allied, Sofia for Soviet and Some Guy for Yuri). NB: EVA.Tag is not
  yet implemented. EVA.Tag=


.. versionadded:: 0.1

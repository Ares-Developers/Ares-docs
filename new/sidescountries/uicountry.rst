User Interface
~~~~~~~~~~~~~~

Display and Selection Chance
----------------------------

:tagdef:`[Country]MenuText.Status=CSF label`
  Brief description of the country, displayed in the status bar of the country
  selection screen when the player mouse-overs that country in the country
  selection drop-down list.
:tagdef:`[Country]ListIndex=integer`
  Specifies which position this country should appear in the country dropdown
  list. If two or more countries use the same :tag:`ListIndex`, the order is
  defined by their appearance in the :tag:`[Countries]` enumeration. Countries
  with negative values will not appear in the dropdown list; you can use this to
  effectively hide countries without having to change the :tag:`[Countries]`
  list and thus without risking game crashes. To also prevent such countries
  from being selected randomly, set :tag:`RandomSelectionWeight=0`. Defaults to
  :value:`100`.
:tagdef:`[Country]RandomSelectionWeight=integer`
  Specifies how likely it is that this country will be randomly selected when a
  player chooses 'Random'. The probability of this country being picked is
  calculated by dividing this country's :tag:`RandomSelectionWeight` value by
  the sum of all :tag:`Multiplay=yes` countries' :tag:`RandomSelectionWeight`
  values. Defaults to :value:`1`.
:tagdef:`[Country]AIRandomSelectionWeight=integer`
  The random selection weight used for AI players. This can be used to make it
  more or less likely for AI players to pick this country randomly. Defaults to
  :tag:`RandomSelectionWeight`.

.. versionadded:: 0.1
.. versionchanged:: 0.D


Flags and Observer Graphics
---------------------------

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

.. versionadded:: 0.1
.. versionchanged:: 0.3

Loading Screen
--------------

Loading screen background options:

:tagdef:`[Country]File.LoadScreen=filename, *including* the .shp extension`
  The SHP file to use for the country's loading screen, in the format
  "filename.shp".
:tagdef:`[Country]File.LoadScreenPAL=filename, *including* the .pal extension`
  The palette file to use for the country's loading screen, in the format
  "filename.pal".

Options regarding the text drawn on the background:

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

The music theme for multiplayer matches can be customized with the following
tag. For single player mission loading themes, please see :doc:`Campaign Load
Screen </ui-features/campaignloadscreen>`.

:tagdef:`[Country]LoadingTheme=theme id`
  The theme playing for a player of this country while the multiplayer match is
  loading. Defaults to :tag:`[Side]LoadingTheme`.

.. versionadded:: 0.1
.. versionchanged:: 0.7


Taunts
------

.. warning:: The following filename specifications (where raw C-style format
  specifiers like %s are required) are going to be changed into safer versions
  in the future. The replacement style has not been decided yet.

:tagdef:`[Country]File.Taunt=filename, *including* the Taunts\ directory and .wav extension`
  Path of the files to use for the country's taunts, in the format
  "Taunts\\filename%02i.wav". The filename specified *must* include "`%02i`",
  which will be substituted for the taunt ID (01 through 08). For example,
  :tag:`File.Taunt=Taunts\\tauam%02i.wav` will make the game load taunts
  :file:`tauam01.wav` through :file:`tauam08.wav`.

  .. note:: Taunts will only be registered for up to 16 countries.

.. versionadded:: 0.1

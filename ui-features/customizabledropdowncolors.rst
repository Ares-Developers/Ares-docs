Customizable Dropdown Colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The player colors shown in the dropdown list in the menu are hardcoded in
:game:`Yuri's Revenge` and they map to hardcoded color schemes in-game.
:game:`Ares` removes the hardcoding and lets you customize all existing colors
and even add more of them.

.. index:: Interface; Custom Dropdown Colors.

Using :file:`uimd.ini` you can define up to 16 colors to be shown in the
dropdown lists. Replace :tag:`X` by the numbers from :value:`1` to :tag:`Count`
(without leading zeros):

:tagdef:`[Colors]Count=integer`
  The number of colors to display. Values from 8 to 16 are valid and :tag:`Ares`
  enforces these limits. Defaults to :value:`8`.
:tagdef:`[Colors]SlotX.DisplayColor=R,G,B`
  The color displayed in the dropdown lists to preview the in-game color scheme
  in RGB format, that is three comma separated values from 0 to 255. Default
  depends on slot index.
:tagdef:`[Colors]SlotX.ColorScheme=Color scheme`
  The name of the color scheme defined in :file:`rulesmd.ini`'s :tag:`[Colors]`
  section this slot maps to in-game. Default depends on slot index.
:tagdef:`[Colors]SlotX.Tooltip=CSF label`
  The text shown as tool tip when the player hovers over the color in the
  dropdown list. Default depends on slot index.

You can use :tag:`Observer` instead of :tag:`SlotX` to define the colors used
for observers.

:game:`Ares` will display all color slots from :value:`1` to :tag:`Count`. You
may redefine any property without having to redefine the entire list.

It is your responsibility to select appropriate values. :game:`Ares` will not
check whether color values and color schemes are unique and distinguishable.

.. quickstart:: \ :game:`Ares` defaults to the original game's values and adds
  six more definitions not shown by default. To display those new items, set
  :tag:`Count=14`. Note that these additional color schemes have been added
  merely for demonstration purposes and they might collide with the original
  color schemes.


Default values
``````````````
Slot ID Menu Color Color Scheme Tool Tip Note `Slot1` 221,226,13 Gold
STT:PlayerColorGold `Slot2` 255,25,25 DarkRed STT:PlayerColorRed
`Slot3` 42,116,226 DarkBlue STT:PlayerColorBlue `Slot4` 62,209,46
DarkGreen STT:PlayerColorGreen `Slot5` 255,160,25 Orange
STT:PlayerColorOrange `Slot6` 50,215,230 DarkSky
STT:PlayerColorSkyBlue `Slot7` 149,40,189 Purple STT:PlayerColorPurple
`Slot8` 255,154,235 Magenta STT:PlayerColorPink `Slot9` 148,93,239
NeonBlue STT:PlayerColorLilac For demonstration purposes `Slot10`
115,255,231 LightBlue STT:PlayerColorLightBlue For demonstration
purposes `Slot11` 255,239,99 Yellow STT:PlayerColorLime For
demonstration purposes `Slot12` 8,195,90 Green STT:PlayerColorTeal For
demonstration purposes `Slot13` 189,85,0 Red STT:PlayerColorBrown For
demonstration purposes `Slot14` 128,128,128 Grey
STT:PlayerColorCharcoal For demonstration purposes ` *(others)*`
255,255,255 LightGrey NOSTR: `Observer` 96,96,96 LightGrey
STT:PlayerColorObserver

.. versionadded:: 0.2

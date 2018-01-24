.. index:: Interface; Dropdown colors

Customizable Dropdown Colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The player colors shown in the dropdown list in the menu are hardcoded in
:game:`Yuri's Revenge` and they map to hardcoded color schemes in-game.
:game:`Ares` removes the hardcoding and lets you customize all existing colors
and even add more of them.

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


Default dropdown color values
`````````````````````````````
  .. table::

    =================  ====================  ==================  =================================  ==========================
    Slot ID            Menu Color            Color Scheme        Tool Tip                           Note
    =================  ====================  ==================  =================================  ==========================
    :tag:`Slot1`       :value:`221,226,13`   :value:`Gold`       :value:`STT:PlayerColorGold`
    :tag:`Slot2`       :value:`255,25,25`    :value:`DarkRed`    :value:`STT:PlayerColorRed`
    :tag:`Slot3`       :value:`42,116,226`   :value:`DarkBlue`   :value:`STT:PlayerColorBlue`
    :tag:`Slot4`       :value:`62,209,46`    :value:`DarkGreen`  :value:`STT:PlayerColorGreen`
    :tag:`Slot5`       :value:`255,160,25`   :value:`Orange`     :value:`STT:PlayerColorOrange`
    :tag:`Slot6`       :value:`50,215,230`   :value:`DarkSky`    :value:`STT:PlayerColorSkyBlue`
    :tag:`Slot7`       :value:`149,40,189`   :value:`Purple`     :value:`STT:PlayerColorPurple`
    :tag:`Slot8`       :value:`255,154,235`  :value:`Magenta`    :value:`STT:PlayerColorPink`
    :tag:`Slot9`       :value:`148,93,239`   :value:`NeonBlue`   :value:`STT:PlayerColorLilac`      For demonstration purposes
    :tag:`Slot10`      :value:`115,255,231`  :value:`LightBlue`  :value:`STT:PlayerColorLightBlue`  For demonstration purposes
    :tag:`Slot11`      :value:`255,239,99`   :value:`Yellow`     :value:`STT:PlayerColorLime`       For demonstration purposes
    :tag:`Slot12`      :value:`8,195,90`     :value:`Green`      :value:`STT:PlayerColorTeal`       For demonstration purposes
    :tag:`Slot13`      :value:`189,85,0`     :value:`Red`        :value:`STT:PlayerColorBrown`      For demonstration purposes
    :tag:`Slot14`      :value:`128,128,128`  :value:`Grey`       :value:`STT:PlayerColorCharcoal`   For demonstration purposes
    :value:`(others)`  :value:`255,255,255`  :value:`LightGrey`  :value:`NOSTR:`
    :tag:`Observer`    :value:`96,96,96`     :value:`LightGrey`  :value:`STT:PlayerColorObserver`
    =================  ====================  ==================  =================================  ==========================

.. versionadded:: 0.2

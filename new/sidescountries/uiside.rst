User Interface
~~~~~~~~~~~~~~

Sidebar
-------

:tagdef:`[Side]Sidebar.MixFileIndex=integer`
  The MIX file number to use for the sidebar (e.g. :value:`1` for the Allied
  sidec01.mix, :value:`2` for the Soviet sidec02.mix).
:tagdef:`[Side]Sidebar.YuriFileNames=boolean`
  Whether or not to use the Yuri sidebar file names (sidec02md.mix and the
  Yuri-specific files within that MIX).

.. index:: Sides; Sides can specify their own unique UI.

.. versionadded:: 0.1


Text Colors
-----------

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

.. index:: Sides; Tooltip and message colors.

.. versionadded:: 0.4



Dialogs
-------

The side specific dialog background is used when a Reconnection error occurs or
while loading or saving a game.

:tagdef:`[Side]DialogBackground.Image=filename, *including* the .shp extension`
The shp file used as background for dialog boxes for this side. Should be
452x326. Defaults to :value:`PUDLGBGA.SHP`, :value:`PUDLGBGS.SHP`, and
:value:`PUDLGBGY.SHP` for sides 1, 2 and all others respectively. Requires
:tag:`DialogBackground.Palette` to be set.

:tagdef:`[Side]DialogBackground.Palette=filename, *including* the .pal extension`
The palette used to draw the background of dialog boxes for this side. Defaults
to :value:`DIALOG.PAL` for sides 1 and 2, to :value:`DIALOG.PAL` otherwise.
Requires :tag:`DialogBackground.Image` to be set.

.. versionadded:: 0.7


.. _sides-evatag:

EVA
---

:tagdef:`[Side]EVA.Tag=EVA Type`
  Name of the EVA Type tag to load from :file:`evamd.ini` for this side's EVA
  announcer. Use :value:`none` to disable EVA. Defaults to :value:`Russian` for
  side :value:`Nod`, to :value:`Yuri` for side :value:`ThirdSide`, to
  :value:`Allied` otherwise.

  See :doc:`EVA Types </new/evatypes>` on how to define values that can be used
  here.

.. index:: Sides; User-defined EVA voices.

.. versionadded:: 0.4

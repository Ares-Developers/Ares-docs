Custom Cameo Palettes
~~~~~~~~~~~~~~~~~~~~~

Rather than always using the cameo palette, individual cameos can now
use their own bespoke palette.
In artmd.ini:

:[UnitArt]CameoPalette= (filename, *including* the .pal extension):
  Specifies the palette to use for the unit's cameo (`Cameo` and
  `AltCameo` must use the same palette), in the format "filename.pal".
  Defaults to :file:`cameo.pal`.


In rulesmd.ini:

:[SuperWeapon]SidebarPalette= (filename, *including* the .pal extension):
  Specifies the palette to use for the super weapon's `SidebarImage`, in the
  format "filename.pal". Defaults to :file:`cameo.pal`.

.. note:: The cameo must not use the color at index 0 of the palette. It
  will be transparent in-game.

.. index:: Art; Custom palettes for cameos.

.. versionadded:: 0.1

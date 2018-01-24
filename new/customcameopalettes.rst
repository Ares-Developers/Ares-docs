.. index::
  Cameos; Palettes
  Art; Palettes for cameos

Custom Cameo Palettes
~~~~~~~~~~~~~~~~~~~~~

Rather than always using the cameo palette, individual cameos can now use their
own bespoke palette.

In :file:`artmd.ini`:

:tagdef:`[UnitArt]CameoPalette=filename, *including* the .pal extension)`
  Specifies the palette to use for the unit's cameo (:tag:`Cameo` and
  :tag:`AltCameo` must use the same palette), in the format "filename.pal".
  Defaults to :value:`cameo.pal`.


In :file:`rulesmd.ini`:

:tagdef:`[SuperWeapon]SidebarPalette=filename, *including* the .pal extension`
  Specifies the palette to use for the super weapon's :tag:`SidebarImage`, in
  the format "filename.pal". Defaults to :value:`cameo.pal`.

.. note:: The cameo must not use the color at index 0 of the palette. It
  will be transparent in-game.

.. versionadded:: 0.1

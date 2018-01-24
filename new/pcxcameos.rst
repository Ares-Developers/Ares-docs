.. index::
  Cameos; PCX cameos for TechnoTypes and super weapons
  TechnoTypes; PCX cameos
  Super Weapons; PCX cameos

PCX Cameos
~~~~~~~~~~

Additionally, cameos can be loaded from PCX files instead of SHP.

In :file:`artmd.ini`:

:tagdef:`[UnitArt]CameoPCX=filename, *including* the .pcx extension`
  Specifies the filename containing the unit's cameo, in the format
  "filename.pcx".
:tagdef:`[UnitArt]AltCameoPCX=filename, *including* the .pcx extension`
  Specifies the filename containing the unit's alternate (promoted) cameo, in
  the format "filename.pcx".


In :file:`rulesmd.ini`:

:tagdef:`[SuperWeapon]SidebarPCX=filename, *including* the .pcx extension`
  Specifies the filename containing the superweapon's cameo, in the format
  "filename.pcx".

.. note:: Like other PCX files used by the game, the PCX files used for this
  feature *must* have 256 colors and dimensions of 60x48 pixels.

.. versionadded:: 0.2

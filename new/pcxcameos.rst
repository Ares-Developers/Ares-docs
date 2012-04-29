PCX Cameos
~~~~~~~~~~

Additionally, cameos can be loaded from PCX files instead of SHP.

In :file:`artmd.ini`:

:[UnitArt]CameoPCX= (filename, *including* the .pcx extension): Specifies the
  filename containing the unit's cameo, in the format "filename.pcx".
:[UnitArt]AltCameoPCX= (filename, *including* the .pcx extension): Specifies the
  filename containing the unit's alternate (promoted) cameo, in the format
  "filename.pcx".

.. index:: Cameos; PCX cameos for TechnoTypes.


In :file:`rulesmd.ini`:

:[SuperWeapon]SidebarPCX= (filename, *including* the .pcx extension): Specifies
  the filename containing the superweapon's cameo, in the format "filename.pcx".

.. index:: Cameos; PCX cameos for Superweapons.

.. note:: Like other PCX files used by the game, the PCX files used for this
  feature *must* have 256 colors and dimensions of 60x48 pixels.

.. versionadded:: 0.2

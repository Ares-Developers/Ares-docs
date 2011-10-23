PCX Cameos
~~~~~~~~~~

Additionally, cameos can be loaded from PCX files instead of SHP.
In artmd.ini:

:[UnitArt]CameoPCX= (filename, *including* the .pcx extension):
  Specifies the filename containing the unit's cameo, in the format
  "filename.pcx".
:[UnitArt]AltCameoPCX= (filename, *including* the .pcx extension):
  Specifies the filename containing the unit's alternate (promoted)
  cameo, in the format "filename.pcx". PCX cameos for TechnoTypes.
  CameoPCX= AltCameoPCX=


In rulesmd.ini:

:[SuperWeapon]SidebarPCX= (filename, *including* the .pcx extension):
  Specifies the filename containing the superweapon's cameo, in the
  format "filename.pcx". PCX cameos for Superweapons. SidebarPCX=


NB: Like other PCX files used by the game, the PCX files used for this
feature *must* have 256 colors and dimensions of 60x48 pixels .

.. versionadded:: 0.2



<<<SEPARATOR>>>

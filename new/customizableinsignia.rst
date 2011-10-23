Customizable Insignia
~~~~~~~~~~~~~~~~~~~~~

Units can now have custom insignia (chevrons) to represent their
veterancy level.

:[TechnoType]Insignia.Rookie= (filename, excluding the .shp extension)
  [TechnoType]Insignia.Veteran= (filename, excluding the .shp extension)
  [TechnoType]Insignia.Elite= (filename, excluding the .shp extension):
  For example, `Insignia.Rookie=SAMPLE` would display sample.shp as the
  insignia while the object is rookie. Insignia.Rookie=
  Insignia.Veteran= Insignia.Elite=


These SHPs - like the original pips.shp - are expected to be in the
theater palette. If you specify an insignia, the first frame of its
SHP will be drawn. Veteran and Elite objects without the insignia
specified will still display the 15th/16th frames of pips.shp as
usual. Custom insignia for veteran/elite units.

.. versionadded:: 0.1



<<<SEPARATOR>>>

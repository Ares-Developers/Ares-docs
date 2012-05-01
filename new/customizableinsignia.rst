Customizable Insignia
~~~~~~~~~~~~~~~~~~~~~

Units can now have custom insignia (chevrons) to represent their veterancy
level.

:tagdef:`[TechnoType]Insignia.Rookie=filename, excluding the .shp extension`

:tagdef:`[TechnoType]Insignia.Veteran=filename, excluding the .shp extension`

:tagdef:`[TechnoType]Insignia.Elite=filename, excluding the .shp extension`
  For example, :tag:`Insignia.Rookie=SAMPLE` would display :file:`sample.shp` as
  the insignia while the object is rookie.


These SHPs - like the original :file:`pips.shp` - are expected to be in the
theater palette. If you specify an insignia, the first frame of its SHP will be
drawn. Veteran and Elite objects without the insignia specified will still
display the 15th/16th frames of :file:`pips.shp` as usual.

.. index:: Veterany; Custom insignia for veteran/elite units.

.. versionadded:: 0.1

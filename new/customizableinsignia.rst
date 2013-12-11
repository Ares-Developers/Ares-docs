Veterancy Insignia
~~~~~~~~~~~~~~~~~~

Chevrons
````````

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

.. index:: Veterancy; Custom insignia for veteran/elite units.

.. versionadded:: 0.1


Hiding Enemy Insignia
`````````````````````

Because you usually cannot ask enemy troops what their rank is, and from a
distance they look all the same anyhow, you can also disable displaying insignia
on enemy units by using the following tags.

:tagdef:`[General]EnemyInsignia=boolean`
  Whether insignia will be shown for enemy players by default. Each unit type
  can override this value. Defaults to :value:`yes`.

:tagdef:`[TechnoType]Insignia.ShowEnemy=boolean`
  Whether insignia for a unit of this type will be shown for enemy players.
  Defaults to :tag:`[General]EnemyInsignia`.

.. note:: Observers will always be able to see insignia of all players.

.. index:: Veterancy; Hide insignia of enemy units.

.. versionadded:: 0.5

Campaign Load Screen
~~~~~~~~~~~~~~~~~~~~

Text Color
----------

:game:`Yuri's Revenge` always draws single player campaign load screen texts in
red. :game:`Ares` uses the correct values, inferred by the mission name prefix.
You can override these defaults for each mission using this new
:file:`missionmd.ini` tag.

:tagdef:`[Mission]LoadScreenText.Color=Color scheme`
  Text on the campaign loading screens for this mission will be drawn using this
  color from the :tag:`[Colors]` list. For example,
  :tag:`LoadScreenText.Color=AlliedLoad`.

.. index:: Interface; Campaign load screen text color customizable per mission.

.. versionadded:: 0.2


Music Theme
-----------

The loading theme for a single player mission is read from the map file itself.

:tagdef:`[Basic]LoadingTheme=theme id`
  The theme playing when loading this mission. Use :value:`none` to disable the
  loading screen music. Defaults to :value:`LOADING`.

.. index:: Interface; Campaign load theme music customizable.

.. versionadded:: 0.7

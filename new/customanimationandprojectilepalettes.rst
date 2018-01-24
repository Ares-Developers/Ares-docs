.. index:: Art; Animation and projectile palettes

Custom Animation and Projectile Palettes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :game:`Yuri's Revenge`, you could use the animation or the unit palette to
display animations. :game:`Ares` lets you to specify custom palettes for
animations and projectiles.

:tagdef:`[Animation]CustomPalette=filename with .pal extension`
  Specifies the palette used to draw this animation/projectile.


You can specify theater-specific palettes by putting three `~` marks to the
theater specific part of the filename. `~~~` is replaced with the theater's
three-letter extension.

+ :tag:`CustomPalette=abcd.pal` always uses :file:`abcd.pal`.
+ :tag:`CustomPalette=lib~~~.pal` uses :file:`libtem.pal`, :file:`libsno.pal`,
  etc.

.. note:: Note that if you're using this on projectiles, you have to add the
  projectile to the :tag:`[Animations]` list.

.. versionadded:: 0.2

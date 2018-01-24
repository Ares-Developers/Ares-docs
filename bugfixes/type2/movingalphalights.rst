.. index:: Alpha Lights; Will now move with the object they are attached to
.. index:: Alpha Lights; Can now have multiple facings

===================
Moving Alpha Lights
===================

The original game includes a little-known flag that allows all
\ :type:`ObjectTypes` (anything placeable on the map - Projectiles, Trees,
Overlays, Smudges (not the :type:`IsometricTileTypes`), Aircraft, Infantry,
Vehicles and Buildings) to have a lighting effect displayed on them.
\ :tag:`[ObjectType]AlphaImage=ALPHATST` instructs the game to display
:file:`ALPHATST.shp` on the object as a lighting effect. The SHP must be saved
without any compression (just like :file:`mouse.sha`).

:game:`Ares` adds the following improvements to this feature:

+ The lighting effect will follow the object around as it moves, rather than
  staying where the object was created.
+ The effect will be inactive when a unit is cloaked, disguised as a terrain
  object or moving below the surface.
+ If the SHP has multiple frames then it is interpreted as a multi-facing image,
  and the largest N frames in the image are used as facing-specific versions (in
  this case, N is the largest power of 2 that is less than or equal to the
  number of frames in the SHP, e.g. 2/4/8/16/32/64...). This is supported only
  for :type:`TechnoTypes`.

.. note:: Alpha Lights on moving objects are a potential source of lag.

.. note:: Only :type:`TechnoTypes` are fully supported. :type:`Animations` are
  supported since :game:`Ares` 0.5.

.. versionadded:: 0.1

.. versionchanged:: 0.5

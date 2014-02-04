Solid Buildings
~~~~~~~~~~~~~~~

Buildings can now be made 'solid' to projectiles, meaning that projectiles will
detonate when hitting a building rather than passing through it.

In :file:`rulesmd.ini`:

:tagdef:`[Projectile]SubjectToBuildings=boolean`
  Whether or not this projectile can be blocked by solid buildings. Defaults to
  :value:`no`.


In :file:`artmd.ini`:

:tagdef:`[BuildingArt]SolidHeight=integer - cells`
  How tall the solid part of the building is considered to be, measured in cells
  (each cell has a height of 256 leptons), so buildings with a large amount of
  clear space near their top can allow projectiles to fly through that space.
  Negative values (e.g. :value:`-1`) tell the game to consider the building's
  full :tag:`Height` as solid. Default is :value:`0`, meaning the building is
  not at all solid (as per the normal game).
  
  .. note:: The solid building logic does not lend itself well to
    non-rectangular buildings, such as the Paris Tower or Space Needle.
  
.. index:: Buildings; Buildings can be made solid (like walls) to certain
  projectiles.

.. versionadded:: 0.1
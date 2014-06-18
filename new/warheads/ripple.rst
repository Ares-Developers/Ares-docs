Ion Cannon Ripple Effect
````````````````````````

:tagdef:`[Warhead]Ripple.Radius=integer, scale unknown`
  This generates a visual shockwave when the warhead detonates, identical to the
  one produced by :game:`Tiberian Sun`'s Ion Cannon. It is recommended that you
  don't set Radius above 79. Note that this is a visual effect only.

  Below are listed some results of modifying the tag values.

  + :tag:`Ripple.Radius=1` - Forget it, nothing.
  + :tag:`Ripple.Radius=5` - Target cell, only voxel rippling
  + :tag:`Ripple.Radius=8` - Target cell, both voxel and SHP rippling.
  + :tag:`Ripple.Radius=10` - 1 cell radius
  + :tag:`Ripple.Radius=15` - 2 cell radius
  + :tag:`Ripple.Radius=20` - 3 cell radius
  + :tag:`Ripple.Radius=25` - 3 cell radius
  + :tag:`Ripple.Radius=28` - 3 cell unit-rippling, 4 cell terrain rippling
    radius
  + :tag:`Ripple.Radius=30` and onwards - 3 cell unit-rippling, 5 cell
    terrain-rippling radius

.. index:: Warheads; Ion Cannon ripple effect for weapons.

.. versionadded:: 0.1

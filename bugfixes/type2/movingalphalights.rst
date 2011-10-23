Moving Alpha Lights
```````````````````

The original game includes a little-known flag that allows all
ObjectTypes (anything placeable on the map - Projectiles, Trees,
Overlays, Smudges (not the IsometricTileTypes), Aircraft, Infantry,
Vehicles and Buildings) to have a lighting effect displayed on them.
`[Object]AlphaImage=ALPHATST` instructs the game to display
ALPHATST.shp on the object as a lighting effect. The SHP must be saved
without any compression (just like mouse.sha).

Ares adds two improvements to this feature:


+ The lighting effect will follow the object around as it moves,
  rather than staying where the object was created. Alpha lights will
  now move with the object they are attached too. NB: Alpha Lights on
  moving objects are a potential source of lag.
+ If the SHP has multiple frames then it is interpreted as a multi-
  facing image, and the largest n frames in the image are used as
  facing-specific versions (in this case, n is the largest power of 2
  that is less than or equal to the number of frames in the SHP, e.g.
  2/4/8/16/32/64...) Alpha lights can now have multiple facings.


.. versionadded:: 0.1



<<<SEPARATOR>>>

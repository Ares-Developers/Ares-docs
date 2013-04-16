.. index:: Performance; Several performance enhancements.

==========================
Type 3 Fixes (Performance)
==========================
+ :file:`pips.shp` was getting reloaded from disk six times in a row.
+ A commonly used function, ``ObjectClass::GetCell``, performed the same tasks
  twice.
+ During startup, many superfluous calls were made to the debug log file writer.
+ Random Map Generator time has been greatly reduced (much time was wasted by
  redrawing the minimap multiple times during a map's generation).
+ Some particularly fast CPUs could cause the game to crash on startup.
+ There exists a version of :file:`ddraw.dll` that is often touted as improving
  the performance of :game:`Yuri's Revenge`. This "magic" DLL forces DirectDraw
  into software emulation mode, which doesn't use any hardware accelerated GPU
  functionality. This means special effects that are not emulated are simply
  omitted, potentially improving performance. :game:`Ares` uses software
  emulation mode by default, making this DLL unnecessary. However, Windows Vista
  and Windows 7 come with DirectX 10 - which does not support software emulation
  - so :game:`Ares` will not default to software emulation mode on those
  versions of Windows (otherwise users would just get a completely black
  screen).
+ Map actions `TechType exists` and `TechType does not exist` were implemented
  inefficiently. Both iterated all available types each frame to resolve an ID
  to a type and then iterated all technos to count the number of existing
  technos of this type. :game:`Ares` caches the type information. :game:`Ares`
  also optimizes summing up the techno count by using the house counters of
  each house, if the type is :tag:`Insignificant=no` and :tag:`DontScore=no`.

.. versionadded:: 0.1

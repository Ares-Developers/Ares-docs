.. index::
  Savegames; Crates will no longer disappear after loading
  Crates; Disappearing after loading a savegame

====================================
Crates Disappear When Loading A Game
====================================

:game:`Yuri's Revenge` contained special code to remove all crates from the map
after loading. When removed, crates existing before the game was saved would not
disappear after being collected any more. Whether the special code was added to
disguise this bug remains unknown, but it could break campaign missions relying
on mission critical crates.

:game:`Ares` fixed the underlying issue preventing the crates to disappear when
collected and removes the special code in the game that removed all crates after
loading. Mission critical crates are now working reliably.

.. versionadded:: 1.0

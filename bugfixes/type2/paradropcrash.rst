.. index:: Crashes; Paradropping from player-loaded aircraft

========================================
Paradropping from Player-Loaded Aircraft
========================================

When player-loaded units were paradropped from aircraft, the game failed to
update their state correctly. This caused issues because the paradropped units
were still linked to the aircraft, and it could cause desyncs and crashes once
the aircraft was destroyed. :game:`Ares` fixes this.

.. versionadded:: 3.0

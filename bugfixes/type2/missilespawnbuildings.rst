=======================================
:captiontag:`MissileSpawn` on Buildings
=======================================

Buildings were able to use :tag:`Spawns` logic only as long as the spawned
:type:`AircraftType` had :tag:`MissileSpawn=no` set, thus could only spawn
aircraft like the Destroyer and the Airgraft Carrier. If a building were to
spawn a missile, the game would crash. :game:`Ares` fixed the missile handling
and thus :tag:`MissileSpawn=yes` no longer crashes the game.

.. versionadded:: 1.0

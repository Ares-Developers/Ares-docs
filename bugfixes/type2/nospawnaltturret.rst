.. index:: Spawners; NoSpawnAlt and Turret

=================================================
:captiontag:`NoSpawnAlt` and :captiontag:`Turret`
=================================================

To store the spawn-less voxel, spawner units with :tag:`NoSpawnAlt=yes` used the
same storage space normally used for turrets. Thus, spawner units which should
have a spawn-less voxel cannot also have a turret at the same time.

:game:`Ares` reworked this feature and makes it possible to combine turrets and
spawn-less voxels.

.. versionadded:: 3.0

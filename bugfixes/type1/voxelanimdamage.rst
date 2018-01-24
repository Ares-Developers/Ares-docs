.. index:: Bugs; Voxel Animations dealt less and less damage over time

=============================
Voxel Animation Damage Issues
=============================

Voxel Animation damage delivery had two bugs. Firstly, it passed its
:tag:`Damage` data on the type directly, without making a copy first. The type
data thus could change during the course of the game, and the type of Voxel Anim
would do less and less damage over time. Secondly, the game could crash if the
Voxel Animation had no :tag:`Warhead` defined.

Both issues have been fixed in :game:`Ares`.

.. versionadded:: 0.E

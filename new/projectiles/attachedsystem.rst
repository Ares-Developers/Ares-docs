.. index:: Projectiles; ParticleSystems as trailers

:captiontag:`AttachedSystem` Trailers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to using animation trailers, :game:`Ares` allows to attach particle
systems to projectiles to emit smoke particles on their way to the target. This
works like the same tag on :type:`VoxelAnimTypes`.

:tagdef:`[Projectile]AttachedSystem=ParticleSystemType`
  The type of the particle system to attach to this projectile. Only particle
  systems  with :tag:`BehavesLike=smoke` are supported.

.. versionadded:: 0.C

Particles
~~~~~~~~~

Optimizations
-------------

Particle handling has been greatly optimized in :game:`Ares`. Pixel particles --
that is types having :tag:`BehavesLike=` set to either :value:`Spark` or
:value:`Railgun` -- were known to cause lag even with relatively few particles
involved. That is, even sparse railgun beams created a noticable slowdown. Also,
:value:`Smoke` particles are created frequently throughout a game.

In :game:`Ares` the optimization is activated automatically if all of the
following are true. If any one is false, the optimization will not be applied
and the particles will be handled like in earlier versions. That is, mixing and
matching is still possible.

1. :tag:`[ParticleSystem]BehavesLike=` is either :value:`Spark`,
   :value:`Railgun`, or :value:`Smoke`
2. The :type:`ParticleType` set as :tag:`[ParticleSystemType]HoldsWhat=` has the
   exact same setting
3. The :type:`ParticleType` does not use alpha images or line trailers

.. note:: Note that mixing :value:`Spark` and :value:`Railgun` will prevent the
  optimization from being applied.

The game's existing particles have been optimized also, and even if the
optimization is not applied, particles will be handled more efficiently.

.. index:: Particles; Optimizations for Pixel Particles

.. versionadded:: 0.C
.. versionchanged:: 0.D


Damage Range for Gas Particles
------------------------------

Gas particles could only damage objects residing on the same cell as itself, no
matter how big the particle's image was. :game:`Ares` allows to customize this.

:tagdef:`[ParticleType]DamageRange=double - cells`
  The particle damage is applied to all objects in this range around the gas
  particle. If less or equal to :value:`0.0`, all objects in the cell the gas
  particle is on are affected. Each object is affected at most once. Defaults to
  :value:`0.0`.

.. index:: Particles; Customize Damage Range for Gas Particles

.. versionadded:: 0.C


Custom Palettes for Shape Particles
-----------------------------------

Particles drawing shape images -- that is types having :tag:`BehavesLike=` set
to :value:`Gas`, :value:`Smoke`, or :value:`Fire` -- now support to be drawn
using a custom palette.

:tagdef:`[ParticleType]Palette=filename with .pal extension`
  The palette used to draw an image particle of this type. Defaults to
  :value:`ANIM.PAL`.

.. index:: Particles; Custom Palette for Shape Particles

.. versionadded:: 0.C

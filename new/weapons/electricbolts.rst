.. index:: Weapons; Electric bolts can have custom colors

Electric Bolts
~~~~~~~~~~~~~~

Bolt Coloring
-------------

The default colors for electric bolts are taken from the theater palette. The
third is always the color at index 15, while both others use the color at index
10 (or 5, if :tagdef:`IsAlternateColor=yes`).

:tagdef:`[Weapon]Bolt.Color1=R,G,B`

:tagdef:`[Weapon]Bolt.Color2=R,G,B`

:tagdef:`[Weapon]Bolt.Color3=R,G,B`
  The three colors used to draw this Electric Bolt. Can be omitted to use the
  palette-dependent default values.

.. versionadded:: 0.1


.. index:: Weapons; Electric bolt spark particle systems

Spark Particle System
---------------------

:tagdef:`[Weapon]Bolt.ParticleSystem=ParticleSystem`
  Defines the spark particle system to spawn at the target location. Use
  :value:`none` to disable the particle system. Defaults to
  :tag:`[CombatDamage]DefaultSparkSystem`.

.. versionadded:: 2.0

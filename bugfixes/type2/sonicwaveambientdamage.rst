.. index:: Weapons; Sonic wave ambient damage comes from the correct weapon (instead of always Primary).

=========================
Sonic Wave Ambient Damage
=========================

The ``Warhead`` and ``AmbientDamage`` settings used when applying ambient
damage from a sonic weapon were always taken from the unit's current
primary weapon rather than the weapon that actually fired the wave.
Now these settings are taken from the weapon that fired the wave.

.. versionadded:: 0.1

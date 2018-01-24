.. index:: Animations; Animations' Warhead= flag now works

=========================
Animation Damage Warheads
=========================

Animations may have appeared to deal damage randomly rather than based on the
warhead specified. In fact, animations were hard-coded to deal damage using the
warhead specified by :tag:`[CombatDamage]FlameDamage2`, unless the animation ID
was :tag:`[INVISO]`, in which case the warhead used
:tag:`[CombatDamage]C4Warhead`. With  :game:`Ares`, the
:tag:`[Animation]Warhead` flag will be adhered to, with the aforementioned
warheads used as the default if :tag:`[Animation]Warhead` is not specified.

.. versionadded:: 0.1

Ion Cannon
``````````

Any warhead can launch an Ion Cannon effect in :game:`Ares`. The Ion Cannon
consists of a beam and an impact animation on the ground as well as damage
delivery using a custom warhead.


.. index::
  Warheads; Fire an Ion Cannon where the warhead impacts
  Ion Cannon; Fire from any warhead

Ion Cannon Blast
----------------

:tagdef:`[Warhead]IonCannon=boolean`
  Whether Ion Cannon logic will be activated when this warhead impacts. Defaults
  to :value:`no`.

The following settings are available for Ion Cannon warheads.

:tagdef:`[Warhead]IonCannon.Blast=Animation`
  The optional first animation on the impact site. This is only used if the
  warhead impacts on land. If the impact site is on water, the last animation
  from the :tag:`[CombatDamage]SplashList` is used. Set to :value:`none` to
  deactivate. Defaults to :tag:`[General]IonBlast`.

:tagdef:`[Warhead]IonCannon.Beam=Animation`
  The optional second animation on the impact site. Set to :value:`none` to
  deactivate. Defaults to :tag:`[General]IonBeam`.

:tagdef:`[Warhead]IonCannon.Warhead=Warhead`
  The optional warhead to deliver the damage. Set to :value:`none` to deal no
  Ion Cannon damage. Defaults to :tag:`[CombatDamage]IonCannonWarhead`.

:tagdef:`[Warhead]IonCannon.Damage=integer - hitpoints`
  The damage dealt by the Ion Cannon warhead. Defaults to
  :tag:`[CombatDamage]IonCannonDamage`.

:tagdef:`[Warhead]IonCannon.Rock=boolean`
  Whether voxel units are rocked by the impact. Defaults to :value:`yes`.

.. versionadded:: 2.0



.. index:: Warheads; Ion Cannon ripple effect

Ripple Effect
-------------

The shockwave visual effect can be activated independently of a warhead being
an Ion Cannon.

:tagdef:`[Warhead]IonCannon.Ripple=integer - frames`
  This generates a visual shockwave when the warhead detonates, identical to the
  one produced by :game:`Tiberian Sun`'s Ion Cannon. Note that this is a visual
  effect only. Valid values range from :value:`0` (off) to :value:`79` (max
  effect). Defaults to :value:`79` for :tag:`IonCannon=yes`, to :value:`0`
  otherwise.

  Below are listed some results of modifying the tag values.

  + :tag:`Ripple.Radius=1` - Forget it, nothing.
  + :tag:`Ripple.Radius=5` - Target cell, only voxel rippling
  + :tag:`Ripple.Radius=8` - Target cell, both voxel and SHP rippling.
  + :tag:`Ripple.Radius=10` - 1 cell radius
  + :tag:`Ripple.Radius=15` - 2 cell radius
  + :tag:`Ripple.Radius=20` - 3 cell radius
  + :tag:`Ripple.Radius=25` - 3 cell radius
  + :tag:`Ripple.Radius=28` - 3 cell unit-rippling, 4 cell terrain rippling
    radius
  + :tag:`Ripple.Radius=30` and onwards - 3 cell unit-rippling, 5 cell
    terrain-rippling radius

.. versionadded:: 0.1



.. index:: Warheads; Destroy bridges instantly

Bridge Destroyer
----------------

A hardcoded property of the original Ion Cannon from :game:`Tiberian Sun` was
that it instantly destroyed bridges it hit. This special logic was only applied
for the warhead defined as :tag:`IonCannonWarhead`. With :game:`Ares`, this
feature can be used on any warhead, and turned off for the original warhead.

:tagdef:`[Warhead]BridgeAbsoluteDestroyer=boolean`
  Whether this warhead immediately destroys a bridge it hits. Requires
  :tag:`Wall=yes`. Defaults to :value:`yes` for
  :tag:`[CombatDamage]IonCannonWarhead`, to :value:`no` otherwise.

.. versionadded:: 2.0

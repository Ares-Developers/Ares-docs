.. _preimpactanim:

.. index:: Warheads; Pre-impact anim not just for nukes

:captiontag:`PreImpactAnim`
```````````````````````````

In :game:`Yuri's Revenge` the nuke uses a special animation called
:tag:`NUKEBALL` which was shown prior to displaying the actual mushroom
explosion and dealing damage. The game was hard-coded to use this only for
warheads with the ID :tag:`NUKE`. :game:`Ares` enables this for arbitrary
warheads.

:tagdef:`[Warhead]PreImpactAnim=animation`
  Specifies the animation to display when a projectile which uses this warhead
  impacts. After the animation is over, the actual explosion is created and
  damage is dealt. The animation may not be looping. Defaults to
  :value:`NUKEBALL` for :tag:`NUKE`, otherwise to :value:`none`.

:tagdef:`[Warhead]PreImpactAnim.Moves=boolean`
  Can be used to optionally move the bullet when the animation used as
  :tag:`PreImpactAnim` moves while playing. If :value:`yes`, moves the bullet to
  the last location of the animation and sets the target to the cell containing
  the animation. Defaults to :value:`no`.

.. versionadded:: 0.2
.. versionchanged:: 2.0

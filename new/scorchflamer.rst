.. index:: Animations; Napalm tags Scorch= and Flamer= restored

:captiontag:`Scorch` and :captiontag:`Flamer`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:game:`Tiberian Sun` had special support for napalm animations: two tags that
spawned new fire animations defined by :tag:`SmallFire` and :tag:`LargeFire`.
This has been reimplemented as it worked previously.

There is one notable change in behavior compared to :game:`Tiberian Sun`: If
:tag:`LargeFire` or :tag:`SmallFire` are not set correctly, the game will not
crash when a new animation of these types is about to be created.

:tagdef:`[Animation]Scorch=boolean`
  Whether a new :tag:`[AudioVisual]SmallFire` animation should be attached to
  the same object this animation is attached to when expiring. Does not spawn on
  water, beach, ice, or rock terrain. For a complete description of behavior and
  requirements, refer to `Scorch on ModEnc
  <https://www.modenc.renegadeprojects.com/Scorch>`_ Defaults to :value:`no`.

  .. note:: Do not set :tag:`Scorch=yes` on :tag:`[AudioVisual]SmallFire`,
    because this would create a loop: if the animation expires, a new animation
    of the same type is created and attached to the same object. It also causes
    trees on fire to never burn down.

:tagdef:`[Animation]Flamer=boolean`
  Whether new :tag:`[AudioVisual]SmallFire` and :tag:`[AudioVisual]LargeFire`
  animations should be randomly created close to the location of this animation
  when expiring. For a complete description of behavior and requirements, refer
  to `Flamer on ModEnc <https://www.modenc.renegadeprojects.com/Flamer>`_.
  Defaults to :value:`no`.

.. versionadded:: 0.8

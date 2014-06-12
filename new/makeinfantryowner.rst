:captiontag:`MakeInfantryOwner`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The original :tag:`MakeInfantry` logic would always grant ownership of
newly-created infantry to the neutral side, unless the animation was caused by
an :type:`InfantryType` being killed by an :tag:`InfDeath=9` warhead (in which
case the killing player would get ownership of the new :type:`InfantryType`).
:game:`Ares` lets you choose which player will gain ownership, from one of
several options.

:tagdef:`[Animation]MakeInfantryOwner=enumeration invoker|killer|victim|neutral|random`
  Specifies which house will own the resulting :type:`InfantryType` that gets
  created after this animation has played. The animation's re-mappable colors
  will be shown in that house's color, if not noted otherwise. Defaults to
  :value:`invoker`.

  .. note:: If you are creating a chain of animations using the :tag:`Next=` tag
    then :tag:`MakeInfantry=` goes on the last animation whereas
    \ :tag:`MakeInfantryOwner=` goes on the first animation - that is, the
    animation that was initially invoked.

Note that this is not a warhead property; it goes on the corresponding animation
entry in :file:`artmd.ini`. However, :tag:`MakeInfantryOwner` only works for
specific animations; namely those invoked by :tag:`InfDeathAnim`,
:tag:`DeathAnims`, :tag:`InfantryExplode`, :tag:`FlamingInfantry`,
:tag:`InfantryElectrocuted`, :tag:`InfantryHeadPop`, :tag:`InfantryNuked`,
:tag:`InfantryVirus`, :tag:`InfantryMutate`, :tag:`InfantryBrute`, and map
triggers. The default :tag:`MakeInfantryOwner` is :value:`invoker`, which
corresponds to a different player depending on the animation.


+ For :tag:`InfDeathAnim`, :tag:`InfantryVirus` and :tag:`InfantryMutate`,
  :value:`invoker` represents :value:`killer` (the owner of the killing unit).
  For :tag:`InfantryVirus` on a :tag:`NotHuman=no` victim, the remappable colors
  are **not** used. If you want them, use :value:`killer` explicitly.
+ For :tag:`InfantryExplode`, :tag:`FlamingInfantry`,
  :tag:`InfantryElectrocuted`, :tag:`InfantryHeadPop`, :tag:`InfantryNuked`, and
  :tag:`InfantryBrute`, :value:`invoker` represents the neutral house with the
  remappable colors **not** being used. If you want the remapped colors, you
  have to use :value:`neutral` explicitly.
+ For :tag:`DeathAnims`, :value:`invoker` represents :value:`victim` (the owner
  of the dying unit).
+ For map triggers, :value:`invoker`, :value:`killer` and :value:`victim` all
  represent the house that is considered to be the owner of the trigger.


:value:`random` will pick a random player from all players in the game,
including neutral.

.. note:: Like :tag:`InfDeath=9`, mutation animations will be rendered in the
  unit palette with remap colors instead of :file:`anim.pal`, if not noted
  otherwise.

.. index:: Animations; MakeInfantry animations (InfDeathAnim, DeathAnims, ..., and map triggers) can choose who the owner will be.

.. versionadded:: 0.1

.. versionchanged:: 0.7

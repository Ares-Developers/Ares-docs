Chain Reactions
```````````````

There are two distinct logics that have their part in the tiberium chain
reactions as seen in :game:`Tiberian Sun`. Chain Reactions were not supported
in :game:`Yuri's Revenge` and has now been restored, and both have been made
more customizable.

.. index: Tiberium; Chain Reactions.

.. versionadded:: 0.5


Tiberium Explosion
------------------

Tiberium Explosion occurs if an animation with :tag:`TiberiumChainReaction=yes`
hits a cell containing tiberium. There is a chance that debris is spawned. For a
more detailled description, refer to `TiberiumChainReaction on ModEnc
<http://modenc.renegadeprojects.com/TiberiumChainReaction>`_.

The warhead, the damage delivered and the chance to spawn debris can be
customized for each of the :type:`Tiberiums`.


Chain Reaction
--------------

Overlay can be made to trigger a chain reaction when damaged. An animation is
spawned on the neighbour cells that can propagate the effect. For a more
detailled description, refer to `ChainReaction on ModEnc
<http://modenc.renegadeprojects.com/ChainReaction>`_.

The logic has been restored and new works as in :game:`Tiberian Sun`. The
warhead can be customized for each of the :type:`Tiberiums`.


Customizable Settings
---------------------

:tagdef:`[Tiberium]ExplosionWarhead=warhead`
  The warhead used to deliver the damage of the chain reaction effect, as well
  as the damage of the Tiberium Explosion effect. Defaults to
  :tag:`[General]C4Warhead`.
  
  .. note:: \ :game:`Tiberian Sun`'s :tag:`C4Warhead` was :value:`HE`, which had
    \ :tag:`Spread` set. :game:`Red Alert 2` uses :value:`Super`, which does
    not.

:tagdef:`[Tiberium]ExplosionDamage=integer`
  The damage an animation with :tag:`TiberiumChainReaction=yes` deals to the
  cell it impacts at. Defaults to :tag:`[CombatDamage]TiberiumExplosionDamage`.

:tagdef:`[Tiberium]Debris.Chance=integer - percent`
  The chance a cell containing this tiberium type hit by an animation with
  :tag:`TiberiumChainReaction=yes` will spawn one of its :tag:`Debris`. Defaults
  to :value:`33`.


Minimum Damage to Trigger :captiontag:`Explodes=yes`
````````````````````````````````````````````````````

Overlay with :tag:`Explodes=yes` detonates when taking even the slightest amount
of damage. With :game:`Ares` you can raise this limit so overlay only explodes
if the damage is higher than a certain value.

:tagdef:`[General]OverlayExplodeThreshold=integer`
  Only if the damage to a cell is higher than this does an overlay with
  :tag:`Explodes=yes` explode. Below this value, the overlay stays intact.
  Defaults to :value:`0`.

.. index: Overlay; Explodes=yes and a minimm damage.

.. versionadded:: 0.5

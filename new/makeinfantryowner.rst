MakeInfantryOwner
~~~~~~~~~~~~~~~~~

The original `MakeInfantry` logic would always grant ownership of
newly-created infantry to the neutral side, unless the animation was
caused by an InfantryType being killed by an `InfDeath=9` warhead (in
which case the killing player would get ownership of the new
InfantryType). Ares lets you choose which player will gain ownership,
from one of several options.

:[Animation]MakeInfantryOwner= (enumeration
  invoker|killer|victim|neutral|random): Specifies which house will own
  the resulting InfantryType that gets created after this animation has
  played. The animation's re-mappable colors will be shown in that
  house's color. NB: If you are creating a chain of animations using the
  `Next=` tag then `MakeInfantry=` goes on the last animation whereas
  `MakeInfantryOwner=` goes on the first animation - that is, the
  animation that was initially invoked.


Note that this is not a warhead property it goes on the corresponding
animation entry in artmd.ini. However, `MakeInfantryOwner` only works
for specific animations; namely those invoked by `InfDeathAnim`,
`DeathAnims` and map triggers. The deafult `MakeInfantryOwner` is
'invoker', which corresponds to a different player depending on the
animation.


+ For `InfDeathAnim`, 'invoker' represents 'killer' (the owner of the
  killing unit).
+ For `DeathAnims`, 'invoker' represents 'victim' (the owner of the
  dying unit).
+ For map triggers, 'invoker', 'killer' and 'victim' all represent the
  house that is considered to be the owner of the trigger.


'random' will pick a random player from all players in the game,
including neutral.
NB: Like `InfDeath=9`, all mutation animations will be rendered in the
unit palette instead of anim.pal. MakeInfantry animations
(InfDeathAnim, DeathAnims, map triggers) can choose who the owner will
be as killer|victim|neutral|random. MakeInfantryOwner=

.. versionadded:: 0.1

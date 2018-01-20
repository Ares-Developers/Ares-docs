Infantry-related Settings
~~~~~~~~~~~~~~~~~~~~~~~~~

Deployed Infantry Damage multiplier
```````````````````````````````````

:tagdef:`[Warhead]Damage.Deployed=float - multiplier`
  A multiplier applied to :tag:`Damage` if the :type:`InfantryType` receiving it
  is currently deployed.


Note that this is not the same as the existing :tag:`ProneDamage=` flag;
deployed units are not considered to be prone. Defaults to :value:`100%`.

.. index:: Warheads; Per-warhead damage multiplier against deployed infantry.

.. versionadded:: 0.1

:captiontag:`InfDeathAnim`
``````````````````````````

:tagdef:`[Warhead]InfDeathAnim=string, animation ID`
  Specifies the animation to display when an :type:`InfantryType` (with
  :tag:`NotHuman=no`) is killed by this warhead. Works in the same way as
  existing :tag:`InfDeath` animations except this flag allows you to specify an
  animation ID rather than an integer. Furthermore, the animation will be
  treated as the correct type (e.g. mutation or non-mutation) automatically,
  which means that you can now have any number of mutations that produce
  player-owned :tag:`InfantryTypes`. See :doc:`MakeInfantryOwner
  </new/makeinfantryowner>` for how to control which player will gain control of
  'mutated' infantry.

.. index:: Warheads; New InfDeaths (InfDeathAnim= any animation, auto-detect mutation).

.. versionadded:: 0.1

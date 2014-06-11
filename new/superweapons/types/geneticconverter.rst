:captiontag:`Type=GeneticConverter`
```````````````````````````````````

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  The area the Genetic Mutator affects. Ignored if :tag:`Mutate.Explosion=yes`.
  Defaults to :value:`3,3`.
:tagdef:`[SuperWeapon]SW.Damage=integer`
  The damage the Genetic Mutator delivers if :tag:`Mutate.Explosion=yes`.
  Defaults to :value:`10000`.
:tagdef:`[SuperWeapon]SW.Warhead=Warhead`
  The warhead used to deal the damage. Defaults to
  :tag:`[SpecialWeapons]MutateExplosionWarhead` if :tag:`Mutate.Explosion=yes`,
  to :tag:`[SpecialWeapons]MutateWarhead` otherwise.
:tagdef:`[SuperWeapon]SW.Animation=Animation`
  Defaults to :tag:`[General]IonBlast`.
:tagdef:`[SuperWeapon]SW.AnimationHeight=integer`
  Defaults to :value:`5`.
:tagdef:`[SuperWeapon]SW.Sound=Sound`
  Defaults to :tag:`[AudioVisual]GeneticMutatorActivateSound`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`GeneticMutator`.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum`
  Specifies the houses affected by the mutation, if :tag:`Mutate.Explosion=no`.
  Defaults to :value:`all`.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum`
  Specifies whether the mutation effect should be limited to :value:`land` or
  :value:`water` targets. You cannot define any unit type here and they will be
  ignored. Ignored if :tag:`Mutate.Explosion=yes`. Defaults to :value:`all`.


Genetic Mutator specific tags:

:tagdef:`[SuperWeapon]Mutate.Explosion=boolean`
  Switches between two modes. If :value:`yes`, the Genetic Mutator will cause an
  explosion using :tag:`SW.Warhad` and :tag:`SW.Damage` without respecting any
  other Genetic Mutator specific tags. Otherwise all infantry units in range are
  damaged using :tag:`SW.Warhead` and :tag:`SW.Damage`, verses and immunities
  are respected. Defaults to :tag:`[General]MutateExplosion`.
:tagdef:`[SuperWeapon]Mutate.IgnoreCyborg=boolean`
  Whether the Genetic Mutator will not affect infantry with :tag:`Cyborg=yes`
  set. Ignored if :tag:`Mutate.Explosion=yes`. Defaults to :value:`no`.
:tagdef:`[SuperWeapon]Mutate.IgnoreNotHuman=boolean`
  Whether the Genetic Mutator will not affect infantry with :tag:`NotHuman=yes`
  set. Ignored if :tag:`Mutate.Explosion=yes`. Defaults to :value:`no`.
:tagdef:`[SuperWeapon]Mutate.KillNatural=boolean`
  Whether the Genetic Mutator will just kill infantry with :tag:`Natural=yes`
  set opposed to affecting it using :tag:`SW.Warhead`. Ignored if
  :tag:`Mutate.Explosion=yes`. Defaults to :value:`yes`.


.. versionadded:: 0.2

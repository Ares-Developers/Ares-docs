:captiontag:`Type=PsychicReveal`
````````````````````````````````

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Range revealed by this super weapon. Defaults to
  :tag:`[CombatDamage]PsychicRevealRadius`. The default value is capped at 10,
  mimicking the original implementation using Cell Spread. To disable this
  limitation, set :tag:`SW.Range` explicitly.
:tagdef:`[SuperWeapon]SW.Sound=Sound`
  Defaults to :tag:`[AudioVisual]PsychicRevealActivateSound`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`ParaDrop`.


.. versionadded:: 0.2

:captiontag:`Type=PsychicReveal`
````````````````````````````````

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Range revealed by this super weapon. Defaults to
  :tag:`[CombatDamage]PsychicRevealRadius`. The default value is capped at
  :value:`10`, mimicking the original implementation using Cell Spread. To
  disable this limitation, set :tag:`SW.Range` explicitly. Use :value:`-1` to
  reveal the whole map. When using full-map reveal you do not have to select a
  target location; instead the super weapon will be fired automatically when you
  click its cameo icon.
:tagdef:`[SuperWeapon]SW.Sound=Sound`
  Defaults to :tag:`[AudioVisual]PsychicRevealActivateSound`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`ParaDrop`.
:tagdef:`[SuperWeapon]Cursor=mouse cursor`
  Defaults to :value:`PsychicReveal`.

.. versionadded:: 0.2
.. versionchanged:: 0.9

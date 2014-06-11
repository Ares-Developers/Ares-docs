:captiontag:`Type=SonarPulse`
`````````````````````````````

The Sonar Pulse is a variation of the original Sonar Pulse known from
Red Alert it will cause any cloaked units in range or on the entire
map to temporarily decloak, even if it is under a Cloak Generator or not.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  The radius, in cells, that the decloak effect will be applied. Use negative
  values to reveal all units on the map. When using full-map sonar you don't
  have to select a target location, instead the super weapon will be fired when
  you click its cameo icon. Defaults to :value:`10`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`Stealth`.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum`
  Specifies the houses affected by the sonar reveal. Defaults to
  :value:`enemies`.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum`
  Specifies which types the sonar affects. Defaults to :value:`water`, all unit
  types situated on water cells.


Sonar Pulse specific tags:

:tagdef:`[SuperWeapon]SonarPulse.Delay=integer - frames`
  The duration that the decloak effect will last. Defaults to :value:`60`.

.. index:: Super Weapons; SonarPulse briefly reveals cloaked units.

.. versionadded:: 0.1
.. versionchanged:: 0.5

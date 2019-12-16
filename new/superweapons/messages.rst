.. index:: Super Weapons; Message list texts as alternative to EVA events

Messages
````````

:tagdef:`[SuperWeapon]Message.Detected=CSF label`
  Message displayed to every player the moment the super weapon building is
  detected.
:tagdef:`[SuperWeapon]Message.Ready=CSF label`
  Message displayed to the firing player when the super weapon becomes ready to
  launch.
:tagdef:`[SuperWeapon]Message.Launch=CSF label`
  Message displayed to every player the moment the super weapon is launched.
:tagdef:`[SuperWeapon]Message.Activate=CSF label`
  Message displayed to every player the moment a deferrable super weapon is
  activated.
:tagdef:`[SuperWeapon]Message.Abort=CSF label`
  Message displayed to the firing player if the super weapon cannot be fired
  right now because another super weapon is active.
:tagdef:`[SuperWeapon]Message.InsufficientFunds=CSF label`
  Message displayed if the firing player doesn't have enough money to launch
  this super weapon.
:tagdef:`[SuperWeapon]Message.CannotFire=CSF label`
  Message displayed to the owning player if firing a super weapon using
  AITargeting fails. Defaults to :value:`MSG:CannotFire`.
:tagdef:`[SuperWeapon]Message.FirerColor=boolean`
  Messages are displayed in the firing house's color scheme. Defaults to
  :value:`no`.
:tagdef:`[SuperWeapon]Message.Color=Color scheme`
  If set, messages are always displayed in this color scheme instead of the
  player's color scheme. This is not respected if
  :value:`Message.FirerColor=yes` is set.

.. versionadded:: 0.2

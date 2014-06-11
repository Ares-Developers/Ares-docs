EVA Events
``````````

:tagdef:`[SuperWeapon]EVA.Detected=EVA event`
  The EVA event that will be triggered when the super weapon building is
  constructed (the EVA event is not played for the owner of the building).
:tagdef:`[SuperWeapon]EVA.Ready=EVA event`
  The EVA event that will be triggered when the super weapon is ready to fire
  (the EVA event is only played for the owner of the super weapon).
:tagdef:`[SuperWeapon]EVA.Activated=EVA event`
  The EVA event that will be triggered when the super weapon is fired.
:tagdef:`[SuperWeapon]EVA.Impatient=EVA event`
  The EVA event that will be triggered when a super weapon cameo is clicked but
  isn't ready to fire yet.
:tagdef:`[SuperWeapon]EVA.InsufficientFunds=EVA event`
  The EVA event that will be triggered when a super weapon can't be fired
  because the player doesn't have enough money. Defaults to
  :value:`EVA_InsufficientFunds`.
:tagdef:`[SuperWeapon]EVA.SelectTarget=EVA event`
  The EVA event that will be triggered when the super weapon cameo is clicked
  in the sidebar and the player is required to select a target.

To disable an EVA event, use the value :value:`none`.

.. index:: Super Weapons; Custom EVA events.

.. versionadded:: 0.1
.. versionchanged:: 0.4

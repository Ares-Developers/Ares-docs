:captiontag:`Gunner` IFVs
`````````````````````````

Multiple IFVs
~~~~~~~~~~~~~

The :tag:`[FV]` was the only unit to be checked for the special turret and
weapon flags, such as :tag:`SniperTurretIndex`. With :game:`Ares`, all
:type:`VehicleTypes` with :tag:`Gunner=yes` set will read those flags. This
means that you can now have multiple types of IFV.

.. index:: Units; IFV clones

.. versionadded:: 0.1


:captiontag:`VoiceIFVRepair`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :game:`Ares` you can specify the :tag:`VoiceIFVRepair` tag on any IFV unit.

:tagdef:`[VehicleType]VoiceIFVRepair=soundmd entry`
  Specifies the response this IFV gives when ordered to repair something. If
  this value is not set, :tag:`[VehicleType]VoiceAttack` is used. Defaults to 
  :tag:`[AudioVisual]VoiceIFVRepair` for :tag:`[FV]`, otherwise to
  :value:`none`.

.. index:: Units; VoiceIFVRepair can be specified on any IFV unit.

.. versionadded:: 0.2

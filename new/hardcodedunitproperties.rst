Hard-coded Unit Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~

The game is hard-coded to do certain things with certain unit IDs. Namely the
:tag:`[COW]`, :tag:`[DESO]` and :tag:`[FV]`. These units can now have said
special properties switched off, and other units can be given these properties
if you want. Hard-coded properties of Cows and Desolators can be toggled on/off
for any infantry.


:captiontag:`IsCow`
```````````````````

The :tag:`[COW]` was hard-coded to play its idle animation more frequently than
other infantry and was also hard-coded to move around randomly. You can now set
:tag:`IsCow=yes` on other :type:`InfantryTypes` or, indeed, :tag:`IsCow=no` on
the :tag:`[COW]`.

:tagdef:`[InfantryType]IsCow=boolean`
  Defaults to :value:`yes` for :tag:`[COW]`, otherwise to :value:`no`.

.. index:: Infantry; Define whether an InfantryType behaves like a cow.

.. versionadded:: 0.1


:captiontag:`IsDesolator`
`````````````````````````

The :tag:`[DESO]` was hard-coded to have different deploy-weapon firing timing
than other units. The change to the timing appears to be related to the unit's
art :tag:`Sequence` although the exact effect has not been investigated. You can
now set :tag:`IsDesolator=yes` on other :type:`InfantryTypes` or, indeed,
:tag:`IsDesolator=no` on the :tag:`[DESO]`.

:tagdef:`[InfantryType]IsDesolator=boolean`
  Defaults to :value:`yes` for :tag:`[DESO]`, otherwise to :value:`no`.

.. index:: Infantry; Enable or disable the Desolator special handling.

.. versionadded:: 0.1


Multiple IFVs / :captiontag:`Gunner`
````````````````````````````````````

The :tag:`[FV]` was the only unit to be checked for the special turret and
weapon flags, such as :tag:`SniperTurretIndex`. With :game:`Ares`, all
:type:`VehicleTypes` with :tag:`Gunner=yes` set will read those flags. This
means that you can now have multiple types of IFV.

.. index:: Units; Custom IFV clones.

.. versionadded:: 0.1


:captiontag:`VoiceIFVRepair`
````````````````````````````

In :game:`Ares` you can specify the :tag:`VoiceIFVRepair` tag on any IFV unit.

:tagdef:`[VehicleType]VoiceIFVRepair=soundmd entry`
  Specifies the response this IFV gives when ordered to repair something. If
  this value is not set, :tag:`[VehicleType]VoiceAttack` is used. Defaults to 
  :tag:`[AudioVisual]VoiceIFVRepair` for :tag:`[FV]`, otherwise to
  :value:`none`.

.. index:: Units; VoiceIFVRepair can be specified on any IFV unit.

.. versionadded:: 0.2

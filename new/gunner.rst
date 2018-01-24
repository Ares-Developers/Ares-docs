:captiontag:`Gunner` IFVs
`````````````````````````

:tag:`Gunner=yes` units support changing their weapon depending on their first
passenger. While it was quite versatile for players and while it supported some
customization for modders, this logic added in :game:`Red Alert 2` was rather
rigidly hardcoded internally. :game:`Ares` changes this.


.. index::
  Units; Multiple IFVs
  Gunner; Multiple IFVs

Multiple IFVs
~~~~~~~~~~~~~

The :tag:`[FV]` was the only unit to be checked for the special turret and
weapon flags, such as :tag:`SniperTurretIndex`. With :game:`Ares`, all
:type:`VehicleTypes` with :tag:`Gunner=yes` set will read those flags. This
means that you can now have multiple types of IFV.

.. versionadded:: 0.1


.. index::
  Units; More than 18 weapons and turrets
  Weapons; More than 18 weapons and turrets
  Turrets; More than 18 weapons and turrets

More Turrets and Weapons
~~~~~~~~~~~~~~~~~~~~~~~~

:game:`Ares` supports more than 18 different turret and barrel voxels, which
means :tag:`TurretCount` now can be set to values greater than :value:`18`.
:tag:`TurretCount` values greater than :value:`127` are not supported, though.

Also, units having multiple turrets enabled by the use of :tag:`TurretCount`
have been expanded to support more than 18 weapons along with their elite
counterparts, thus more than 18 different :tag:`IFVMode`\ s are now possible.

.. versionadded:: 0.E


.. index::
  Units; More IFV Modes
  Gunner; More than 18 IFV Modes

Defining IFV Modes
~~~~~~~~~~~~~~~~~~

:game:`Ares` replaces the original parsing of the tags mapping weapons to
turrets like :tag:`InitiateWeaponIndex` and :tag:`InitiateTurretIndex`. No
longer are the values applied even though the weapon index is :value:`-1` (which
is the default and which usually resulted in corruptions and crashes).
:tag:`Gunner=yes` units will not change properties if their section is defined
for example in a map file without restating all those mappings.

For the additional :tag:`IFVMode`\ s :game:`Ares` adds an alternative way to
define which turret to use for which weapon using a single tag each. Also, a
warning message is put into the debug log if an index is set to an invalid
value.

:tagdef:`[TechnoType]WeaponTurretIndexX=integer - turret index`
  The turret index used when :tag:`WeaponX` and :tag:`EliteWeaponX` are active,
  defined by :tag:`IFVMode` on the passenger. :value:`X` is the number from
  :value:`1` to :tag:`WeaponCount`. Defaults to :value:`-1`.

  .. note:: Note that :tag:`WeaponX` is 1-based while :tag:`IFVMode` is 0-based.
    For example :tag:`IFVMode=4` activates :tag:`Weapon5` and uses the turret
    index set as :tag:`WeaponTurretIndex5`.

Optionally, the :tag:`Gunner=yes` unit can have its own custom tool tip text for
each active weapon, which can be set using the following tags.

Note that this is different from the original game's approach which focused on
the active turret index to determine what name to show. The game used hardcoded
labels for certain turrets and could also merge the final tool tip from the
passenger type's name and the transport's name.

:tagdef:`[TechnoType]WeaponUINameX=CSF label`
  If set, is used as tool tip for this :tag:`Gunner=yes` unit if weapon
  :value:`X` is active. :value:`X` is the number from :value:`1` to
  :tag:`WeaponCount`. If not set, defaults to the original behavior.

.. versionadded:: 0.E


.. index::
  Units; VoiceIFVRepair per IFV unit
  Gunner; VoiceIFVRepair per unit

:captiontag:`VoiceIFVRepair`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :game:`Ares` you can specify the :tag:`VoiceIFVRepair` tag on any IFV unit.

:tagdef:`[VehicleType]VoiceIFVRepair=soundmd entry`
  Specifies the response this IFV gives when ordered to repair something. If
  this value is not set, :tag:`[VehicleType]VoiceAttack` is used. Defaults to 
  :tag:`[AudioVisual]VoiceIFVRepair` for :tag:`[FV]`, otherwise to
  :value:`none`.

.. versionadded:: 0.2

.. index::
  Weapons; Switch to other weapon if ammo is empty
  TechnoTypes; Switch to other weapon if ammo is empty

:captiontag:`NoAmmoWeapon`
~~~~~~~~~~~~~~~~~~~~~~~~~~

Units and structures usually always use the same weapon against the same target.
If the weapon is not charged because ammo is depleted, the unit will wait for it
to reload. It will not try the next available weapon that might not even need
ammunition.

This feature works like :tag:`OpenTransportWeapon` (which forces another weapon
on the condition that a unit is in an open-topped transport). It can be used to
make the unit or structure switch to a less powerful weapon automatically and
use it until ammo has been reloaded, or to disable firing any weapon when set to
a weapon that requires ammo.

:tagdef:`[TechnoType]NoAmmoWeapon=integer`
  The weapon index to switch to when there is no ammo left. This will override
  the normal weapon selection and only allow this weapon to be selected. Valid
  values :value:`0` for the primary weapon and :value:`1` for the secondary. Use
  :value:`-1` to not switch weapons. Defaults to :value:`-1`.

  .. note:: This tag cannot override the :tag:`DeployFireWeapon` enabled by
    :tag:`DeployFire=yes` on :type:`VehicleTypes` and :tag:`InfantryTypes`.

:tagdef:`[TechnoType]NoAmmoAmount=integer`
  If the current ammo is equal to or below this value, the :tag:`NoAmmoWeapon`
  will be used. Defaults to :value:`0`.

.. versionadded:: 0.C

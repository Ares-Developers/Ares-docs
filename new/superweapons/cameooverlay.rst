Cameo Overlay Texts
```````````````````

These texts will overlay the cameo in the sidebar to show the super weapon's
current status.

:tagdef:`[SuperWeapon]Text.Hold=CSF label`
  Overlay displayed in case this super weapon is powered and can't currently
  charge because the building is shut down.
:tagdef:`[SuperWeapon]Text.Ready=CSF label`
  Overlay displayed in case this super weapon is fully charged and ready to be
  launched.
:tagdef:`[SuperWeapon]Text.Charging=CSF label`
  Overlay displayed in case this super weapon has :tag:`UseChargeDrain=yes` set
  and can be fired, but it isn't fully charged yet.
:tagdef:`[SuperWeapon]Text.Active=CSF label`
  Overlay displayed in case this super weapon has :tag:`UseChargeDrain=yes` set
  and is currently enabled and draining.
:tagdef:`[SuperWeapon]Text.Preparing=CSF label`
  Overlay displayed in case none of the above texts are shown for this super
  weapon. That is, for example, charging for super weapons not using charge
  drain.

.. versionadded:: 0.2

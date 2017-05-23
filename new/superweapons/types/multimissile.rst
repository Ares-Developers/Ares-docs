:captiontag:`Type=MultiMissile`
```````````````````````````````

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Damage=integer`
  The damage the nuclear missile delivers. Negative values indicate to use the
  payload weapon's damage. Defaults to :value:`-1`.
:tagdef:`[SuperWeapon]SW.Warhead=Warhead`
  The warhead used to deal the damage of the nuke. If this is empty, the payload
  weapon's warhead will be used. Defaults to :value:`none`.
:tagdef:`[SuperWeapon]SW.ActivationSound=Sound`
  The nuke warn siren played at the destination. Defaults to
  :tag:`[AudioVisual]DigSound`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`Nuke`.
:tagdef:`[SuperWeapon]Light.*=integer`
  Default to :tag:`Light.Ambient=200`, :tag:`Light.Red=175`,
  :tag:`Light.Green=150`, and :tag:`Light.Blue=125` respectively.
:tagdef:`[SuperWeapon]Cursor=mouse cursor`
  Defaults to :value:`Nuke`.


Nuclear missile specific tags:

:tagdef:`[SuperWeapon]Nuke.Payload=Weapon`
  The Weapon used to display the downward-pointing nuke and as default, if
  :tag:`SW.Damage` and :tag:`SW.Warhead` aren't set. Defaults to
  :value:`NukePayload`.
:tagdef:`[SuperWeapon]Nuke.TakeOff=Animation`
  The Animation played on the missile silo when the missile is launched.
  Defaults to :tag:`[General]NukeTakeOff`.
:tagdef:`[SuperWeapon]Nuke.PsiWarning=Animation`
  The Animation played at the nuke target, detectable by Psychic Sensors.
  Defaults to :value:`PSIWARN`.
:tagdef:`[SuperWeapon]Nuke.SiloLaunch=boolean`
  Whether this missile is launched from a building with :tag:`NukeSilo=yes`
  providing this super weapon. Otherwise the weapon defined by
  :tag:`Nuke.Payload` is created off-screen, aiming for the target cell.
  Defaults to :value:`yes`.


Other changes:

Use :tag:`WeaponType` to control the properties of the upward flying animation
(especially its :tag:`Projectile`). :game:`Ares` respects the :tag:`WeaponType`
for every nuke, it will not use the :tag:`WeaponType` of the first superweapon
with :tag:`Type=Nuke` like :game:`Yuri's Revenge` did. Also mind to set
:tag:`NukeMaker=yes` on the :tag:`WeaponType`, otherwise the nuke will not come
down again.

:game:`Ares` supports multiple buildings with :tag:`NukeSilo=yes` providing this
super weapon. :game:`Yuri's Revenge` only tried to find the first building type
that matched those criteria.

:game:`Yuri's Revenge` supported the nuke impact animation only for the warhead
called :tag:`NUKE`, hardcoded to :tag:`NUKEBALL`. To change this animation in
:game:`Ares`, have a look at :ref:`PreImpactAnim <preimpactanim>`.

.. versionadded:: 0.2


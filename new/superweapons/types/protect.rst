:captiontag:`Type=IronCurtain` and :captiontag:`Type=ForceShield`
`````````````````````````````````````````````````````````````````

The difference between :tag:`Type=IronCurtain` and :tag:`Type=ForceShield` are
the default values used. :tag:`Type=ForceShield` will always use the force
shield protection color for buildings, otherwise the iron curtain color is used.
At the moment, the color cannot be customized.

Default values for general tags:

:tagdef:`[SuperWeapon]SW.Range=float,integer`
  Range affected by the protection. Defaults to
  :tag:`[General]ForceShieldRadius` for :value:`ForceShield`, to :value:`3,3`
  otherwise.
:tagdef:`[SuperWeapon]SW.Animation=Animation`
  Defaults to :tag:`[General]ForceShieldInvokeAnim` for :value:`ForceShield`, to
  :tag:`[General]IronCurtainInvokeAnim` otherwise.
:tagdef:`[SuperWeapon]SW.AnimationHeight=integer`
  The height the :tag:`SW.Animation` is played above the ground. Defaults to
  :value:`5`.
:tagdef:`[SuperWeapon]SW.AITargeting=enum`
  Defaults to :value:`ForceShield` for :value:`ForceShield`, to :value:`none`
  otherwise and the AI cannot use this.
:tagdef:`[SuperWeapon]SW.AffectsHouse=enum`
  Specifies the houses affected by the protection. Defaults to :value:`team` for
  :value:`ForceShield`, to :value:`all` otherwise.
:tagdef:`[SuperWeapon]SW.AffectsTarget=enum`
  Specifies which types the protection affects. Defaults to :value:`buildings`
  for :value:`ForceShield`, to :value:`all` otherwise.
:tagdef:`[SuperWeapon]SW.RequiresTarget=enum`
  Specifies which types the protection can be fired upon. Defaults to
  :value:`buildings` for :value:`ForceShield`, to :value:`all` otherwise.
:tagdef:`[SuperWeapon]SW.RequiresHouse=enum`
  Defaults to :value:`team` for :value:`ForceShield`, to :value:`none`
  otherwise.


Iron Curtain and Force Shield specific tags:

:tagdef:`[SuperWeapon]Protect.Duration=integer - frames`
  The length the protection effect endures. Defaults to
  :tag:`[General]ForceShieldDuration` for :value:`ForceShield`, to
  :tag:`[CombatDamage]IronCurtainDuration` otherwise.
:tagdef:`[SuperWeapon]Protect.PowerOutage=integer - frames`
  The length the owning player will expericence a power outage after firing this
  super weapon. Defaults to :tag:`[General]ForceShieldBlackoutDuration` for
  :value:`ForceShield`, to :value:`0` otherwise.
:tagdef:`[SuperWeapon]Protect.PlayFadeSoundTime=integer - frames`
  This many frames before the protection effect ends the
  :tag:`[SuperWeapon]SpecialSound` is played. Must be lower than
  :tag:`Protect.Duration`. Defaults to
  :tag:`[General]ForceShieldPlayFadeSoundTime` for :value:`ForceShield`, to
  :value:`0` otherwise.

The duration of the protection can be customized for each :type:`TechnoType`.
See the :doc:`Force Shield Modifier </new/forceshield>` section for
:tag:`Type=ForceShield`, otherwise see the :ref:`Iron Curtain Effect on Warheads
<wh-ironcurtain>` section.

.. versionadded:: 0.2

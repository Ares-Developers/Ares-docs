.. index::
  Bounty; Rewards for killing enemies
  TechnoTypes; Bounty awarded for killings

Bounty
~~~~~~

Units and structures can be awarded bounty for killing enemies, either by firing
at them or crushing them. This bounty is a defined amount of credits that can be
customized for each :type:`TechnoType`.

The following tags are global settings to enable bounty only if players own
certain buildings and to define the default to display the bounty amount.

:tagdef:`[General]BountyEnablers=list of BuildingTypes`
  Bounty will be enabled only after a building of a type in this list is owned
  by the player. If the list is empty, bounty will always be enabled.. Defaults
  to :value:`none`.

:tagdef:`[AudioVisual]BountyDisplay=boolean`
  Whether enemy units and structures will display the amount of bounty awarded
  when destroyed by an object of this type. Defaults to :value:`no`.


The following tags are for units or structures bounty is awarded to.

:tagdef:`[TechnoType]Bounty=boolean`
  Whether this object will be awarded bounty when destroying enemy units or
  structures either by firing at them or by crushing them. Defaults to
  :value:`no`.

:tagdef:`[TechnoType]Bounty.Display=boolean`
  Whether enemy units and structures will display the amount of bounty awarded
  when destroyed by an object of this type. Defaults to
  :tag:`[AudioVisual]BountyDisplay`.


The following tags define properties on victims, the units and structures
destroyed by bounty hunters.

:tagdef:`[TechnoType]Bounty.Value=integer - credits`
  The amount rewarded as bounty if this becomes the victim of a bounty hunter.
  Can be negative to penalize the player. If set, resets the veterancy level
  specific values. Defaults to :value:`0`.

:tagdef:`[TechnoType]Bounty.RookieValue=integer - credits`

:tagdef:`[TechnoType]Bounty.VeteranValue=integer - credits`

:tagdef:`[TechnoType]Bounty.EliteValue=integer - credits`
  The amount rewarded as bounty if an object with this veterancy is destroyed.
  Can be negative to penalize the player. Defaults to :tag:`Bounty.Value`.

.. versionadded:: 0.C

Cloak Depending On State
````````````````````````

Cloak Only If Standing Still (:captiontag:`CloakStop`)
------------------------------------------------------

In :game:`Tiberian Sun` units were supposed to be made to cloak only when they
stopped moving using :tag:`CloakStop=yes`. This tag was never actually working
though. :game:`Ares` implements it.

.. note:: \ :tag:`CloakStop=yes` is not supported for :tag:`BalloonHover=yes`
  units. It does not work without :tag:`Cloakable=yes`. :value:`CLOAK` ability
  will not be affected by it.

.. index: Cloak; CloakStop restored.

.. versionadded:: 0.5


Cloak Only If Deployed
----------------------

Infantry can be made cloakable only when deployed. When undeployed, the infantry
will decloak again. This applies to all active cloaking abilities like
:tag:`Cloakable=yes` or the :value:`CLOAK` ability. Only Cloak Generators will
cloak the infantry even if not deployed.

:tagdef:`[InfantryType]Cloakable.Deployed=boolean`
  Whether this infantry is only allowed to self-cloak when deployed. Requires
  \ :tag:`Deployer=yes` and :tag:`Cloakable=yes`. Defaults to :value:`no`.

.. index: Cloak; Cloakable only if infantry is deployed.

.. versionadded:: 0.5


Cloak Only If Powered
---------------------

:tag:`Powered=yes` buildings stay cloaked even if they have no power. This can
be changed using the following tag. This does not affect buildings cloaked by a
Cloak Generator.

:tagdef:`[BuildingType]Cloakable.Powered=boolean`
  Whether this building will uncloak when shut down or in low-power situations.
  Otherwise the building will be allowed to cloak. Defaults to :value:`no`.

.. index: Cloak; Cloakable only if building has power.

.. versionadded:: 0.5


Disallow Cloaking
-----------------

This can be used to create :game:`Tiberium Wars`-style stealth generators like
the Disruption Tower, which cloaks everything around but stays uncloaked itself,
even if other Disruption Towers are placed nearby.

:tagdef:`[TechnoType]Cloakable.Allowed=boolean`
  Whether this techno is allowed to cloak at all. If set to :value:`no`, this
  techno is not allowed to be cloaked (neither through self-cloak nor through
  Cloak Generators). Defaults to :value:`yes`.
  
If a unit is disallowed from cloaking, it will not receive cloak bonuses through
crates. In case a crate provides the cloaking ability, it will fall back to
money.

.. index: Cloak; Uncloakable technos.

.. versionadded:: 0.5

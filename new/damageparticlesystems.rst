Damage Sparks
~~~~~~~~~~~~~

There was a hardcoded setting in the games since :game:`Tiberian Sun` that
enabled :type:`InfantryTypes` with :tag:`Cyborg=yes` to repeatedly spawn damage
spark particle systems when damaged into yellow or red healh. The setting was
cleared whenever the infantry's section was not present in the map or scenario
file. :game:`Ares` unties this feature from :tag:`Cyborg` and :type:`InfantryTypes` by
making this a proper tag.

See `DamageParticleSystems on ModEnc
<http://modenc.renegadeprojects.com/DamageParticleSystems>`_ for a thorough
description of this feature.

:tagdef:`[TechnoType]DamageSparks=boolean`
  Defines whether an object of this type should spawn spark particle systems
  defined by :tag:`DamageParticleSystems`. Defaults to :tag:`Cyborg` for
  :type:`InfantryTypes`, to :value:`no` otherwise.

.. index:: Units; Damage sparks for all TechnoTypes.

.. versionadded:: 0.7

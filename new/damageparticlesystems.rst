Damage Particle Systems
~~~~~~~~~~~~~~~~~~~~~~~

Damage particle systems are used to visually indicate a unit has been damaged
severely, by either emitting smoke when the unit enters yellow or red health or
by sparking repeatedly. See `DamageParticleSystems on ModEnc
<http://modenc.renegadeprojects.com/DamageParticleSystems>`_ for a thorough
description of this feature.


.. index::
  Particles; Damage sparks for all TechnoTypes
  TechnoTypes; Damage sparks for all types

Damage Sparks
-------------

There was a hardcoded setting in the games since :game:`Tiberian Sun` that
enabled :type:`InfantryTypes` with :tag:`Cyborg=yes` to repeatedly spawn damage
spark particle systems when damaged into yellow or red health. The setting was
cleared whenever the infantry's section was not present in the map or scenario
file. :game:`Ares` unties this feature from :tag:`Cyborg` and
:type:`InfantryTypes` by making this a proper tag.

:tagdef:`[TechnoType]DamageSparks=boolean`
  Defines whether an object of this type should spawn spark particle systems
  defined by :tag:`DamageParticleSystems`. Defaults to :tag:`Cyborg` for
  :type:`InfantryTypes`, to :value:`no` otherwise.

.. versionadded:: 0.7


.. index::
  Particles; Smoke and Spark DamageParticleSystems 
  Units; DamageParticleSystems

Smoke and Spark :captiontag:`DamageParticleSystems`
---------------------------------------------------

:game:`Ares` adds two new tags that allow arbitrary damage particle systems
where previously only one with either :tag:`BehavesLike=Smoke` or
:tag:`BehavesLike=Spark` were possible.

The new tag does not enforce the restrictions the original tag had. Without
opting in by using the new ones, damage particle systems are spawned as always.

.. warning:: Only :value:`Smoke` and :value:`Spark` particle systems are fully
  supported as of Ares 0.7, because the others need special handling that is not
  yet in place.

:tagdef:`[TechnoType]DamageSmokeParticleSystems=list of ParticleSystems`
  Defines a list of :type:`ParticleSystems` to randomly spawn from when an
  object is damaged into yellow or red health. You have to use this if you want
  to use :type:`ParticleSystems` with :tag:`BehavesLike` set to other values
  than :value:`Smoke`. Defaults to all :tag:`DamageParticleSystems` with
  :tag:`BehavesLike=Smoke` set.

:tagdef:`[TechnoType]DamageSparksParticleSystems=list of ParticleSystems`
  Defines a list of :type:`ParticleSystems` to randomly spawn from when an
  object is in yellow or red health. You have to use this if you want
  to use :type:`ParticleSystems` with :tag:`BehavesLike` set to other values
  than :value:`Spark`. Defaults to all :tag:`DamageParticleSystems` with
  :tag:`BehavesLike=Spark` set.

.. versionadded:: 0.7

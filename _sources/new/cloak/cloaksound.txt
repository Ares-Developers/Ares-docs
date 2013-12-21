Cloak Sounds
````````````

There was only one global sound used to indicate a change of cloak state.
:game:`Ares` split this into two separate flags for cloaking and decloaking, and
made both of them customizable for each :type:`TechnoType`.

:tagdef:`[AudioVisual]DecloakSound=Sound`
  The sound played when a unit or building decloaks. Defaults to
  \ :tag:`[AudioVisual]CloakSound`.

:type:`TechnoTypes` can override the global sounds. It does not matter whether
the unit cloaks itself or whether it is cloaked by a Cloak Generator.

:tagdef:`[TechnoType]CloakSound=Sound`
  The sound played when this object cloaks or submerges. Defaults to
  \ :tag:`[AudioVisual]CloakSound`.

:tagdef:`[TechnoType]DecloakSound=Sound`
  The sound played when this object decloaks or emerges. Defaults to
  \ :tag:`[AudioVisual]DecloakSound`.

.. index: Cloak; Customizable cloak and decloak sounds.

.. versionadded:: 0.5

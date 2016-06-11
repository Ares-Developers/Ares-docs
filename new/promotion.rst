Promotion settings
~~~~~~~~~~~~~~~~~~

Global :captiontag:`VeteranFlashTimer`
--------------------------------------

:game:`Yuri's Revenge` allowed units to flash only when they were promoted to
elite veterancy. :game:`Ares` adds a new global tag that works like
:tag:`EliteFlashTimer`.

:tagdef:`[AudioVisual]VeteranFlashTimer=integer - frames`
  The number of frames a newly veteran unit or structure will flash for.
  Defaults to :value:`0`.

.. index:: AudioVisual; Global VeteranFlashTimer


Sounds, EVA and Flashing
------------------------

The following tags can be used to customize the sounds played and the flashing
when the unit or structure is promoted.

:tagdef:`[TechnoType]Promote.VeteranSound=sound`
  The sound played when a unit of this type is promoted to veteran. Defaults to
  :tag:`[AudioVisual]UpgradeVeteranSound`.

:tagdef:`[TechnoType]Promote.EliteSound=sound`
  The sound played when a unit of this type is promoted to elite. Defaults to
  :tag:`[AudioVisual]UpgradeEliteSound`.

:tagdef:`[TechnoType]Promote.VeteranFlash=integer - frames`
  The number of frames a unit or structure of this type flashes when promoted to
  veteran. Defaults to :tag:`[AudioVisual]VeteranFlashTimer`.

:tagdef:`[TechnoType]Promote.EliteFlash=integer - frames`
  The number of frames a unit or structure of this type flashes when promoted to
  elite. Defaults to :tag:`[AudioVisual]EliteFlashTimer`.

:tagdef:`[TechnoType]EVA.VeteranPromoted=EVA message`
  The message played when a unit or structure of this type is promoted to
  veteran level. Defaults to :value:`EVA_UnitPromoted`.

:tagdef:`[TechnoType]EVA.ElitePromoted=EVA message`
  The message played when a unit or structure of this type is promoted to
  elite level. Defaults to :value:`EVA_UnitPromoted`.

.. index:: TechnoTypes; Promotion customizations

.. versionadded:: 0.C

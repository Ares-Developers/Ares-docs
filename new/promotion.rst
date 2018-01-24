Promotion settings
~~~~~~~~~~~~~~~~~~

.. index:: Art; Global VeteranFlashTimer

Global :captiontag:`VeteranFlashTimer`
--------------------------------------

:game:`Yuri's Revenge` allowed units to flash only when they were promoted to
elite veterancy. :game:`Ares` adds a new global tag that works like
:tag:`EliteFlashTimer`.

:tagdef:`[AudioVisual]VeteranFlashTimer=integer - frames`
  The number of frames a newly veteran unit or structure will flash for.
  Defaults to :value:`0`.


.. index::
  Veterancy; Promotion customizations
  TechnoTypes; Promotion customizations

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

.. versionadded:: 0.C


.. index::
  OpenTopped; Promote passengers as if they are part of the transport
  Veterancy; Promote passengers as if they are part of the transport

Promote all Passengers
----------------------

The following setting can be used on :tag:`OpenTopped=yes` transports with
Initial Payload, which are used to imitate multiple weapons but logically only
count as one unit. This works best with :tag:`Experience.PromotePassengers=no`
and optionally :tag:`Experience.FromPassengers=yes`.

This does not forward "experience" as the ratio of a destroyed object's cost and
the own cost. Instead, this forwards the "rank" like veteran and elite. A
Guardian GI inside a Battle Fortress will always mirror the transport's rank,
despite being much cheaper than the vehicle and thus usually promoted earlier. 

:tagdef:`[TechnoType]Promote.IncludePassengers=boolean`
  Whether all :tag:`Trainable=yes` passengers will be set to the same rank if
  the rank of this transport unit changes. Defaults to :value:`no`.

  .. note:: The passengers' veterancy is discarded when the vehicle is promoted.
    This should not be used on manually controllable transports, because they
    could degrade elite passengers to veterans, for example.

.. versionadded:: 0.E

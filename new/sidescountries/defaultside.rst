Side Defaults
~~~~~~~~~~~~~

These are the side defaults used instead of global tags.


Crew, Survivors and Other Types
-------------------------------

:tagdef:`[Side]Crew=InfantryType`
  The :type:`InfantryType` that is spawned as a survivor when objects (with
  :tag:`Crewed=yes` set) owned by this side are destroyed (or, in the case of
  buildings, sold).
:tagdef:`[Side]Engineer=InfantryType`
  The :type:`InfantryType` that has a chance to be spawned when buildings with
  :tag:`Factory=BuildingType` owned by this side are destroyed or sold. Defaults
  to :tag:`[General]Engineer`.
:tagdef:`[Side]Technician=InfantryType`
  The :type:`InfantryType` that has a chance to be spawned when armed objects
  owned by this side are destroyed or sold. Defaults to
  :tag:`[General]Technician`.
:tagdef:`[Side]DefaultDisguise=InfantryType`
  Default :type:`InfantryType` that disguisable infantry will be disguised as
  when first created.
:tagdef:`[Side]SurvivorDivisor=integer`
  An object's refund amount is divided by this number to determine how many
  survivors will be spawned when this object is destroyed (or, in the case of
  buildings, sold).

.. versionadded:: 0.1
.. versionchanged:: 0.5


AI and Base-Building
--------------------

:tagdef:`[Side]AI.BaseDefenses=list of BuildingTypes`
  List of base defense buildings that the AI can build.
:tagdef:`[Side]AI.BaseDefenseCounts=list of integers`
  The maximum amount of base defense building that the AI can build.
  (listed as AI difficulties: hard, medium, easy)  Defaults to
  :tag:`[General]AlliedBaseDefenseCounts` for GDI (Allied),
  :tag:`[General]SovietBaseDefenseCounts` for Nod (Soviet), and
  :tag:`[General]ThirdBaseDefenseCounts` for ThirdSide (Yuri).

.. versionadded:: 0.1


Paradrop Defaults
-----------------

:tagdef:`[Side]ParaDrop.Types=list of InfantryTypes and/or VehicleTypes`
  The units that will be paradropped by :tag:`Type=ParaDrop` super weapons (such
  as the one normally provided by a Tech Airport) for this side. Defaults to
  :tag:`[General]AllyParaDropInf` for GDI (Allied),
  :tag:`[General]SovParaDropInf` for Nod (Soviet), and
  :tag:`[General]YuriParaDropInf` for ThirdSide (Yuri).

  .. note:: The original flags used to control the paradrop units only accept
    \ :type:`InfantryTypes`. To include :type:`VehicleTypes` in a paradrop you
    *have to* use the new :tag:`ParaDrop.Types` and :tag:`ParaDrop.Num` flags.
:tagdef:`[Side]ParaDrop.Num=list of integers`
  The quantity of each corresponding unit (listed against :tag:`ParaDrop.Types`)
  that will be paradropped. Defaults to :tag:`[General]AllyParaDropNum` for GDI
  (Allied), :tag:`[General]SovParaDropNum` for Nod (Soviet), and
  :tag:`[General]YuriParaDropNum` for ThirdSide (Yuri).
:tagdef:`[Side]ParaDrop.Aircraft=AircraftType`
  The aircraft type that will be used to deliver paradrops. Defaults to
  :value:`PDPLANE`.
:tagdef:`[Side]Parachute.Anim=Animation`
  This side's default parachute used if not overridden by the country or a
  :type:`TechnoType`. Defaults to :value:`PARACH`.

.. versionadded:: 0.2


Hunter Seeker Defaults
----------------------

.. _sides-hunterseeker:

:tagdef:`[Side]HunterSeeker=VehicleType`
  The unit used as default Hunter Seeker for the Hunter Seeker super weapon.
  Replaces :tag:`[General]GDIHunterSeeker` and :tag:`[General]NodHunterSeeker`
  from :game:`Tiberian Sun`. Set this to a :type:`VehicleType` with Fly
  locomotor as specified under :doc:`Hunter Seeker </new/hunterseeker>`.
  Defaults to :value:`none`.

.. versionadded:: 0.7

Prerequisites
~~~~~~~~~~~~~

The prerequisite system has been enhanced in several ways. New flags are
described below, and an issue has been resolved with regard to upgrades as
prerequisites (see Type 2 Fixes).

:tagdef:`[Unit]Prerequisite.RequiredTheaters=list of theater names`
  The map theaters in which the unit is available. Defaults to all theaters. For
  example, if only the :value:`SNOW` theater were specified then the unit would
  only be available on arctic maps. This allows you to implement, for example,
  the :tag:`AlternateArcticArt` functionality used on the Navy SEAL, but for all
  unit types and all theaters (however this may present challenges for your AI).
  The theater names are:

    + :value:`TEMPERATE` - most maps
    + :value:`SNOW` - arctic/snowy maps
    + :value:`URBAN` - some city maps
    + :value:`DESERT` - some desert maps, older maps use Temperate
    + :value:`LUNAR` - Soviet Mission 6
    + :value:`NEWURBAN` - most YR urban maps

  .. note:: \ :tag:`PrerequisiteOverride` does *not* override
    \ :tag:`Prerequisite.RequiredTheaters`.

.. index:: Prerequisites; Units can require the map to be a specific theater (desert/snow/lunar/etc).

.. versionadded:: 0.1


:tagdef:`[Unit]Prerequisite.Negative=list of BuildingTypes`
  The buildings that preclude construction of the unit. If the player owns one
  or more of the buildings on this list then the unit will not be available.
  Defaults to :value:`none`.

  .. note:: \ :tag:`PrerequisiteOverride` does *not* override
    \ :tag:`Prerequisite.Negative`.

.. index:: Prerequisites; PrerequisiteNegative makes a unit unavailable if a
  building on the list is owned.

.. versionadded:: 0.1


:tagdef:`[Unit]Prerequisite.Lists=integer`
  Specifies how many extra Prerequisite lists are available (see below).
  Defaults to :value:`0`.

:tagdef:`[Unit]Prerequisite.List#=list of BuildingTypes (where # is the 1-based index of the prerequisite list, the maximum specified by Prerequisite.Lists)`
  Each prerequisite list acts as an independent copy of the existing
  :tag:`Prerequisite` flag. For example, if you set
  :tag:`Prerequisite=GAPILE,GATECH` and :tag:`Prerequisite.List1=NAHAND,NATECH`
  then the unit will be available to any player who owns both an Allied Barracks
  and Battle Lab, or a Soviet Barracks and Battle Lab (a minimum of one of the
  prerequisite lists must be satisfied). :tag:`Prerequisite.List0`, if
  specified, overrides the existing :tag:`Prerequisite` flag.

  .. index:: Prerequisites; Multiple separate prerequisite lists - a unit can
    require any one of several sets of buildings.

.. versionadded:: 0.1


:tagdef:`[Unit]Prerequisite.StolenTechs=list of integers`
  The list of stealable technology types that must be stolen before this object
  can be built. See Stolen Technology for more information.

.. index:: Prerequisites; New StolenTech requirements.

.. versionadded:: 0.1


Below is a flowchart of the current prerequisite system. Blue sections
are unchanged from the original system. Pink sections have been
modified or added by :game:`Ares`.



Generic Prerequisite Groups
```````````````````````````

You can now create custom generic prerequisite groups like the existing
:value:`POWER` (:tag:`PrerequisitePower`), :value:`FACTORY`
(:tag:`PrerequisiteFactory`), :value:`BARRACKS` (:tag:`PrerequisiteBarracks`),
:value:`RADAR` (:tag:`PrerequisiteRadar`), :value:`TECH`
(:tag:`PrerequisiteTech`) and :value:`PROC` (:tag:`PrerequisiteProc` and
:tag:`PrerequisiteProcAlternate`) groups.

To create new groups simply include the new :tag:`[GenericPrerequisites]`
section and add flags with the format :tag:`GROUPNAME=` (list of BuildingTypes).
For example:


::

    [GenericPrerequisites]
    NAVALYARD=GAYARD,NAYARD,YAYARD
    etc...



::

    [TechnoType]
    ...
    Prerequisites=NAVALYARD
    ...


If you declare any of the existing groups (:value:`POWER`/:value:`FACTORY`/\
:value:`BARRACKS`/:value:`RADAR`/:value:`TECH`/:value:`PROC`) then the
BuildingTypes specified in the :tag:`[GenericPrerequisites]` section will be
used *instead* of those specified on the original PrerequisiteGroup flags
(i.e. :tag:`[GenericPrerequisites]POWER=`, if specified, overrides
:tag:`[General]PrerequisitePower=`). Take note that
:tag:`[GenericPrerequisites]PROC=` does not override or nullify
:tag:`[General]PrerequisiteProcAlternate=`.

.. index:: Prerequisites; New Prerequisite Groups.

.. versionadded:: 0.1

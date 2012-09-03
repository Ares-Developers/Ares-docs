Prerequisites
~~~~~~~~~~~~~

The prerequisite system has been enhanced in several ways. New flags
are described below, and an issue has been resolved with regard to
upgrades as prerequisites (see Type 2 Fixes). Prerequisites:

:[Unit]Prerequisite.RequiredTheaters= (list of theater names): The map
theaters in which the unit is available. Defaults to all theaters. For
example, if only the SNOW theater were specified then the unit would
only be available on arctic maps. This allows you to implement, for
example, the `AlternateArcticArt` functionality used on the Navy SEAL,
but for all unit types and all theaters (however this may present
challenges for your AI). The theater names are:

    + TEMPERATE - most maps
    + SNOW - arctic/snowy maps
    + URBAN - some city maps
    + DESERT - some desert maps, older maps use Temperate
    + LUNAR - Soviet Mission 6
    + NEWURBAN - most YR urban maps
`PrerequisiteOverride` does *not* override
  `Prerequisite.RequiredTheaters`. Units can require the map to be a
  specific theater (desert/snow/lunar/etc).
  Prerequisite.RequiredTheaters=
.. versionadded:: 0.1 :[Unit]Prerequisite.Negative= (list of
  BuildingTypes): The buildings that preclude construction of the unit.
  If the player owns one or more of the buildings on this list then the
  unit will not be available. `PrerequisiteOverride` does *not* override
  `Prerequisite.Negative`. PrerequisiteNegative makes a unit unavailable
  if a building on the list is owned. Prerequisite.Negative=
.. versionadded:: 0.1 :[Unit]Prerequisite.Lists= (integer):
  Specifies how many extra Prerequisite lists are available (see below).
  Defaults to zero. Prerequisite.Lists=
:[Unit]Prerequisite.List#= (list of BuildingTypes) (where # is the
  1-based index of the prerequisite list, the maximum specified by
  `Prerequisite.Lists`): Each prerequisite list acts as an independent
  copy of the existing `Prerequisite` flag. For example, if you set
  `Prerequisite=GAPILE,GATECH` and `Prerequisite.List1=NAHAND,NATECH`
  then the unit will be available to any player who owns both an Allied
  Barracks and Battle Lab, or a Soviet Barracks and Battle Lab (a
  minimum of one of the prerequisite lists must be satisfied).
  `Prerequisite.List0`, if specified, overrides the existing
  `Prerequisite` flag. Multiple separate prerequisite lists - a unit can
  require any one of several sets of buildings. Prerequisite.List#=
.. versionadded:: 0.1 :[Unit]Prerequisite.StolenTechs= (list of
  integers): The list of stealable technology types that must be stolen
  before this object can be built. See Stolen Technology for more
  information. New StolenTech requirements. Prerequisite.StolenTechs=
.. versionadded:: 0.1

Below is a flowchart of the current prerequisite system. Blue sections
are unchanged from the original system. Pink sections have been
modified or added by Ares.



Generic Prerequisite Groups
```````````````````````````

You can now create custom generic prerequisite groups like the
existing `POWER` ( `PrerequisitePower`), `FACTORY` (
`PrerequisiteFactory`), `BARRACKS` ( `PrerequisiteBarracks`), `RADAR`
( `PrerequisiteRadar`), `TECH` ( `PrerequisiteTech`) and `PROC` (
`PrerequisiteProc` and `PrerequisiteProcAlternate`) groups.

To create new groups simply include the new `[GenericPrerequisites]`
section and add flags with the format `GROUPNAME=` (list of
BuildingTypes). For example:


::

    [GenericPrerequisites]
    		NAVALYARD=GAYARD,NAYARD,YAYARD
    		etc...



::

    [TechnoType]
    		...
    		Prerequisites=NAVALYARD
    		...


If you declare any of the existing groups ( `POWER`/ `FACTORY`/
`BARRACKS`/ `RADAR`/ `TECH`/ `PROC`) then the BuildingTypes specified
in the `[GenericPrerequisites]` section will be used *instead* of
those specified on the original `PrerequisiteGroup` flags (i.e.
`[UnitType]POWER=`, if specified, overrides
`[UnitType]PrerequisitePower=`). Take note that `[BuildingType]PROC=`
does not override or nullify
`[BuildingType]PrerequisiteProcAlternate=`. New Prerequisite Groups.
GenericPrerequisites

.. versionadded:: 0.1

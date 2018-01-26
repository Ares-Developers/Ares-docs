Prerequisites
~~~~~~~~~~~~~

The prerequisite system has been enhanced in several ways. New flags are
described below, and an issue has been resolved with regard to upgrades as
prerequisites (see
:doc:`/bugfixes/type2/buildingtypeupgradesarenotviableprerequisites`).

.. index:: Prerequisites; Require the map to be a specific theater (desert/snow/lunar/etc)

Require Theater
```````````````

:tagdef:`[TechnoType]Prerequisite.RequiredTheaters=list of theater names`
  The map theaters in which the type is available. Defaults to all theaters. For
  example, if only the :value:`SNOW` theater were specified then the type would
  only be available on arctic maps. This allows you to implement, for example,
  the :tag:`AlternateArcticArt` functionality used on the Navy SEAL, but for all
  types and all theaters (however this may present challenges for your AI). The
  theater names are:

    + :value:`TEMPERATE` - most maps
    + :value:`SNOW` - arctic/snowy maps
    + :value:`URBAN` - some city maps
    + :value:`DESERT` - some desert maps, older maps use Temperate
    + :value:`LUNAR` - Soviet Mission 6
    + :value:`NEWURBAN` - most YR urban maps

  .. note:: \ :tag:`PrerequisiteOverride` does *not* override
    \ :tag:`Prerequisite.RequiredTheaters`.

.. versionadded:: 0.1


.. index:: Prerequisites; Make an object unavailable if a listed building is owned

Negative Prerequisites
``````````````````````

:tagdef:`[TechnoType]Prerequisite.Negative=list of BuildingTypes`
  The buildings that preclude construction of the type. If the player owns one
  or more of the buildings on this list then the type will not be available.
  Defaults to :value:`none`.

  .. note:: \ :tag:`PrerequisiteOverride` does *not* override
    \ :tag:`Prerequisite.Negative`.

.. versionadded:: 0.1


.. index:: Prerequisites; Multiple separate prerequisite lists

Multiple Alternative Prerequisites Lists
````````````````````````````````````````

:game:`Ares` supports more than one prerequisite list. Each prerequisite list
acts as an independent copy of the existing :tag:`Prerequisite` flag, and a
minimum of one of the prerequisite lists must be satisfied for this type to
become buildable.

For example, if you set :tag:`Prerequisite=GAPILE,GATECH` and
:tag:`Prerequisite.List1=NAHAND,NATECH` then the object will be available to any
player who owns both an Allied Barracks and Battle Lab, or a Soviet Barracks and
Battle Lab.

.. note:: Either :tag:`Prerequisite` or :tag:`Prerequisite.List0` has to be
  specified, because these are only *additional* lists and the original
  prerequisites list is still used. If this is ignored and the list is left
  empty, the object will become always buildable, because an empty list is
  always satisfied.

:tagdef:`[TechnoType]Prerequisite.Lists=integer`
  Specifies how many extra Prerequisite lists complimentary to the one default
  list are available. Defaults to :value:`0`.

:tagdef:`[TechnoType]Prerequisite.List#=list of BuildingTypes (where # is the 1-based index of the prerequisite list, the maximum specified by Prerequisite.Lists)`
  The :type:`BuildingTypes` required to satisfy this prerequisite list. Each
  list is checked on its own, and if any list is satisfied, the Prerequisite
  requirement is satisfied.
  
  .. note:: \ :tag:`Prerequisite.List0`, if specified, overrides the existing
    \ :tag:`Prerequisite` flag.

.. versionadded:: 0.1


.. index:: Prerequisites; Require stolen tech 

Require Stolen Technology
`````````````````````````

:tagdef:`[TechnoType]Prerequisite.StolenTechs=list of integers`
  The list of stealable technology types that must be stolen before this object
  can be built. See :ref:`Stolen Technology <spybehavior-stolentech>` for more
  information.

.. versionadded:: 0.1


.. index:: Prerequisites; Require building initially built by certain country

Require Factory Built By Country
````````````````````````````````

:tagdef:`[BuildingType]FactoryOwners.HaveAllPlans=boolean`
  Whether a player capturing a building of this type would permanently gain all
  plans of its initial owner. The initial owner is the player who owned it
  first: the player who built it, or the owner of buildings pre-placed on the
  map. For neutral structures, this would be the neutral country. Defaults to
  :value:`no`.
:tagdef:`[TechnoType]FactoryOwners=list of houses`
  The list of countries whose factories can build this object. If empty, every
  country is allowed to build this object. Otherwise, players need to own at
  least one factory built by a country in this list or the plans of at least one
  of these countries to produce it.
:tagdef:`[TechnoType]FactoryOwners.Forbidden=list of houses`
  The list of countries whose factories cannot build this object. Players owning
  only factories built by countries in this list and only having plans of these
  countries are prevented from producing it.

.. note:: AI ignores :tag:`FactoryOwners` and :tag:`FactoryOwners.Forbidden` on
  buildings, but not on units.

.. versionadded:: 0.6
.. versionchanged:: 0.9


Overview
````````

Below is a flowchart of the current prerequisite system. Blue sections
are unchanged from the original system. Pink sections have been
modified or added by :game:`Ares`.

.. image:: /images/prerequisite_system.svg
  :alt: Flowchart of the current prerequisite system
  :align: center


.. index:: Prerequisites; Prerequisite groups

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

.. versionadded:: 0.1


.. index::
  Prerequisites; Generalized alternate prerequisite groups
  Prerequisites; Units as prerequisite

Alternate Prerequisites with Non-Buildings
``````````````````````````````````````````

To support the Slave Miner as prerequisite, :game:`Yuri's Revenge` added the
option to satisfy the :value:`PROC` requirement by either owning the deployed
building or alternatively the undeployed Slave Miner vehicle. This was done only
for the refinery group by adding :tag:`[General]PrerequisiteProcAlternate=`,
which accepted one :type:`VehicleType`.

:game:`Ares` adds alternate prerequisites support for all Generic Prerequisite
Groups and expands this feature to support multiple items of arbitrary
:type:`TechnoTypes`.

:tagdef:`[General]PrerequisiteXAlternate=list of TechnoTypes`
  A list of types that alternatively satisfy this requirement if player does not
  own a building from the :tag:`[General]PrerequisiteX=` list.

  Replace :tag:`X` with a key from :tag:`[GenericPrerequisites]`, first
  character upper case, all others lower case. For instance, :value:`NAVALYARD`
  from above would become :value:`Navalyard`.

  .. note:: Using :type:`BuildingTypes` is not supported and adding them here
    might give unexpected results. For example, upgrades will not work.

.. versionadded:: 0.B

.. index::
  Hunter Seeker; How to set up
  Universe; Hunter Seekers

Hunter Seeker
~~~~~~~~~~~~~

The Hunter Seeker known from :game:`Tiberian Sun` is a :type:`VehicleType` that
uses the Fly locomotor and has :tag:`HunterSeeker=yes` set. It is launched by
the :doc:`Hunter Seeker super weapon </new/superweapons/types/hunterseeker>`.

Refer to `ModEnc <http://modenc.renegadeprojects.com/HunterSeeker>`_ for
more information about Hunter Seeker's movement and targeting logic.

.. versionadded:: 0.7


.. index::
  Super Weapons; Hunter Seeker global settings
  Vehicles; Hunter Seeker settings

Global Settings
---------------

The following tags define the defaults for the Hunter Seeker super weapons and
all :type:`VehicleTypes` with :tag:`HunterSeeker=yes` set. The tags do not
default to meaningful values, but the values :game:`Tiberian Sun` uses are given
here for reference.

Default for super weapons:

:tagdef:`[SpecialWeapons]HSBuilding=list of BuildingTypes`
  Buildings that can launch Hunter Seekers. :type:`BuildingTypes` in this list
  do not have to provide the Hunter Seeker super weapon. Either this or the
  corresponding tag on the super weapon have to be set. If the player does not
  own any building from this list, the super weapon will discharge without a
  Hunter Seeker being launched. Defaults to :value:`none`, :game:`Tiberian Sun`
  uses :value:`GAPLUG,NATMPL`.

Defaults for :type:`VehicleTypes`:

:tagdef:`[General]HunterSeekerDetonateProximity=integer`
  Distance to target in leptons below which the Hunter Seeker will detonate.
  Defaults to :value:`0`, :game:`Tiberian Sun` uses :value:`150`.
:tagdef:`[General]HunterSeekerDescendProximity=integer`
  Distance to target in leptons where the Hunter Seeker will start to descend.
  Defaults to :value:`0`, :game:`Tiberian Sun` uses :value:`700`.
:tagdef:`[General]HunterSeekerAscentSpeed=integer`
  Speed value used while rising to a higher flight level. Defaults to
  :value:`0`, :game:`Tiberian Sun` uses :value:`40`.
:tagdef:`[General]HunterSeekerDescentSpeed=integer`
  Speed value used while going down to a lower flight level. Defaults to
  :value:`0`, :game:`Tiberian Sun` uses :value:`50`.
:tagdef:`[General]HunterSeekerEmergeSpeed=integer`
  Speed value used when ascending from the launch site. Defaults to :value:`0`,
  :game:`Tiberian Sun` uses :value:`6`.

Hunter Seeker Unit Settings
---------------------------

These tags override the global tags for each unit type. Only the Fly locomotor
makes use of these values.

:tagdef:`[VehicleType]HunterSeeker.DetonateProximity=integer`
  Distance to target in leptons below which the Hunter Seeker will detonate.
  Defaults to :tag:`[General]HunterSeekerDetonateProximity`.
:tagdef:`[VehicleType]HunterSeeker.DescendProximity=integer`
  Distance to target in leptons where the Hunter Seeker will start to descend.
  Defaults to :tag:`[General]HunterSeekerDescendProximity`.
:tagdef:`[VehicleType]HunterSeeker.AscentSpeed=integer`
  Speed value used while rising to a higher flight level. Defaults to
  :tag:`[General]HunterSeekerAscentSpeed`.
:tagdef:`[VehicleType]HunterSeeker.DescentSpeed=integer`
  Speed value used while going down to a lower flight level. Defaults to
  :tag:`[General]HunterSeekerDescentSpeed`.
:tagdef:`[VehicleType]HunterSeeker.EmergeSpeed=integer`
  Speed value used when ascending from the launch site. Defaults to
  :tag:`[General]HunterSeekerEmergeSpeed`.


.. index::
  Hunter Seeker; Make units untargetable
  TechnoTypes; Disallow targeting by Hunter Seeker

Disallow Targeting
------------------

A :type:`TechnoType` can be exempt from the target scan of all Hunter Seekers
enabling the tag below. This can help reduce frustration because vital or overly
expensive objects or insignificant or unreasonably cheap objects can be spared.
It can also be used for mission-critical objects in campaigns.

:tagdef:`[TechnoType]HunterSeeker.Ignore=boolean`
  Whether the Hunter Seeker will ignore targets of this type altogether, and not
  even randomly select them when no other target is eligible. Defaults to
  :value:`no`.

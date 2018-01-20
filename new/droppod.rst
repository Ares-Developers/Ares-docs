Drop Pods
~~~~~~~~~

These are the collected settings that apply to the Drop Pod locomotor in general
and the :doc:`Drop Pod super weapon </new/superweapons/types/droppod>`
specifically.

.. index:: Drop Pods; Locomotor

.. versionadded:: 0.7


Trailer
-------

The original Drop Pod trailer was not customizable and also not implemented in
an optimal way. Now the animation is looked up only once, not once for each Drop
Pod every six frames. Also, the smoke trailer now is created even if the Drop
Pod does not have a :tag:`[General]DropPodWeapon` set.

:tagdef:`[General]DropPodTrailer=AnimationType`
  The animation used as smoke trailer for Drop Pods. Defaults to
  :value:`SMOKEY`.


Global Super Weapon Defaults
----------------------------

The following tags define the defaults for the Drop Pod super weapons. The tags
do not default to meaningful values, but the values :game:`Firestorm` uses are
given here for reference.

:tagdef:`[General]DropPodTypes=list of InfantryTypes`
  The types to randomly choose from when spawning units for the Drop Pod super
  weapon. Each type has an equal chance of being selected. You can add types
  more than once. Only infantry is supported. Defaults to :value:`none`,
  :game:`Firestorm` uses an equivalent :value:`E1,E2`.
:tagdef:`[General]DropPodMinimum=integer`
  The minimum number of Drop Pods being created. Defaults to :value:`0`,
  :game:`Firestorm` uses :value:`5`.
:tagdef:`[General]DropPodMaximum=integer`
  The maximum number of Drop Pods being created. Defaults to :value:`0`,
  :game:`Firestorm` uses :value:`8`.


Miscellaneous
-------------

If the weapon used as :tag:`[General]DropPodWeapon` does not have at least one
valid :tag:`Report` sound set, the game will not crash any more when a Drop Pod
is spawned.

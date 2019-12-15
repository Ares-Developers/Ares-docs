.. index:: Universe; DropPod reinforcements

:captiontag:`Type=DropPod`
``````````````````````````

:game:`Ares` re-implements the Drop Pod SW (:tag:`Type=DropPod`) known from
:game:`Firestorm`. A super weapon of this type spawns between a minimum and a
maximum number of random units from a list of types, which all arrive in drop
pods.

.. note:: \ :game:`Firestorm` had the Drop Pods hardcoded to use :value:`E1`
  (Rifle Soldier) and :value:`E2` (Disk Thrower), a behavior that has not been
  recreated. :game:`Ares` uses no default types, thus do not forget to set them
  correctly.


Default values for general tags:

:tagdef:`[SuperWeapon]SW.AITargeting=enumeration`
  Defaults to :value:`DropPod`.
:tagdef:`[SuperWeapon]EVA.Detected=EVA event`
  Defaults to :value:`EVA_DropPodDetected`.
:tagdef:`[SuperWeapon]EVA.Ready=EVA event`
  Defaults to :value:`EVA_DropPodReady`.
:tagdef:`[SuperWeapon]EVA.Activated=EVA event`
  Defaults to :value:`EVA_DropPodActivated`.
:tagdef:`[SuperWeapon]Cursor=mouse cursor`
  Defaults to :value:`ParaDrop`.


Drop Pod specific tags:

:tagdef:`[SuperWeapon]DropPod.Types=list of InfantryTypes`
  The types to choose from. Each type has an equal chance of being selected. You
  can add types more than once. Only infantry is supported. Defaults to
  :tag:`[General]DropPodTypes`.
:tagdef:`[SuperWeapon]DropPod.Veterancy=float`
  The veterancy level the units will start with, if they do not have a higher
  initial rank already. Values between :value:`0.0` and
  :tag:`[General]VeteranCap` are valid. Defaults to :value:`2.0` (elite).
:tagdef:`[SuperWeapon]DropPod.Minimum=integer`
  The minimum number of Drop Pods being created. Defaults to
  :tag:`[General]DropPodMinimum`.
:tagdef:`[SuperWeapon]DropPod.Maximum=integer`
  The maximum number of Drop Pods being created. Defaults to
  :tag:`[General]DropPodMaximum`.

Drop pods need clear ground around them to be spawned. If a unit cannot find a
place to land and another cell to spawn above, another random unit and new cell
close to the last cell are picked. The maximum number of retries for placing all
units is 3 times the number of units to spawn. In case this limit is exceeded,
the super weapon stops to place more units.

See :doc:`Drop Pods </new/droppod>` for information about the global defaults
and other related additions.

.. versionadded:: 0.7
.. versionchanged:: 3.0

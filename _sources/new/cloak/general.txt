General Changes and Updates
```````````````````````````

Powered Units
-------------

Deactivated units (using either the :tag:`PoweredBy=` or :value:`PoweredUnit=`
logic) and units whose drivers have been killed lose the ability to cloak
themselves, and they will uncloak automatically. The units are still allowed to
be cloaked by allied Cloak Generators in range.

.. index: Cloak; Deactivated powered units will uncloak.

.. versionadded:: 0.5


Parasites
---------

In the original :game:`Yuri's Revenge`, parasites like the Terror Drone were
ejected from a unit when it cloaked. This has been changed so the parasite stays
inside the victim and continues damaging it.

.. index: Cloak; Parasites will not be ejected.

.. versionadded:: 0.5

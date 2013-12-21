Cloaking and Units Above Ground
```````````````````````````````

Units can now cloak and be cloaked by Cloak Generators regardless of their
height above ground, where they were only cloaked in :game:`Yuri's Revenge` if
they sat directly on the ground, which prevented hover vehicles from recloaking
correctly. This is now supported.

Units with :tag:`Cloakable=yes` or the :value:`CLOAK` ability can cloak
regardless of height. Other units will be cloaked by Cloak Generators only if
their height is below this value:

:tagdef:`[General]CloakHeight=integer`
  The height below which units are cloaked by Cloak Generator buildings. Units
  above this height will not be affected (though they can still self-cloak).
  Defaults to :tag:`[General]HoverHeight`.
  
  .. note:: \ :game:`Yuri's Revenge` defaulted to :value:`0`.

.. index: Cloak; Support for units hovering above the ground.

.. versionadded:: 0.5

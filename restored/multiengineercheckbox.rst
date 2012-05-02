Multi Engineer Checkbox
~~~~~~~~~~~~~~~~~~~~~~~

:game:`Tiberian Sun` lets the user enable and disable the Multi Engineer feature
from the user interface. :game:`Ares` restores this feature. If the user turns
off Multi Engineer in the skirmish menu, buildings can always be captured using
an engineer, otherwise the settings in :file:`rulesmd.ini` are used.

.. index:: Multi Engineer checkbox in Skirmish menu.

:tagdef:`[UISettings]AllowMultiEngineer=bool`
  Specifies whether the user can turn the Multi Engineer feature on and off from
  the menu. Defaults to :value:`no`. If the checkbox is not shown the settings
  in :file:`rulesmd.ini` will be enforced.

See :doc:`/restored/multiengineer` for more info on :tag:`EngineerDamage` and
:tag:`EngineerCaptureLevel`.

.. note:: Currently only the skirmish menu supports changing the Multi Engineer
  option. This will be changed in the future to support network and online games
  as well.

.. versionadded:: 0.2

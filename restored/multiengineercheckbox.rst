Multi Engineer Checkbox
~~~~~~~~~~~~~~~~~~~~~~~

Tiberian Sun lets the user enable and disable the Multi Engineer
feature from the user interface. Ares restores this feature. If the
user turns off Multi Engineer buildings can always be captured using
an engineer, otherwise the settings in rulesmd.ini are used. Multi
Engineer checkbox in Skirmish menu.



:[UISettings]AllowMultiEngineer= (bool): Specifies whether the user
  can turn the Multi Engineer feature on and off from the menu. Defaults
  to `no`. If the checkbox is not shown the settings in rulesmd.ini will
  be enforced. AllowMultiEngineer=


See Multi Engineer for more info on `EngineerDamage` and
`EngineerCaptureLevel`.

NB: Currently only the skirmish menu supports changing the Multi
Engineer option. This will be changed in the future to support network
and online games as well.

.. versionadded:: 0.2



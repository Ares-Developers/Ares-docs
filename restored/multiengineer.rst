Multi Engineer
~~~~~~~~~~~~~~

Red Alert introduced a way to balance engineers. By being able to
capture a building only if has been damaged already engineer rushes
became a lot more difficult. If the building could not be captured the
engineer would damage it instead. ``EngineerDamage`` is not present in
Yuri's Revenge. Ares restores this feature. Multi Engineer.



:[General]EngineerCaptureLevel= (float - level): Specifies the health
  level equal to or below the building has to be capture it.
  EngineerCaptureLevel=
:[General]EngineerDamage= (float - percent): If the building can not
  be captured the engineer will damage it by this amount of its full
  health. EngineerDamage=
:[General]EngineerAlwaysCaptureTech= (boolean): Specifies whether tech
  buildings can be captured no matter what their current health status
  is. EngineerAlwaysCaptureTech=
:[General]EngineerDamageCursor.*= (Cursor): Specifies the cursor to
  indicate an engineer will only damage the building instead of
  capturing it. See Super weapon cursors Defaults to a previously unused
  detonator cursor.


Use sensible defaults. Generally, `EngineerDamage` should never be
higher than `EngineerCaptureLevel` or there might be situations an
engineer blows up the building to be captured.
EngineerDamageCursor.Count= EngineerDamageCursor.Frame=
EngineerDamageCursor.HotSpot= EngineerDamageCursor.Interval=
EngineerDamageCursor.MiniCount= EngineerDamageCursor.MiniFrame=
See Multi Engineer Checkbox to enable the user to turn the Multi
Engineer option on and off from the game menu. If the checkbox is not
enabled, the game will force the settings defined in rulesmd.ini.

.. versionadded:: 0.2


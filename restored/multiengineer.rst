Multi Engineer
~~~~~~~~~~~~~~

:game:`Red Alert` introduced a way to balance engineers. By being able to
capture a building only if has been damaged already engineer rushes became a lot
more difficult. If the building could not be captured the engineer would damage
it instead. :tag:`EngineerDamage` is not present in :game:`Yuri's Revenge`.
:game:`Ares` restores this feature.

.. image:: /images/engineerdamage.png
  :alt: Screenshot of an Engineer going to damage a building
  :align: center

:tagdef:`[General]EngineerCaptureLevel=float - percent`
  If the building's health is equal to or below this percentage of its strength
  it can be captured by an engineer instead of being damaged. Defaults to
  \ :value:`1.0`.
:tagdef:`[General]EngineerDamage=float - percent`
  If the building cannot be captured the engineer will damage it by this amount
  of its full health. Defaults to :value:`0.0`.
:tagdef:`[General]EngineerAlwaysCaptureTech=boolean`
  Specifies whether tech buildings can be captured no matter what their current
  health status is. Defaults to :value:`yes`.

  .. note:: All structures originally owned by countries with
    \ :tag:`MultiplayPassive=yes` are considered tech structures. This
    definition  is likely to change in a later version.
:tagdef:`[General]EngineerDamageCursor.*=cursor definition`
  Specifies the cursor to indicate an engineer will only damage the building
  instead of capturing it. See :doc:`Mouse Cursors </new/cursors>`. Defaults to
  a previously unused detonator cursor.

.. note:: Use sensible defaults. Generally, :tag:`EngineerDamage` should never
  be higher than :tag:`EngineerCaptureLevel` or there might be situations an
  engineer blows up the building to be captured.

See :doc:`/restored/multiengineercheckbox` to enable the user to turn the Multi
Engineer option on and off from the game menu. If the checkbox is not enabled,
the game will enforce the settings defined in :file:`rulesmd.ini`.

.. versionadded:: 0.2

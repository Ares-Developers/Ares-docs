Unit Lost EVA Report
~~~~~~~~~~~~~~~~~~~~

If a unit is destroyed, EVA announces that the player has lost a unit. This EVA
report can now be customized or turned off.

.. note:: The EVA message is not played for units if :tag:`DontScore=yes`,
  \ :tag:`Insignificant=yes` or :tag:`Spawned=yes`.

:tagdef:`[Unit]EVA.Lost=evamd entry`
  The message played when a unit of this type is destroyed. Use :value:`none` to
  disable the report. Defaults to :value:`EVA_UnitLost`.

.. index:: EVA; Unit Lost report customizable.

.. versionadded:: 0.5

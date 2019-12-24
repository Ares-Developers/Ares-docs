.. index::
  EVA; Unit or Structure Lost message per type
  Infantry; Unit Lost EVA message
  Vehicles; Unit Lost EVA message
  Aircraft; Unit Lost EVA message
  Buildings; Structure Lost EVA message

Unit or Structure Lost EVA Report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a unit or a structure is destroyed, EVA announces to the owning player that
they have lost it. This EVA report can now be customized or turned off.

.. note:: The EVA message is not played for units or structures if
  \ :tag:`DontScore=yes`, :tag:`Insignificant=yes` or :tag:`Spawned=yes`.

:tagdef:`[TechnoType]EVA.Lost=evamd entry`
  The message played when a unit or strucure of this type is destroyed. Use
  :value:`none` to disable the report. Defaults to :value:`none` for structures,
  to :value:`EVA_UnitLost` otherwise.

.. versionadded:: 0.5
.. versionchanged:: 3.0

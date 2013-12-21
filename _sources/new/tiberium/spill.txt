Tiberium Spill
``````````````

Units carrying or buildings storing tiberium can spill their contents when
destroyed. This behavior is applied by default in :game:`Tiberian Sun`, and it
is optional in :game:`Ares`.

:tagdef:`[TechnoType]TiberiumSpill=boolean`
  Whether this techno with positive :tag:`Storage` will spill parts of its
  stored tiberium when destroyed. Defaults to :value:`no`.

Buildings like Refineries and Silos will spill as many bails as they have
stored. The spilled tiberium type depends on the tiberium stored inside the
building.

Units like Harvesters and Slaves can spill up to 9 bails of the first resource
from the :type:`Tiberiums` list depending on fill state, but not more than the
unit's :tag:`Storage`.

.. index: Tiberium; Technos can lose tiberium on destruction.

.. versionadded:: 0.5

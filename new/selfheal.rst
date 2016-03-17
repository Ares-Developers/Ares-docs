Self Heal
~~~~~~~~~

A unit's ability to self heal was hardcoded in :game:`Yuri's Revenge` and aside
from enabling it through veterancy and setting the interval after which the unit
would regain a fixed amount of health.

:game:`Ares` makes self healing much more customizable, which can be used to
recreate the Mammoth Tank from :game:`Tiberian Dawn`, which only recovered half
of its health.

:tagdef:`[TechnoType]SelfHealing.Rate=double - minutes`
  The minutes between applying the self heal. Defaults to
  :tag:`[General]RepairRate`.

:tagdef:`[TechnoType]SelfHealing.Max=double - percentage`
  The health level this object is restored to by self healing. The health will
  be capped at this percentage of the object's :tag:`Strength`. If defined,
  overrides the veterancy specific tags below. Defaults to :value:`100%`.

:tagdef:`[TechnoType]SelfHealing.RookieMax=double - percentage`

:tagdef:`[TechnoType]SelfHealing.VeteranMax=double - percentage`

:tagdef:`[TechnoType]SelfHealing.EliteMax=double - percentage`
  The health level this object is restored to by self healing, depending on its
  veterancy level. These settings are fully independent of each other. Defaults
  to :tag:`SelfHealing.Max`.

:tagdef:`[TechnoType]SelfHealing.Amount=integer - hitpoints`
  The amount of hitpoints restored when self healing. Cannot be less than
  :value:`0`. If defined, overrides the veterancy specific tags below. Defaults
  to :value:`1`.

:tagdef:`[TechnoType]SelfHealing.RookieAmount=integer - hitpoints`

:tagdef:`[TechnoType]SelfHealing.VeteranAmount=integer - hitpoints`

:tagdef:`[TechnoType]SelfHealing.EliteAmount=integer - hitpoints`
  The amount of hitpoints restored when self healing, depending on its
  veterancy level. These settings are fully independent of each other. Cannot be
  less than :value:`0`. Defaults to :tag:`SelfHealing.Amount`.

.. index:: Self Heal; Customizable rate, heal amount, and max level
.. index:: Self Heal; Tiberian Dawn Mammoths

.. versionadded:: 0.B

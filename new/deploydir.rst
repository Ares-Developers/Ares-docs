.. index:: TechnoTypes; DeployDir for each type

:captiontag:`DeployDir`
=======================

Originally, this setting was used for :tag:`DeployToLand=yes` units. When
ordered to deploy, they would turn towards this direction first.

With :game:`Ares`, all units having a :tag:`DeployingAnim` will turn towards
this direction first when deploying, ignoring :tag:`DeployToLand`. This way,
deploying anims can hide the transition of unit types better, while units not
having a :tag:`DeployingAnim` do not turn needlessly.

:tagdef:`[TechnoType]DeployDir=integer - facing`
  The direction a unit will face when deploying. Valid values range from
  :value:`0` for north to :value:`7` for north west. Defaults to
  :tag:`[General]DeployDir`.

.. versionadded:: 2.0

.. index:: AI; Control over AI's multiple factory-cloning behaviour.

=================================
Multiple AI Factories Clone Units
=================================

If the AI were modified to build multiple factories of the same type then every
time they built a unit from that factory type they would produce a copy of that
unit from every additional factory. For example, if the AI were made to build a
second War Factory then they would get a second copy of every vehicle they
build. This behavior can be disabled in :game:`Ares`, by the following flag:

:tagdef:`[GlobalControls]AllowParallelAIQueues=boolean`
	Set this to no to disable AI factory cloning. Defaults to :value:`yes`.

=======================================================
AI ignores :captiontag:`BuildLimit` when creating teams
=======================================================

In the original game the AI did not respect a unit's :tag:`BuildLimit` tag when
creating teams. :game:`Ares` changes this to disallow the AI from creating a
team if any unit's build limit would have to be violated. This new tag gives you
a way to restore the original behavior.

:tagdef:`[GlobalControls]AllowBypassBuildLimit= list of boolean`
	Allows AI to bypass build limits to create teams. This list is ordered by
	difficulty: easy, medium, hard. Use :value:`yes` to let the AI bypass build
	limits. Defaults to :value:`no,no,no`.

.. versionadded:: 0.1
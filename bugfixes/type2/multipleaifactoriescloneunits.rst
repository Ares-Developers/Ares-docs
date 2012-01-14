.. index:: AI; Control over AI's multiple factory-cloning behaviour.

=================================
Multiple AI Factories Clone Units
=================================

If the AI were modified to build multiple factories of the same type
then every time they built a unit from that factory type they would
produce a copy of that unit from every additional factory. For
example, if the AI were made to build a second War Factory then they
would get a second copy of every vehicle they build. This behavior can
be disabled in Ares, by the following flag:

``[GlobalControls]`` |>| ``AllowParallelAIQueues=`` :term:`boolean`
	Set this to no to disable AI factory cloning.

.. versionadded:: 0.1

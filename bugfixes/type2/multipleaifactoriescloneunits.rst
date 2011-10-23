Multiple AI Factories Clone Units
`````````````````````````````````

If the AI were modified to build multiple factories of the same type
then every time they built a unit from that factory type they would
produce a copy of that unit from every additional factory. For
example, if the AI were made to build a second War Factory then they
would get a second copy of every vehicle they build. This behavior is
disabled by default in Ares, although a flag has been added to allow
mod authors to turn it back on if they really want to:

:[GlobalControls]AllowParallelAIQueues= (boolean): Set this to yes to
  re-enable AI factory cloning.


If an AI is made to build multiple factories of the same type they
will no longer result in cloned units/buildings (this can be turned
back on if desired). GlobalControls AllowParallelAIQueues=
.. versionadded:: 0.1



<<<SEPARATOR>>>

.. index:: Glitches; Infantry jamming when using area attack

======================
Infantry Deploy Glitch
======================

Under certain circumstances, :tag:`Deployer=yes` infantry units with an
:tag:`UndeployDelay` greater than or equal to zero get jammed. This for instance
made the Yuri Clone helplessly hover in air for half a minute after using its
Area Fire deploy attack.

Due to a hole in the state machine for that mission, the game would fall back to
what appears to be the default handling to make such holes obvious. :game:`Ares`
plugs that hole.

.. versionadded:: 3.0

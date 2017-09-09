Movies List
~~~~~~~~~~~

With :game:`Ares` the in-game movies list can be customized and new unlockable
movies can be added. Each movie is now unlocked individually instead of using
only two campaign progression trackers for Allies and Soviets. The unlocked
state is saved in a new section called :tag:`[UnlockedMovies]` in
:file:`ra2md.ini`.

In the new file :file:`moviemd.ini`, add all movie filenames without the
:file:`.BIK` extension to the :tag:`[Movies]` list. All movies will appear on
the in-game menu in the same order as in this list. Only if the list is empty
does the game default to the original behavior using the hardcoded movie lists
and the two progression trackers.

Each movie item can be customized using these settings:

:tagdef:`[MovieFilename]Description=CSF label`
  The name this movie will appear under in the list. Defining this tag is
  required.

:tagdef:`[MovieFilename]Unlockable=boolean`
  Whether this movie has to be unlocked first before appearing in the list. If
  :value:`no`, the movie will always appear in the list, like the intro movie.
  Defaults to :value:`yes`.

Example:
  ::

    ; Assume INTRO.BIK and BRIEF01.BIK exist
    [Movies]
    0=INTRO
    1=BRIEF01
    
    [INTRO]
    Description=Name:IntroMovie
    Unlockable=no
    
    [BRIEF01]
    Description=Name:MissionName01

.. index:: Movies; Add new movies to the game

.. versionadded:: 0.E

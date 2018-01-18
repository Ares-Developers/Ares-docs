========
Glossary
========

.. glossary::

	bool
	boolean
	booleans
		Either :value:`yes` or :value:`no`, :value:`true` or :value:`false`,
		:value:`1` or :value:`0`.

	byte
	bytes
		All whole numbers from 0 to 255. For allowed formats see :term:`integer`

	cell
	cells
		Depending on context, range or distance as :term:`integer` or
		:term:`floating point value <float>`.

	clsid
	clsids
	locomotor
	locomotors
		One of the fixed locomotor clsids.

	color
	colors
		Color definition values, either in :term:`R,G,B <rgb>` or
		:term:`H,S,B <hsb>` notation.

	csf label
	csf string
		The name of an entry in the CSF file containing the translated strings
		displayed by the game. Label names can be up to 31 characters long.

	eva entry
	evamd entry
		The name of an EVA message defined in :file:`evamd.ini`.

	float
	floats
	double
	doubles
		Any decimal number, using the dot :value:`.` as decimal point. If the value
		ends with a percentage sign :value:`%`, the value is divided by 100.

	frame
	frames
		Ticks of game-time as :term:`integer`. One second of game-time is 15 frames;
		one minute of game-time is 900 frames. One second of game-time equals one
		second of real-time on normal game speed. Used to define durations, delays,
		or intervals.

	hsb
		Hue, Saturation, and Brightness is used much less frequently than
		:term:`RGB`. Similarly, each :term:`byte` represents the amount of each
		factor. However, it is important to note that the Tiberian Sun and Red Alert
		2 engines use a unique HSB color model that is not the same as the one used
		by most PC programs, like MS Paint. 

	integer
	integers
		Whole numbers from -2147483648 to 2147483647; in rare cases, only from
		-32768 to 32767. Allowed formats are all decimal numbers, and hexadecimal
		numbers either with a :value:`$` prefix or a :value:`H` or :value:`h`
		suffix. For example :value:`123`, :value:`$7b`, and :value:`7Bh` all mean
		the same.

	lepton
	leptons
		Distance as :term:`integer` as fractions of a :term:`cell`. 256 leptons are
		one cell.

	list
		A comma-separated list of items like integers or type names. Usually, lists
		can be up to 127 characters long.

	minute
	minutes
		Minutes as :term:`floating point value <float>`, with support for fractions.
		Multiplied by 900, gives the number of :term:`frames` of game-time. Used to
		define durations, delays, or intervals. Note that this is sometimes used as
		`real-time` minutes.

	modifier
	multiplier
		A :term:`floating point value <float>` used as a factor, that is it is being
		multiplied to strengthen or weaken an effect. :value:`1.0` or :value:`100%`
		usually mean an effect is not changed, while :value:`0.0` or :value:`0%`
		mean an effect is nullified. Depending on context, values larger than
		:value:`100%` are allowed.

	percent
	percents
	percentage
	percentages
	chance
		A :term:`floating point value <float>` that is used as a percentage value, a
		probability or a multiplier. Most commonly a value between :value:`0%` and
		:value:`100%`.
		
		Seldomly an :term:`integer` between :value:`0` and :value:`100`. Note that
		integer percentages `do not` end with a :value:`%` sign.

	rgb
		Red, Green, and Blue is the most common way colors are represented. Each
		:term:`byte` represents the amount of each color respectively, with
		:value:`0` as the minimum and :value:`255` as the maximum.

	sound entry
	soundmd entry
		The name of a sound entry defined in :file:`soundmd.ini`.

	special
		If given as a value type, this value doesn't conform to any typical format.
		Please check the context of the documentation to see how the value must be 
		formatted.

	string
	strings
		Normal text. Mind the length limits that apply.

	theme
	theme id
		The name of a theme entry defined in :file:`thememd.ini`.

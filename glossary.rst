========
Glossary
========

.. glossary::

	int
	integer
	integers
	signed integer
	signed integers
		All whole numbers from -2147483648 to 2147483647; in rare cases, only from -32768 to 32767.
	
	unsigned integer
	unsigned integers
		All non-negative whole numbers from 0 to either 32767, 2147483647 or 4294967296.
	
	float
	floats
	double
	doubles
		Any decimal number.
	
	byte
	bytes
	unsigned byte
	unsigned bytes
		All whole numbers from 0 to 255.
	
	signed byte
	signed bytes
		All whole numbers from -128 to 127.
	
	bool
	boolean
	booleans
		yes or no, true or false, 1 or 0.
	
	str
	string
	strings
		Normal text.
	
	stringlist
	listofstrings
		Character-separated list of :term:`strings`.
	
	intlist
	listofints
		Character-separated list of :term:`integers`.
		
	rgb
		Red, Green, and Blue is the most common way colors are represented. Each :term:`byte` represents the amount of each color respectively, with 0 as the minimum and 255 as the maximum.
		This color model is used with RadColor, for instance. 
	
	hsb
		Hue, Saturation, and Brightness is used much less frequently than :term:`RGB`. Similarly, each :term:`byte` represents the amount of each factor. However, it is important to note that the Tiberian Sun and Red Alert 2 engines use a unique HSB color model that is not the same as the one used by most PC programs, like MS Paint. 
		
	color
	colors
		Color definition values, either in :term:`R,G,B <rgb>` or :term:`H,S,B <hsb>` notation.
		This unique color model is used with flags in the ``[Colors]`` section. 
	
	clsid
	clsids
	locomotor
	locomotors
		Either a locomotor, or an AI general identifier.
	
	percent
	percents
	percentage
	percentages
	%
		Either a direct percentage (e.g. "50%"), or a :term:`floating point value <float>` (e.g. "0.5").

	special
		If given as a value type, this value doesn't conform to any typical format.
		Please check the context of the documentation to see how the value must be formatted.
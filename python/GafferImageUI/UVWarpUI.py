##########################################################################
#
#  Copyright (c) 2016, Image Engine Design Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import Gaffer
import GafferImage

Gaffer.Metadata.registerNode(

	GafferImage.UVWarp,

	"description",
	"""
	Warps an input image onto a set of UVs provided
	by a second image, effectively applying a texture
	map to the UV image.
	""",

	plugs = {

		"uv" : [

			"description",
			"""
			The UV image. The R and G channel are used to provide
			the U and V values, and these determine the source pixel
			in the main input image. A UV values of ( 0, 0 ) corresponds
			to the bottom left corner of the input image, and ( 1, 1 )
			corresponds to the top right corner.
			"""

		],
		"vectorMode" : [

			"description",
			"""
			Do vectors specify absolute positions in the source image, or relative
			offsets from the current pixel to the pixel in the source image.
			""",
			"preset:Absolute", GafferImage.UVWarp.VectorMode.Absolute,
			"preset:Relative", GafferImage.UVWarp.VectorMode.Relative,

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],
		"vectorUnits" : [

			"description",
			"""
			Are vectors measured in pixels, or as fractions of the input image display
			window ranging from 0 to 1.
			""",
			"preset:Pixels", GafferImage.UVWarp.VectorUnits.Pixels,
			"preset:Screen", GafferImage.UVWarp.VectorUnits.Screen,

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],


	}

)

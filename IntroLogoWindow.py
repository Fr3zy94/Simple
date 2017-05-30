#########################################
#										#
#	IntroLogo by .Eugen @ TheWarez.net	#
#										#
#########################################

import uiScriptLocale

window = {
	"name" : "IntroLogoWindow",
	
	"x" : 0,
	"y" : 0,
	
	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,
	
	"children" :
	(
		{
			"name" : "intro_bg", "type" : "expanrod_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/ro/ui/intro.jpg",
		},
		
		##IntroLogo
		{ "name" : "img_01", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/1.jpg" ), },
		{ "name" : "img_02", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/2.jpg" ), },
		{ "name" : "img_03", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/3.jpg" ), },
		{ "name" : "img_04", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/4.jpg" ), },
		{ "name" : "img_05", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/5.jpg" ), },
		{ "name" : "img_06", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/6.jpg" ), },
		{ "name" : "img_07", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/7.jpg" ), },
		{ "name" : "img_08", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/8.jpg" ), },
		{ "name" : "img_09", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/9.jpg" ), },
		{ "name" : "img_10", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/10.jpg" ), },
		{ "name" : "img_11", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/11.jpg" ), },
		{ "name" : "img_12", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/12.jpg" ), },
		{ "name" : "img_13", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/13.jpg" ), },
		{ "name" : "img_14", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/14.jpg" ), },
		{ "name" : "img_15", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/15.jpg" ), },
		{ "name" : "img_16", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/16.jpg" ), },
		{ "name" : "img_17", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/17.jpg" ), },
		{ "name" : "img_18", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/18.jpg" ), },
		{ "name" : "img_19", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/19.jpg" ), },
		{ "name" : "img_20", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/20.jpg" ), },
		{ "name" : "img_21", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/21.jpg" ), },
		{ "name" : "img_22", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/22.jpg" ), },
		{ "name" : "img_23", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/23.jpg" ), },
		{ "name" : "img_24", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/24.jpg" ), },
		{ "name" : "img_25", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/25.jpg" ), },
		{ "name" : "img_26", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/26.jpg" ), },
		{ "name" : "img_27", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/27.jpg" ), },
		{ "name" : "img_28", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/28.jpg" ), },
		{ "name" : "img_29", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/29.jpg" ), },
		{ "name" : "img_30", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/30.jpg" ), },
		{ "name" : "img_31", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/31.jpg" ), },
		{ "name" : "img_32", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/32.jpg" ), },
		{ "name" : "img_33", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/33.jpg" ), },
		{ "name" : "img_34", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/34.jpg" ), },
		{ "name" : "img_35", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/35.jpg" ), },
		{ "name" : "img_36", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/36.jpg" ), },
		{ "name" : "img_37", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/37.jpg" ), },
		{ "name" : "img_38", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/38.jpg" ), },
		{ "name" : "img_39", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/39.jpg" ), },
		{ "name" : "img_40", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/40.jpg" ), },
		{ "name" : "img_41", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/41.jpg" ), },
		{ "name" : "img_42", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/42.jpg" ), },
		{ "name" : "img_43", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/43.jpg" ), },
		{ "name" : "img_44", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/44.jpg" ), },
		{ "name" : "img_45", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/45.jpg" ), },
		{ "name" : "img_46", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/46.jpg" ), },
		{ "name" : "img_47", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/47.jpg" ), },
		{ "name" : "img_48", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/48.jpg" ), },
		{ "name" : "img_49", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/49.jpg" ), },
		{ "name" : "img_50", "type" : "image", "x" : 0, "y" : 0, "vertical_align" : "center", "horizontal_align" : "center", "image" : ( "locale/ro/ui/intrologo/50.jpg" ), },
	),	
}

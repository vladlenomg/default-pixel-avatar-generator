from PIL import Image, ImageDraw, ImageFont
import random
import textwrap

allpalette = ['malachite', 'deep ocean', 'ocean' , 'weed', 'palette 5', 'palette 6', 'palette 7', 'purple drank', 'hot pink', 'peach',
	         'fire', 'gold', 'palette 13', 'sky', 'dollar', 'palette 16', 'palette 17', 'gray', 'palette 19', 'palette 20', 'palette 21',
	         'palette 22', 'palette 23', 'palette 24', 'palette 25', 'palette 26', 'palette 27', 'fire on the water']

colors = {
	'malachite': ["#ffffe5","#f7fcb9","#d9f0a3","#addd8e","#78c679","#41ab5d","#238443","#006837","#004529"],
	'deep ocean': ["#ffffd9","#edf8b1","#c7e9b4","#7fcdbb","#41b6c4","#1d91c0","#225ea8","#253494","#081d58"],
	'ocean': ["#f7fcf0","#e0f3db","#ccebc5","#a8ddb5","#7bccc4","#4eb3d3","#2b8cbe","#0868ac","#084081"],
	'weed': ["#f7fcfd","#e5f5f9","#ccece6","#99d8c9","#66c2a4","#41ae76","#238b45","#006d2c","#00441b"],
	'palette 5': ["#fff7fb","#ece2f0","#d0d1e6","#a6bddb","#67a9cf","#3690c0","#02818a","#016c59","#014636"],
	'palette 6': ["#fff7fb","#ece7f2","#d0d1e6","#a6bddb","#74a9cf","#3690c0","#0570b0","#045a8d","#023858"],
	'palette 7': ["#f7fcfd","#e0ecf4","#bfd3e6","#9ebcda","#8c96c6","#8c6bb1","#88419d","#810f7c","#4d004b"],
	'purple drank': ["#fff7f3","#fde0dd","#fcc5c0","#fa9fb5","#f768a1","#dd3497","#ae017e","#7a0177","#49006a"],
	'hot pink': ["#f7f4f9","#e7e1ef","#d4b9da","#c994c7","#df65b0","#e7298a","#ce1256","#980043","#67001f"],
	'peach': ["#fff7ec","#fee8c8","#fdd49e","#fdbb84","#fc8d59","#ef6548","#d7301f","#b30000","#7f0000"],
	'fire': ["#ffffcc","#ffeda0","#fed976","#feb24c","#fd8d3c","#fc4e2a","#e31a1c","#bd0026","#800026"],
	'gold': ["#ffffe5","#fff7bc","#fee391","#fec44f","#fe9929","#ec7014","#cc4c02","#993404","#662506"],
	'palette 13': ["#fcfbfd","#efedf5","#dadaeb","#bcbddc","#9e9ac8","#807dba","#6a51a3","#54278f","#3f007d"],
	'sky': ["#f7fbff","#deebf7","#c6dbef","#9ecae1","#6baed6","#4292c6","#2171b5","#08519c","#08306b"],
	'dollar': ["#f7fcf5","#e5f5e0","#c7e9c0","#a1d99b","#74c476","#41ab5d","#238b45","#006d2c","#00441b"],
	'palette 16': ["#fff5eb","#fee6ce","#fdd0a2","#fdae6b","#fd8d3c","#f16913","#d94801","#a63603","#7f2704"],
	'palette 17': ["#fff5f0","#fee0d2","#fcbba1","#fc9272","#fb6a4a","#ef3b2c","#cb181d","#a50f15","#67000d"],
	'gray': ["#ffffff","#f0f0f0","#d9d9d9","#bdbdbd","#969696","#737373","#525252","#252525","#000000"],
	'palette 19': ["#7f3b08","#b35806","#e08214","#fdb863","#fee0b6","#f7f7f7","#d8daeb","#b2abd2","#8073ac","#542788","#2d004b"],
	'palette 20': ["#543005","#8c510a","#bf812d","#dfc27d","#f6e8c3","#f5f5f5","#c7eae5","#80cdc1","#35978f","#01665e","#003c30"],
	'palette 21': ["#40004b","#762a83","#9970ab","#c2a5cf","#e7d4e8","#f7f7f7","#d9f0d3","#a6dba0","#5aae61","#1b7837","#00441b"],
	'palette 22': ["#276419", "#4d9221", "#7fbc41", "#b8e186", "#e6f5d0", "#f7f7f7", "#fde0ef", "#f1b6da", "#de77ae", "#c51b7d", "#8e0152"],
	'palette 23': ["#053061", "#2166ac", "#4393c3", "#92c5de", "#d1e5f0", "#f7f7f7", "#fddbc7", "#f4a582", "#d6604d", "#b2182b", "#67001f"],
	'palette 24': ["#67001f","#b2182b","#d6604d","#f4a582","#fddbc7","#ffffff","#e0e0e0","#bababa","#878787","#4d4d4d","#1a1a1a"],
	'palette 25': ["#a50026","#d73027","#f46d43","#fdae61","#fee090","#ffffbf","#e0f3f8","#abd9e9","#74add1","#4575b4","#313695"],
	'palette 26': ["#9e0142","#d53e4f","#f46d43","#fdae61","#fee08b","#ffffbf","#e6f598","#abdda4","#66c2a5","#3288bd","#5e4fa2"],
	'palette 27': ["#a50026","#d73027","#f46d43","#fdae61","#fee08b","#ffffbf","#d9ef8b","#a6d96a","#66bd63","#1a9850","#006837"],
	'fire on the water':  ["#fdf0ce","#ffeca7","#f9b272","#f06351","#f07e66","#bee6e6","#bde7e6", "#92cbb8", "#93ccb9"]
}

def background(im, W, H, pixel, palette):
	draw = ImageDraw.Draw(im)
	for i in range(0, int(W / pixel)):
		for j in range(0, int(H / pixel)):
			random_color = colors[palette][random.randint(0, len(colors[palette])-1)]
			dots = [(i*pixel, j*pixel), (i*pixel, (j+1)*pixel), ((i+1)*pixel, (j+1)*pixel), ((i+1)*pixel, j*pixel)]
			draw.polygon(dots, fill=random_color)
	del draw


def rainbow_background(im, W, H, pixel, palette):
	draw = ImageDraw.Draw(im)
	for i in range(0,int(W / pixel)):
		for j in range(0,int(H / pixel)):
			if j <= int(H / pixel / 4):
				random_color = colors[palette][random.randint(0, 1)]

			if j > int(H / pixel / 4):
				random_color = colors[palette][random.randint(1, 3)]

			if j > int(H / pixel / 4) * 2:
				random_color = colors[palette][random.randint(3, 5)]

			if j > int(H / pixel / 4) * 3:
				random_color = colors[palette][random.randint(5, 8)]

			dots = [(i*pixel, j*pixel), (i*pixel, (j+1)*pixel), ((i+1)*pixel, (j+1)*pixel), ((i+1)*pixel, j*pixel)]
			draw.polygon(dots, fill=random_color)
	del draw


def draw_text(im, msg, fontsize, palette, W, H):
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype("fonts/Helvetica-Bold.ttf", fontsize)
	para = textwrap.wrap(msg, width=10)
	if len(para) == 0:
		pass
	elif len(para) == 1:
		w, h = draw.textsize(msg, font=font)
		draw.text(((W - w) / 2, (H - h) / 2), msg, fill=colors[palette][-1], font=font)
	else:
		current_h = int(H/4)
		pad =  10
		for line in para:
		    w, h = draw.textsize(line, font=font)
		    draw.text(((W - w) / 2, current_h), line, fill=colors[palette][-1], font=font)
		    current_h += h + pad

	del draw


def main(name = 'image', palette = 'purple drank', size = (500, 500), pixel = 20, rainbow = False, msg='', fontsize=250):
	im = Image.new('RGB', size)
	W = im.size[0]
	H = im.size[1]
	if rainbow:
		rainbow_background(im, W, H, pixel, palette)
	else:
		background(im, W, H, pixel, palette)
	
	draw_text(im, msg, fontsize, palette, W, H)
	im.save(str(name)+ ".png", "PNG")
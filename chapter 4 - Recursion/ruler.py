def draw_lines(tick_length,tick_label =''):
	"Draw one line with given tick length followed by optional label"
	line = "-"*tick_length
	if tick_label:
		line += " "+tick_label
	print(line)

def draw_interval(center_length):
	"Draw tick interval depending upon the tick length"
	if center_length > 0:
		draw_interval(center_length - 1)
		draw_lines(center_length)
		draw_interval(center_length-1)

def draw_ruler(num_inches,major_length):
	"Draw English ruler with given number of inches,major tick length"
	draw_lines(major_length,"0")
	for j in range(1,1+num_inches):
		draw_interval(major_length-1)
		draw_lines(major_length,str(j))

draw_ruler(1,4)


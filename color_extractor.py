import colorgram

colors = colorgram.extract("hirst_painting.jpeg", 10)
values = []

# Iterate to get tuple values for the 3 colors and save it in a variable
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors = (r, g, b)
    values.append(new_colors)
# print(values)

color_list = [(232, 242, 237), (192, 165, 115),(138, 166, 190), (56, 102, 140), (141, 91, 50),
              (12, 23, 55), (222, 207, 123)]
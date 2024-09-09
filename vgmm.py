import xml.etree.ElementTree as Et
import svgwrite
from svgwrite import mm
# import sign as sign


def vgmm(args):
    # Parse input file from XML
    root = parse_file(args.input_file)

    # Traverse XML tree and make appropriate calls to SVG library
    if root is not None:
        # Create the sign
        sign_assembly = make_sign(root)

        # Save the sign
        sign_assembly.saveas(args.output_file, indent = True, pretty = True)


def make_sign(root):
    # print(root.iter())
    sign = svgwrite.Drawing(profile = "full")

    for node in root.iter():
        if node.tag == "sign":
            process_sign(sign, node)
        # if node.tag == "ystack":
        #     sign.add(process_ystack(node))
        # elif node.tag == "xstack":
        #     sign.add(process_xstack(node))
        # elif node.tag == "text":
        #     sign.add(process_text(node))
        # elif node.tag == "arrow":
        #     sign.add(process_arrow(node))

    # sign.add(sign.rect((0, 0), (300, 75), fill = "#00755c"))
    # sign.add(sign.rect((1.5, 1.5), (300, 75), 8, 8, fill_opacity = 0.0, stroke = "white", stroke_width = 3))

    total_width = 800
    total_height = 600
    sign.viewbox(0, 0, total_width, total_height)

    return sign


def process_sign(sign, node):
    sign.add(get_plate(sign, (300, 75), get_color("green")))
    sign.add(sign.rect((1.5, 1.5), (300-3, 75-3), 8, 8, fill_opacity = 0.0, stroke = "white", stroke_width = 3))


def get_plate(sign, size, color, pos = (0, 0)):
    return sign.rect(pos, size, fill = color)


def get_color(color):
    if color == "green":
        return "#00755c"

    return color

# def plate_with_stroke(pos = (0, 0), size, fill_color, stroke_color = "white", stroke_width):
#     return sign.rect(pos, size, a, b, fill_opacity = 0.0, stroke = stroke_color, stroke_width = stroke_width)

# Feature to select file
# FIXME


# Parse file and return XML tree
def parse_file(filename):
    try:
        with open(filename, "r") as input_file:
            tree = Et.parse(input_file)
            root = tree.getroot()
            return root
    except Exception as error:
        print(error)
        return None


#        for child in root.iter():
#            print(child.tag, child.attrib)

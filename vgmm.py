import xml.etree.ElementTree as Et
import svgwrite
#import sign as sign


def vgmm(argv):
    # Argument checking
    if len(argv) != 3:
        return -1

    # Save arguments
    input_filename = argv[1]
    output_filename = argv[2]

    # Parse input file from XML
    root = parse_file(input_filename)

    # Traverse XML tree and make appropriate calls to SVG library
    if root is not None:
        sign_assembly = make_sign(root)
        # sign_assembly = sign.make_sign(root)
        sign_assembly.save(indent = True, pretty = True)

    # Produce an SVG file (write to file)
    # try:
    #     write_sign(sign_assembly, output_file_name)
    # except Exception as error:
    #     print(error)


def make_sign(root):
    #print(root.iter())
    sign = svgwrite.Drawing("out.svg", profile = "full")

    for node in root.iter():
        if node.tag == "sign":
            process_sign(sign, node)
        if node.tag == "ystack":
            sign.add(process_ystack(node))
        elif node.tag == "xstack":
            sign.add(process_xstack(node))
        elif node.tag == "text":
            sign.add(process_text(node))
        elif node.tag == "arrow":
            sign.add(process_arrow(node))

    # sign.add(sign.rect((0, 0), (300, 75), fill = "#00755c"))
    # sign.add(sign.rect((1.5, 1.5), (300, 75), 8, 8, fill_opacity = 0.0, stroke = "white", stroke_width = 3))

    return sign

def process_sign(sign, node):


# def plate_with_stroke(pos = (0, 0), size, fill_color, stroke_color = "white", stroke_width):
#
#     return sign.rect(pos, size, a, b, fill_opacity = 0.0, stroke = stroke_color, stroke_width = stroke_width)

# Feature to select file
# FIXME

# Help function (print help info)
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

# Write sign to disk
def write_sign(sign, filename):
    try:
        with open(filename, "w", encoding="utf-8") as output_file:
            output_file.write(sign)
    except Exception as error:
        print(error)

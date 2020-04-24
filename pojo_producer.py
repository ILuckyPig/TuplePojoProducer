import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", dest="name", required=True, help="class name, e.g. '-c User'")
parser.add_argument("-p", action="append", dest="properties", required=True, help="class properties, e.g. '-p "
                                                                                  "\"Long uid\" -p \"String name\"'")
args = parser.parse_args()

class_name = args.name
properties = args.properties
with open(class_name + ".java", "w") as file:
    line = " extends Tuple" + str(len(properties)) + "<"
    for property in enumerate(properties):
        line = line + str(property[1].split()[0]) + ", "
    line = line[:-2] + ">"
    file.write("public class " + class_name + line + " {\n")
    for property in properties:
        file.write("    private " + property + ";\n")
    file.write("\n")
    for property in enumerate(properties):
        type = property[1].split()[0]
        property_name = property[1].split()[1]
        method_name = "%s%s" % (property_name[0].upper(), property_name[1:])
        file.write("    public " + type + " get" + method_name + "() {\n")
        file.write("        return this.f" + str(property[0]) + ";\n")
        file.write("    }\n\n")

        file.write("    public void set" + method_name + "(" + type + " " + property_name + ") {\n")
        file.write("        this.f" + str(property[0]) + " = " + property_name + ";\n")
        file.write("    }\n\n")
    file.write("}")

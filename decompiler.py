import methods
import fields


def decompile(file):
    with open(file, "r") as f:
        print('Decompiling file', file)
        lines = f.read()
        for i in range(len(methods.dict)):
            lines = lines.replace(methods.dict[i][0], methods.dict[i][1])
        for i in range(len(fields.dict)):
            lines = lines.replace(fields.dict[i][0], fields.dict[i][1])
    with open(file, "w") as f:
        f.write(lines)

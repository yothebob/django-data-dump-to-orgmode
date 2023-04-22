import json

import_file = "test.json"
file_title = "test"
file_titles = []

output_file_data = ""
output_file = "output.org"

lookout_fks = ["participant"]

with open(import_file, "r") as f:
    output_file_data += """#+TITLE: {0}
#+INFOJS_OPT: view:info
#+SETUPFILE: https://fniessen.github.io/org-html-themes/org/theme-readtheorg.setup

""".format(file_title)
    file_json = json.load(f)
    for item in file_json:
        if item["model"] not in file_titles:
            file_titles.append(item["model"])

    for title in file_titles:
        output_file_data += """\n* {0}""".format(title)
        for item in file_json:
            obj_data = {}
            if item["model"] == title:
                output_file_data += """\n** {0}""".format(item["pk"])
                output_file_data += """\n<<{0}-{1}>>""".format(item["model"].split(".")[-1],item["pk"])
                output_file_data += """\n |Field | Value|"""
                output_file_data += """\n |-|"""
                for field, value in item["fields"].items():
                    if field in lookout_fks and value != None:
                        output_file_data += """\n |{0} | {1}|""".format(field, f"[[{field}-{value}]]")
                    else:
                        output_file_data += """\n |{0} | {1}|""".format(field, value)
with open(output_file, "w") as opf:
    opf.write(output_file_data)

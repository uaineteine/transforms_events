import os

from uainepydat import fileio
from uainepydat import datatransform


main_package_name = "events"  # Your main package name
relative_directory = "../" + main_package_name  # Your source code root
absolute_directory = os.path.abspath(relative_directory)

# --- Update pre-compile index.rst_pre ---
pre_compile_path = "source/index.rst_pre"
pre_str = fileio.read_file_to_string(pre_compile_path)

# --- Dependencies ---
requirements_path = "../requirements.txt"
requirements = fileio.read_file_to_string(requirements_path)
requirements = datatransform.break_into_lines(requirements)
requirements = list(map(lambda string: datatransform.add_prefix(string, "* "), requirements))
requirements.append("\n")
post_str = datatransform.replace_between_tags(pre_str, "dependencies", requirements, deleteTags=True)

# --- Purpose ---
purpose_path = "../meta/purpose.txt"
pur = fileio.read_file_to_string(purpose_path)
pur = datatransform.break_into_lines(pur)
post_str = datatransform.replace_between_tags(post_str, "purpose", pur, deleteTags=True)

# --- Changelog ---
changelog_path = "../meta/changelog.txt"
chlog = fileio.read_file_to_string(changelog_path)
chlog = datatransform.break_into_lines(chlog)
post_str = datatransform.replace_between_tags(post_str, "changelog", chlog, deleteTags=True)

# --- Optional description ---
description_path = "../meta/description.txt"
if os.path.exists(description_path):
    description_content = fileio.read_file_to_string(description_path)
    description_content = datatransform.break_into_lines(description_content)
    post_str = datatransform.replace_between_tags(post_str, "description", description_content, deleteTags=True)
else:
    print(f"Warning: {description_path} does not exist. Skipping description replacement.")

# --- Write out final index.rst ---
post_compile_path = "source/index.rst"
with open(post_compile_path, "w", encoding="utf-8") as text_file:
    text_file.write(post_str)

print("Updated rst file and subfolder pages.")

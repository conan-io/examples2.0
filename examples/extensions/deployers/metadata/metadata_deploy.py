import os
import shutil


def deploy(graph, output_folder, **kwargs):
    # Note the kwargs argument is mandatory to be robust against future changes.
    conanfile = graph.root.conanfile
    for name, dep in conanfile.dependencies.items():
        shutil.copytree(dep.package_metadata_folder,
                        os.path.join(output_folder, "dependencies_metadata", "packages", dep.ref.name, dep.pref.package_id))
        shutil.copytree(dep.recipe_metadata_folder,
                        os.path.join(output_folder, "dependencies_metadata", "recipes", dep.ref.name))

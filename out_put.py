
# handles output
# data in the form of list of 'directive'
# directive is [project <object>,assignments <list>]
# assignment is [contrib <object>,skill <string>]

from data_types import project, contributor, skill


def order_based_on_skill(assignments: list, proj_req: list) -> list:
    result = []
    for req in proj_req:
        temp = [x[0].name for x in assignments if x[1] == req.name]
        result += temp

    return result
        

def write(data, filename):

    content = ''
    content += f"{str(len(data))}\n"

    for directive in data:
        project, assignments = directive
        
        # Project name
        content += f"{project.name}\n"

        contribs_ordered = " ".join(order_based_on_skill(assignments, project.roles))
        content += f"{contribs_ordered}\n"

    with open(filename, 'w') as output_file:
        output_file.write(content)

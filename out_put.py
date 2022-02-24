
#handles output



#input in the form of list of 'directive'
# directive is [project <object>,assignments <list>]
# assignment is [contrib <object>,skill <string>]


def write(input,filename):

    for directive in input:
        project,assignments = directive

        for assignment in assignments:
            contrib,skill = assignment

    with open(filename,'w') as output_file:
        pass

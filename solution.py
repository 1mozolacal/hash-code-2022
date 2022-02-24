from msilib.schema import Directory
from data_types import  contributor, project






def solve(input):
    contrib = input['contribs']
    pro = input['projects']

    directives = []

    project_order_by_due_date = sorted(pro, key=lambda x: x.get_due_date())

    for current_pro in project_order_by_due_date:
        current_assignments = [] # (contrib,skill)
        # get roles: list of tuple(skill,level)
        roles = current_pro.get_roles()
        for role in roles:
            currently_working = [p for p,skil in current_assignments]
            peoples_skills = [p for p in contrib if not p in currently_working]








def main():
    directory = 'inputFiles/'
    test_cases = ['a_an_example.in.txt','b_better_start_small.in.txt','c_collaboration.in.txt','d_dense_schedule.in.txt','e_exceptional_skills.in.txt','f_find_great_mentors.in.txt']
    for test in test_cases:
        pass
        # input = input(directory+test)
        # soltuion = sovle(input)
        # write(solution,"SUB-"test)

if __name__ == '__main__':
    main()
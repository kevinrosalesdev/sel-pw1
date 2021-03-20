def format_rules(rules, print_rules=False):
    str_rules = ""
    for idx, rule in enumerate(rules, 1):
        str_rules += f"R{idx}: IF "
        for condition in rule[0]:
            str_rules += f"{condition[0]} = '{condition[1]}' AND "
        str_rules = str_rules[:-4]
        str_rules += f"-> {rule[1][0]} = '{rule[1][1]}'\n"

    if print_rules:
        print(str_rules)

    return str_rules


def write_rules(rules):
    f = open('Out/rules.out', 'w')
    f.write(rules)
    f.close()

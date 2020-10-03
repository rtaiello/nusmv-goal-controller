#!/usr/bin/env python3

import io

from tqdm import tqdm

import src.my_lib.utils as u

GOOD_ENTRY = 1
BAD_ENTRY = 0


class Controller:

    def __init__(self, M):
        self.n, self.m = M.data.n, M.data.m
        entry_init = M.data.entry
        self.goal = M.data.goal
        self.entries = set()
        set_path = set()
        moves_dictionary = io.StringIO()
        moves_dictionary.write("MOVES = {\n")

        for i in tqdm(range(self.n)):
            for j in tqdm(range(self.m)):
                if (i, j) in self.entries:
                    continue
                try:
                    M.set_entry((i, j))
                    M.regenerate()
                    res = u.launch_nusmv()
                    plan = u.get_path(res)
                    current_path_list = (u.get_path(res))
                    update_path_list = check_exist(current_path_list, set_path)
                    set_path.update(update_path_list)
                    from_list_to_dictinary(update_path_list, moves_dictionary)
                    if plan is not None:
                        self.entries.update(plan)
                except Exception as e:
                    continue

        M.set_entry(entry_init)
        moves_dictionary.write("}\n")
        with open("./moves_dictionary.py", 'w') as file_desciptor:
            file_desciptor.write(moves_dictionary.getvalue())

def from_list_to_dictinary(path_list: list, sb):
    if len(path_list) >= 2:
        local_cell = path_list.pop(0)
        next_move = path_list[0]
        sb.writelines(" {}: {},\n".format(str(local_cell), str(next_move)))
        from_list_to_dictinary(path_list, sb)


def check_exist(path_list: list, tmp: set):
    result = []
    visited = False
    i = 0
    while i < len(path_list) and not visited:
        visited = path_list[i] in tmp
        if not visited:
            result.append(path_list[i])
            i = i + 1
        else:
            result.append(path_list[i])
            i = len(path_list)
    return result

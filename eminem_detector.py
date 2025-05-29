# -*- encoding: utf-8 -*-
"""
The project was created on May 28, 2025
by @Temn1yKot
the project was created for fun
"""
import inspect
import os

def get_importing_file():
    stack = inspect.stack()
    try:
        for frame_info in reversed(stack):
            frame = frame_info.frame
            filename = frame.f_code.co_filename

            if (not filename.startswith('<')
                and os.path.exists(filename)
                and not os.path.samefile(filename, __file__)):
                return os.path.abspath(filename)
    finally:
        del stack
    return None

file = get_importing_file()

songs = 'not alike', 'without me', 'the real slim shady', 'killshot', 'killer', 'we made you', 'kill you', 'just lose it', '3am', '3 am', '3 a.m.', '3a.m.', 'berzerk', 'offended', 'guilty conscience', 'rap god', 'the ringer'
bad_words = 'niger', 'nigga', 'nigger', 'niggers', 'niggas', 'nigas'

def activate():
    with open(file) as file_:
        file_ = file_.read()
        code = ''
        for i in file_.split('\n'):
            if 'eminem' in i.lower() and not 'import eminem_detector' in i.strip().lower() and not 'eminem_detector.activate()' in i.strip().lower():
                exit(f'''\tFile "{file}", line {len(code.split('\n'))}\n{i.strip()}\n{'~' * int(len(i.strip().lower().split('eminem')[0])) + '^' * len("Eminem") + '~' * int(len(i.strip().lower().split('eminem')[1]))}\nFlowError: Eminem has very big and strong flow, it is against your code running''')
            elif any(s in i.lower() for s in songs):
                s_found = next(s for s in songs if s in i.lower())
                exit(f'''\tFile "{file}", line {len(code.split('\n'))}\n{i.strip()}\n{'~' * len(i.strip().lower().split(s_found)[0]) + '^' * len(s_found) + '~' * len(i.strip().lower().split(s_found)[1])}\nFlowError: Too many very strong flow''')
            elif "mgk" in i.lower():
                exit(f'''\tFile "{file}", line {len(code.split('\n'))}\n{i.strip()}\n{'~' * int(len(i.strip().lower().split('mgk')[0])) + '^' * len("mgk") + '~' * int(len(i.strip().lower().split('mgk')[1]))}\nFlowError: Python is against code being run with the world's worst rapper''')
            elif any(s in i.lower() for s in bad_words):
                s_found = next(s for s in bad_words if s in i.lower())
                exit(f'''\tFile "{file}", line {len(code.split('\n'))}\n{i.strip()}\n{'~' * len(i.strip().lower().split(s_found)[0]) + '^' * len(s_found) + '~' * len(i.strip().lower().split(s_found)[1])}\nCondemnError: Python is against such words and condemns them, so it will not let your code run.''')
            else:
                code += i + "\n"
                try:
                    exec(code)
                except KeyboardInterrupt:
                    exit(0)
                except:
                    continue

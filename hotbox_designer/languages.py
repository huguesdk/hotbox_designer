def execute_code(language, code):
    return EXECUTORS[language](code)


def execute_python(code):
    exec(code)


def execute_mel(code):
    from maya import mel
    mel.eval(code.replace(u'\u2029', '\n'))


EXECUTORS = {
    'mel': execute_mel,
    'python': execute_python
}

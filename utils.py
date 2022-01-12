from subprocess import PIPE, run


def cmd(command, **kwargs):
    r = run(
        command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True, **kwargs
    )
    print(r.args)
    if r.returncode != 0:
        print(f"ERROR {r.returncode}")
    print(r.stdout.strip())
    print(r.stderr.strip(), end="")
    return r


def fetchall_dict(con, *args):
    return [dict(r) for r in con.execute(*args).fetchall()]


def singleColumnToList(array_of_half_tuplets, column_name=1):
    return list(
        map(
            lambda x: x[column_name],
            array_of_half_tuplets,
        )
    )

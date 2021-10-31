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

import yappi
from commands import *

yappi.start

t = Threading()

def work():
    out = Console.get_output("figlet hello world")
    print(out)


for i in Int.from_to(1, 10):
    t.add(work)

t.start(wait_for_keyboard_interrupt=True)

print("done threads")

for thread in t.finished_threads:
    thread = thread.thread
    print(
        "Function stats for (%s) (%d)" % (thread.name, thread.ident)
    )  # it is the Thread.__class__.__name__
    yappi.get_func_stats(ctx_id=thread.ident).print_all()

print("done yappy")

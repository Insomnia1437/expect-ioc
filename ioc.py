import pexpect
import sys


command = "/home/sdcswd/epics/R7.0.8/base/bin/linux-x86_64/softIocPVA st.cmd"
arg = "st.cmd"
ioc_ps1 = "epics>"


def communicate(child, cmd):
    child.sendline(cmd)
    child.expect(ioc_ps1)
    return f"before:\n{child.before.decode('utf-8')}\nafter:\n{child.after.decode('utf-8')}"


ioc = pexpect.spawn(command)
# ioc.logfile = sys.stdout.buffer
ioc.expect(ioc_ps1)
print(f"before:\n{ioc.before.decode('utf-8')}\nafter:\n{ioc.after.decode('utf-8')}")
print(communicate(ioc, "dbl"))
print(communicate(ioc, "help"))

#HQ9#---Better version of HQ9+
"""
Here is all the commands:
H - hello world
Q - print source code
9 - 99 bottles of beer
+ - add 1 to invisible variable
That is not all
# - multiply invisible variable by 2
P - print PANCAKES
M - print linux kernel part
W - wrong number song
C - print Hello world source code on C
B - print BarBarBarBarBar
R - End program
WARNING:
UPPERCASE Or lowercase MATTERS: ONE LETTER COMMANDS ARE UPPERCASE
"""
#Variables
bottle = 99
lines = []
invis = 0
number = 0
#Defines
def H():
    print("Hello, world!")
def Q():
    global lines
    print("\n".join(lines))
def NINE():
    global bottle
    for ib in range(99):
        print(f"{bottle} bottles of beer\nyou take one down, pass it around,")
        bottle -= 1
        if bottle >= 1:
            print(f"{bottle} bottles of beer on the wall.\n")
        else:
            print("no more bottles of beer on the wall.\n")
    bottle = 99
def PLUS():
    global invis
    invis += 1
def SHARP():
    global invis
    invis *= 2
def P():
    print("PANCAKES")
def M():
    print("""static int __init setup_proxy_exec(char *str)
{
	bool proxy_enable = true;

	if (*str && kstrtobool(str + 1, &proxy_enable)) {
		pr_warn("Unable to parse sched_proxy_exec=\n");
		return 0;
	}

	if (proxy_enable) {
		pr_info("sched_proxy_exec enabled via boot arg\n");
		static_branch_enable(&__sched_proxy_exec);
	} else {
		pr_info("sched_proxy_exec disabled via boot arg\n");
		static_branch_disable(&__sched_proxy_exec);
	}
	return 1;
}
#else
static int __init setup_proxy_exec(char *str)
{
	pr_warn("CONFIG_SCHED_PROXY_EXEC=n, so it cannot be enabled or disabled at boot time\n");
	return 0;
}
#endif
__setup("sched_proxy_exec", setup_proxy_exec);

/*
 * Debugging: various feature bits
 *
 * If SCHED_DEBUG is disabled, each compilation unit has its own copy of
 * sysctl_sched_features, defined in sched.h, to allow constants propagation
 * at compile time and compiler optimization based on features default.
 */
#define SCHED_FEAT(name, enabled)	\
	(1UL << __SCHED_FEAT_##name) * enabled |
__read_mostly unsigned int sysctl_sched_features =
#include "features.h"
	0;
#undef SCHED_FEAT

/*
 * Print a warning if need_resched is set for the given duration (if
 * LATENCY_WARN is enabled).
 *
 * If sysctl_resched_latency_warn_once is set, only one warning will be shown
 * per boot.
 */
__read_mostly int sysctl_resched_latency_warn_ms = 100;
__read_mostly int sysctl_resched_latency_warn_once = 1;

/*
 * Number of tasks to iterate in a single balance run.
 * Limited because this is done with IRQs disabled.
 */
__read_mostly unsigned int sysctl_sched_nr_migrate = SCHED_NR_MIGRATE_BREAK;

__read_mostly int scheduler_running;

#ifdef CONFIG_SCHED_CORE

DEFINE_STATIC_KEY_FALSE(__sched_core_enabled);

/* kernel prio, less is more */
static inline int __task_prio(const struct task_struct *p)
{
	if (p->sched_class == &stop_sched_class) /* trumps deadline */
		return -2;

	if (p->dl_server)
		return -1; /* deadline */

	if (rt_or_dl_prio(p->prio))
		return p->prio; /* [-1, 99] */

	if (p->sched_class == &idle_sched_class)
		return MAX_RT_PRIO + NICE_WIDTH; /* 140 */

	if (task_on_scx(p))
		return MAX_RT_PRIO + MAX_NICE + 1; /* 120, squash ext */

	return MAX_RT_PRIO + MAX_NICE; /* 119, squash fair */
}
""")
def W():
    print("Oh it's the wrong number\nThe wrong number song!\nWe are very very sorry that we got it wrong!")
def C():
    print("""#include <stdio.h>
int main() {
    printf("Hello, world!");
    return 0;
}""")
def B():
    print("Bar" * 5)
#TODO: 1. rm -rf 2. See how my WSL burns
#MAIN LOOOOOOOOOOOOOOOOOOOP
def ENTER():
    global lines, number, bottle, invis
    while True:
        lines = []
        number = 0
        while True:
            number += 1
            cmd = input(f"{number}. ").upper()
            if "R" in cmd:
                break
            lines.append(cmd)
        for line in lines:
            for ch in line:
                if ch == "H":
                    H()
                elif ch =="Q" :
                    Q()
                elif ch == "9":
                    NINE()
                elif ch == "+":
                    PLUS()
                elif ch == "#":
                    SHARP()
                elif ch == "P":
                    P()
                elif ch == "M":
                    M()
                elif ch == "W":
                    W()
                elif ch == "C":
                    C()
                elif ch == "B":
                    B()
                else:
                    pass
ENTER()
#Aw, that .join() thing is useful a lot
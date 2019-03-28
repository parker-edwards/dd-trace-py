GC_GEN1_COUNT = 'gc_gen1_count'
GC_GEN2_COUNT = 'gc_gen2_count'
GC_GEN3_COUNT = 'gc_gen3_count'

THREAD_COUNT = 'thread_count'
MEM_RSS = 'mem.rss'
CTX_SWITCH_VOLUNTARY = 'ctx_switch.voluntary'
CTX_SWITCH_INVOLUNTARY = 'ctx_switch.involuntary'
CPU_TIME_SYS = 'cpu.time.sys'
CPU_TIME_USER = 'cpu.time.user'
CPU_PERCENT = 'cpu.percent'

GC_RUNTIME_METRICS = set([
    GC_GEN1_COUNT,
    GC_GEN2_COUNT,
    GC_GEN3_COUNT,
])

PSUTIL_RUNTIME_METRICS = set([
    THREAD_COUNT,
    MEM_RSS,
    CTX_SWITCH_VOLUNTARY,
    CTX_SWITCH_INVOLUNTARY,
    CPU_TIME_SYS,
    CPU_TIME_USER,
    CPU_PERCENT,
])

DEFAULT_RUNTIME_METRICS = GC_RUNTIME_METRICS | PSUTIL_RUNTIME_METRICS

RUNTIME_ID = 'runtime-id'
SERVICE = 'service'
LANG_INTERPRETER = 'lang_interpreter'
LANG_VERSION = 'lang_version'

TRACER_TAGS = set([
    RUNTIME_ID,
    SERVICE,
])

PLATFORM_TAGS = set([
    LANG_INTERPRETER,
    LANG_VERSION
])

DEFAULT_RUNTIME_TAGS = TRACER_TAGS | PLATFORM_TAGS

DD_METRIC_PREFIX = 'runtime.python'

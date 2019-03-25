import os

from .collector import ValueCollector


class RuntimeMetricCollector(ValueCollector):
    value = {}


class GCRuntimeMetricCollector(RuntimeMetricCollector):
    """
    """
    required_modules = ['gc']
    periodic = True

    def collect_fn(self, keys):
        """Returns the gc count of the collections of the first 3 generations.
        More information:
            - https://docs.python.org/3/library/gc.html

        Metrics collected are:
        - gc.gen1_count
        - gc.gen2_count
        - gc.gen3_count
        """
        gc = self.modules.get('gc')
        metrics = {}

        # DEV: shortcut if none of the keys are required.
        if not len(set([
            'gc.gen1_count',
            'gc.gen2_count',
            'gc.gen3_count',
        ]).intersection(keys)):
            return {}

        count = gc.get_count()
        if 'gc.gen1_count' in keys:
            metrics['gc.gen1_count'] = count[0]
        if 'gc.gen2_count' in keys:
            metrics['gc.gen2_count'] = count[1]
        if 'gc.gen3_count' in keys:
            metrics['gc.gen3_count'] = count[2]

        return metrics


class PSUtilRuntimeMetricCollector(RuntimeMetricCollector):
    """Collector for psutil metrics.

    Performs batched operations via proc.oneshot() to optimize the calls.
    See https://psutil.readthedocs.io/en/latest/#psutil.Process.oneshot
    for more information.

    Metrics supported are:
    - thread_count
    - mem.rss
    """
    required_modules = ['psutil']
    periodic = True

    def _on_modules_load(self):
        self.proc = self.modules['psutil'].Process(os.getpid())

    def collect_fn(self, keys):
        metrics = {}
        with self.proc.oneshot():
            if 'thread_count' in keys:
                metrics['thread_count'] = self.proc.num_threads()

            if 'mem.rss' in keys:
                metrics['mem.rss'] = self.proc.memory_info().rss

            if 'ctx_switch.voluntary' in keys:
                metrics['ctx_switch.voluntary'] = self.proc.num_ctx_switches().voluntary
            if 'ctx_switch.involuntary' in keys:
                metrics['ctx_switch.involuntary'] = self.proc.num_ctx_switches().involuntary

            if 'cpu.time.sys' in keys:
                metrics['cpu.time.sys'] = self.proc.cpu_times().user
            if 'cpu.time.user' in keys:
                metrics['cpu.time.user'] = self.proc.cpu_times().system
            if 'cpu.percent' in keys:
                metrics['cpu.percent'] = self.proc.cpu_percent()
        return metrics

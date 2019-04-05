from ddtrace.internal.runtime.runtime_metrics import (
    RuntimeTags,
    RuntimeMetrics,
    RuntimeWorker,
)
from ddtrace.internal.runtime.constants import (
    DEFAULT_RUNTIME_METRICS,
    DEFAULT_RUNTIME_TAGS,
    GC_GEN0_COUNT,
    RUNTIME_ID,
)
from ...base import (
    BaseTestCase,
    BaseTracerTestCase,
)


class TestRuntimeTags(BaseTracerTestCase):
    def test_all_tags(self):
        with self.override_global_tracer():
            with self.trace('test', service='test'):
                tags = set([k for (k, v) in RuntimeTags()])
                self.assertSetEqual(tags, DEFAULT_RUNTIME_TAGS)

    def test_one_tag(self):
        with self.override_global_tracer():
            with self.trace('test', service='test'):
                tags = [k for (k, v) in RuntimeTags(enabled=[RUNTIME_ID])]
                self.assertEqual(tags, [RUNTIME_ID])


class TestRuntimeMetrics(BaseTestCase):
    def test_all_metrics(self):
        metrics = set([k for (k, v) in RuntimeMetrics()])
        self.assertSetEqual(metrics, DEFAULT_RUNTIME_METRICS)

    def test_one_metric(self):
        metrics = [k for (k, v) in RuntimeMetrics(enabled=[GC_GEN0_COUNT])]
        self.assertEqual(metrics, [GC_GEN0_COUNT])


class TestRuntimeWorker(BaseTracerTestCase):
    def setUp(self):
        super(TestRuntimeWorker, self).setUp()
        self.worker = RuntimeWorker(self.tracer.dogstatsd)

    def test_worker_start_stop(self):
        self.worker.start()
        self.worker.stop()

    def test_worker_flush(self):
        self.worker.start()
        self.worker.flush()
        self.worker.stop()

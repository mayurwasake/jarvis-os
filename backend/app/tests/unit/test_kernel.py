from app.kernel import Kernel
from app.kernel import KernelState


def test_kernel_initial_state():

    kernel = Kernel()

    assert kernel.state == KernelState.CREATED


def test_kernel_boot():

    kernel = Kernel()

    kernel.boot()

    assert kernel.state == KernelState.RUNNING

    assert kernel.is_running()


def test_kernel_shutdown():

    kernel = Kernel()

    kernel.boot()

    kernel.shutdown()

    assert kernel.state == KernelState.STOPPED


def test_status():

    kernel = Kernel()

    kernel.boot()

    status = kernel.status()

    assert status["state"] == "RUNNING"

    assert status["registered_services"] == 2
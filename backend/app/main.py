from app.kernel import Kernel
from app.logging_system import logger


def main():

    logger.info("=" * 60)

    logger.info("🚀 Booting JARVIS OS")

    logger.info("=" * 60)

    kernel = Kernel()

    kernel.boot()

    logger.info("JARVIS OS is Operational.")

    print()

    print(kernel.status())


if __name__ == "__main__":
    main()
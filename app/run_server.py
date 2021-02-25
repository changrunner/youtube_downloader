from zeppos_api.run_server_base import RunServerBase
from zeppos_logging.app_logger import AppLogger


class RunServer(RunServerBase):
    def __init__(self):
        super().__init__(current_module_filename=__file__)

    def run_server(self):
        if super().start_app():
            pass


if __name__ == '__main__':
    RunServerBase.main_basic_logging(logger_name="youtube_downloader",
                                     current_module_filename=__file__)
    AppLogger.logger.debug("Entering __main__")
    RunServer().run_server()
    # main(sys.argv[1:])

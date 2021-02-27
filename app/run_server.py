from zeppos_api.run_server_base import RunServerBase
from zeppos_logging.app_logger import AppLogger
from flask import Flask
from flask_restful import Api
from waitress import serve
from paste.translogger import TransLogger


class RunServer(RunServerBase):
    def __init__(self):
        super().__init__(current_module_filename=__file__)

    def run_server(self):
        if super().start_app():
            LISTEN = f"127.0.0.1:{8080}"
            serve(TransLogger(application=App.create_app_instance([HeartBeat]),
                              logger=AppLogger.logger,
                              setup_console_handler=True)
                  , listen=LISTEN)

class App:
    def create_app(self, class_object_list):
        AppLogger.logger.info("creating app")
        flask_app = Flask(__name__)
        api = Api(flask_app)
        for class_object in class_object_list:
            class_object.add_routes(api)

        return flask_app

    @staticmethod
    def create_app_instance(class_object_list):
        AppLogger.logger.info("Create App Instance")
        return App().create_app(class_object_list)


if __name__ == '__main__':
    RunServerBase.main_basic_logging(logger_name="youtube_downloader",
                                     current_module_filename=__file__)
    AppLogger.logger.debug("Entering __main__")
    RunServer().run_server()
    # main(sys.argv[1:])
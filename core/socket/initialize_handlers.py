from matrx_utils.socket.core.service_factory import ServiceFactory


def initialize_socketio_handlers():
    service_factory = ServiceFactory()
    service_factory.register_default_services()

    import core.socket.global_socket_events
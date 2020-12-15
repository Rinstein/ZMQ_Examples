import threading

import sys
import time
import zmq

def start_handle_and_sending_data(id: str):
    # 往队列中扔数据 作为生产者
    context = zmq.Context()
    # Socket to send messages to
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5558")

    # Process tasks forever
    for i in range(3):
        # Simple progress indicator for the viewer
        sys.stdout.write(id)
        sys.stdout.flush()

        # Do the work
        time.sleep(int(10) * 0.001)

        # Send results to sink
        # sender.send(b'')
        sender.send_string(id)


if __name__ == "__main__":
    # 开启3个线程，同时发数据到队列
    for i in range(3):
        t = threading.Thread(target=start_handle_and_sending_data, args=(str(i),))
        t.start()

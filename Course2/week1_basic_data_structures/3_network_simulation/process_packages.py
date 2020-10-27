# python3

from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.packet_que = deque()
        self.time = 0

    def process(self, request):
        while self.packet_que and self.packet_que[-1].time_to_process == 0: #if it takes no time to process packet, then process and move on.
            self.packet_que.pop()
        while self.packet_que and self.packet_que[-1].arrived_at < request.arrived_at:
            popped = self.packet_que.pop()
            self.time += popped.time_to_process
        if len(self.packet_que) < self.size:# if length of deque is less than size, there is space
            self.packet_que.appendleft(request)
            return Response(False, self.time)  
        else: #if there is no space, the packet is dropped
            return Response(True, -1)    

        # if len(self.packet_que) < self.size:# if length of deque is less than size, there is space
        #     self.packet_que.appendleft(request)
        # else: #if there is no space, the packet is dropped
        #     return Response(True, -1)
        # while self.packet_que and self.packet_que[-1].time_to_process == 0: #if it takes no time to process packet, then process and move on.
        #     self.packet_que.pop()
        # while self.packet_que and self.packet_que[-1].arrived_at <= request.arrived_at:
        #     popped = self.packet_que.pop()
        #     processtime = popped.arrived_at
        #     self.time += popped.time_to_process
        # if processtime != undefined:
        #     return Response(False, processtime)
        # else:
        #     return Response(False, self.time)

        # # if self.packet_que: #not empty
        # #     while self.packet_que and (self.packet_que[-1].arrived_at <= request.arrived_at or self.packet_que[-1].time_to_process == 0):
        # #         popped = self.packet_que.pop() # this is where you will check if the incoming packet time is greater than the time of packets in que. If so, deque the packet
        # #         self.time = popped.time_to_process
        # if len(self.packet_que) <= self.size: # if length of deque is less than size, there is space
        #     if self.packet_que: #not empty
        #         while self.packet_que and (self.packet_que[-1].arrived_at <= request.arrived_at or self.packet_que[-1].time_to_process == 0):
        #             popped = self.packet_que.pop() # this is where you will check if the incoming packet time is greater than the time of packets in que. If so, deque the packet
        #             self.time = popped.time_to_process
        #     self.packet_que.appendleft(request) 
        #     return Response(False, self.time)
        # else: #if there is no space, the packet is dropped
        #     return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()

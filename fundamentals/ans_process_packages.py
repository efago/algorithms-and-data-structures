# python3

class Queue:
    def __init__( self, size):
        self.queue= []
        self.size= size
    def pop( self):
        if len( self.queue) > 0:
            self.queue.pop( 0)
        else:
            print( 'Queue empty')
    def push( self, request):
        if len( self.queue) < self.size:
            self.queue.append( request)
            return True
        else:
            return False

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request, queue):
        # write your code here
        start_time= 0 if len( self.finish_time_) == 0 else self.finish_time_[ -1]
        for req in queue.queue:
            if start_time >= ( req.arrival_time + req.process_time):
                queue.pop()
            else:
                break

        success= queue.push( request)
        if success:
                completion_time= start_time + request.process_time
                self.finish_time_.append( completion_time)
                return Response( False, start_time)
        else:
                return Response( True, -1)

        return Response(False, -1)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    queue= Queue( buffer.size)
    for request in requests:
        responses.append(buffer.Process(request, queue))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)

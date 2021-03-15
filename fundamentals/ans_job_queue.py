# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        self.assigned_workers = []
        self.start_times = []

        self.job_heap= [ 0] * self.num_workers
        self.worker_pos= [ i for i in range( self.num_workers)]
        self.time= 0
        for job in self.jobs:
            if self.job_heap[ 0] > self.time:
                self.time= self.job_heap[ 0]
            self.start_times.append( self.time)
            self.insert_job( self.time + job)

    def insert_job( self, end_time):
        self.job_heap[ 0]= end_time
        self.assigned_workers.append( self.worker_pos[ 0])

        self.job_heap[ -1], self.job_heap[ 0]= self.job_heap[ 0], self.job_heap[ -1]
        self.worker_pos[ -1], self.worker_pos[ 0]= self.worker_pos[ 0], self.worker_pos[ -1]
        self.sift_down( 0)

    def sift_down( self, i):
        size= len( self.job_heap)
        left_idx= i * 2 + 1
        right_idx= ( i + 1) * 2
        min_idx= i
        if ( left_idx < size) and \
            (( self.job_heap[ left_idx] < self.job_heap[ min_idx]) or \
                ( ( self.job_heap[ left_idx] == self.job_heap[ min_idx]) and \
                    ( self.worker_pos[ left_idx] < self.worker_pos[ min_idx]))):
            min_idx= left_idx
        if ( right_idx < size) and \
            (( self.job_heap[ right_idx] < self.job_heap[ min_idx]) or \
                ( ( self.job_heap[ right_idx] == self.job_heap[ min_idx]) and \
                    ( self.worker_pos[ right_idx] < self.worker_pos[ min_idx]))):
            min_idx= right_idx
        if min_idx != i:
            self.job_heap[ i], self.job_heap[ min_idx]= self.job_heap[ min_idx], self.job_heap[ i]
            self.worker_pos[ i], self.worker_pos[ min_idx]= self.worker_pos[ min_idx], self.worker_pos[ i]            
            self.sift_down( min_idx)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

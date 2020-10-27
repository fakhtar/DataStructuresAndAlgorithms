# python3

from collections import namedtuple
from collections import deque
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    len_jobs = len(jobs)
    result = []
    jobs = deque(jobs)
    myheap = []
    for i in range(0,n_workers):
        myheap.append((0,i))
    heapq.heapify(myheap)
    # job = jobs.popleft()
    # heapq.heappop(heap)
    # heapq.heappush(heap, item)
    for i in range(0,len_jobs):
        job = jobs.popleft()
        worker = heapq.heappop(myheap)
        result.append(AssignedJob(worker[1], worker[0]))
        new_worker = (worker[0] + job,worker[1])
        heapq.heappush(myheap, new_worker)
    # print(myheap)
    # next_free_time = [0] * n_workers
    # for job in jobs:
    #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #     next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()

"""
A server has n customers waiting to be served. The service time required by each
customer is known in advance, 𝒕_𝒊 minutes for customer 𝒊.
So if, e.g., customers are served in order of increasing i,
then the i-th customer has to wait ∑2_(𝒋=𝟏)^𝒊▒𝒕_𝒋 minutes
"""
def minWaitTime(wait_times):
    """
    Sort by 𝒕_𝒊 and pick customers in increasing order of 𝒕_𝒊
    Greedily select the customer with lowest wait time first
    """
    n = len(wait_times)
    wait_times_sorted = sorted(zip(wait_times, range(n)))
    total = 0
    order = [0] * n

    for ii, (t, i) in enumerate(wait_times_sorted):
        order[ii] = i
        total += (n-1-ii) * t

    return order, total

order, total = minWaitTime([5,4,6,2,7,2])
print('order=', order) # order= [3, 5, 1, 0, 2, 4]
print('total=', total) # total= 46
import matching
import timeit

start = timeit.default_timer()

applicants = [
    [1, 4, 3, 1, 2],
    [2, 2, 1, 3, 4],
    [3, 1, 3, 4, 2],
    [4, 4, 3, 1, 2]]

apartments = [
    [1, 3, 2, 4, 1],
    [2, 2, 3, 1, 4],
    [3, 3, 1, 2, 4],
    [4, 3, 2, 4, 1]]

matcher = matching.Matcher()

for applicant in applicants:
    matcher.input_applicant(applicant)
for apartment in apartments:
    matcher.input_apartment(apartment)

print(matcher.match())
matcher.print_result()

stop = timeit.default_timer()
#print('Time: ', stop - start)
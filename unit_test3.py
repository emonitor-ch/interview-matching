import matching
import timeit

start = timeit.default_timer()

#Your statements here

applicants =[
    [1, 4, 5, 3, 7, 2, 6, 1],
    [2, 5, 6, 4, 7, 3, 2, 1],
    [3, 1, 6, 5, 4, 3, 7, 2],
    [4, 3, 5, 6, 7, 2, 4, 1],
    [5, 1, 7, 6, 4, 3, 5, 2],
    [6, 6, 3, 7, 5, 2, 4, 1],
    [7, 1, 7, 4, 2, 6, 5, 3]]
#2 apartments left, used for matcher4
apartments =[
    [1, 3, 4, 2, 1, 6, 7, 5],
    [2, 6, 4, 2, 3, 5, 1, 7],
    [3, 6, 3, 5, 7, 2, 4, 1],
    [4, 1, 6, 3, 2, 4, 7, 5],
    [5, 1, 6, 5, 3, 4, 7, 2]]

matcher1 = matching.Matcher()
matcher2 = matching.Matcher()
matcher3 = matching.Matcher()
matcher4 = matching.Matcher()

#no input
matcher1.match()
matcher1.print_result()

#no applicants
for apartment in apartments:
    matcher2.input_apartment(apartment)
matcher2.match()
matcher2.print_result()

#no apartments
for applicant in applicants:
    matcher3.input_applicant(applicant)
matcher3.match()
matcher3.print_result()

#uneven pairing
for applicant in applicants:
    matcher4.input_applicant(applicant)
for apartment in apartments:
    matcher4.input_apartment(apartment)

matcher4.match()
matcher4.print_result()

stop = timeit.default_timer()
#print('Time: ', stop - start) 

class Matcher:
    def __init__(self):
        self.applicants_dict = {}
        self.apartments_dict = {}
        #[applicant, apartment]
        self.matches = []

    def input_applicant(self, applicant):
        self.applicants_dict[applicant[0]] = applicant[1:]

    def input_apartment(self, apartment):
        self.apartments_dict[apartment[0]] = apartment[1:]

    def propose_applicant(self, applicant, apartment):
        matchFound = False
        try:
            apartment_pref = self.apartments_dict[apartment].copy()
            apartment_pref = list(filter(self.is_applicant_avaliable, apartment_pref))#filter only avaliable applicants
        except Exception as e:
            #print(e)
            return matchFound
        if self.is_apartment_avaliable(apartment):
            if apartment_pref[0] == applicant:
                self.matches.append([applicant, apartment])
                #print("Match accepted. Applicant {}, Apartment {}.".format(applicant, apartment))
                matchFound = True
            else:
                pass
                #print("Match rejected, not first choice. Applicant {}, Apartment {}.".format(applicant, apartment))
        return matchFound

    def is_apartment_avaliable(self, apartment):
        isAvaliable = False
        result = [match for match in self.matches if match[1] == apartment]
        if result == []:
            isAvaliable = True
        return isAvaliable

    def is_applicant_avaliable(self, applicant):
        isAvaliable = False
        result = [match for match in self.matches if match[0] == applicant]
        if result == []:
            isAvaliable = True
        return isAvaliable

    def match(self):
        noMatch = True
        applicant_proposal_count = 1#number of apartments applicant will propose starting from the first avaliable prefference
        #loop ends when there are no more avaliable applicants or apartments
        print()
        while len(self.matches) < min(len(self.applicants_dict), len(self.apartments_dict)):
            for applicant, prefference in self.applicants_dict.items():
                applicant_pref = prefference
                applicant_pref = list(filter(self.is_apartment_avaliable, applicant_pref))#filter only avaliable apartments
                for apartment in applicant_pref[:applicant_proposal_count]:
                    if self.propose_applicant(applicant, apartment):
                        noMatch = False
                        applicant_proposal_count = 1
            #if iteration ends with no match increase number of proposals
            if noMatch:
                applicant_proposal_count += 1
            else:
                noMatch = True
                applicant_proposal_count = 1
            if applicant_proposal_count > len(self.apartments_dict):
                break
        sorted_matches = sorted(self.matches, key=lambda match: match[0])
        return sorted_matches
    
    def print_result(self):
        sorted_matches = sorted(self.matches, key=lambda match: match[0])
        for match in sorted_matches:
            print("{} {}".format(match[0], match[1]))